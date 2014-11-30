#!/usr/bin/env python
# coding: utf-8
import sys
import logging
import logging.config
import re
import csv
from decimal import Decimal

from settings import TABLES, TABLE1_NAME, TABLE2_NAME, LOGGING

logger = logging.getLogger(__name__)
logging.config.dictConfig(LOGGING)


class Shipping(object):

    message = ''

    def __init__(self, table, argv):
        logger.info('CALL %s.%s' % (type(self).__name__, '__init__'))
        self.table = table
        self.origin = argv[1].lower()
        self.destination = argv[2].lower()
        self.receipt = float(argv[3])
        self.weight = float(argv[4])
        logger.debug('self.table: %s' % self.table)
        logger.debug('self.origin: %s' % self.origin)
        logger.debug('self.destination: %s' % self.destination)
        logger.debug('self.receipt: %s' % self.receipt)
        logger.debug('self.weight: %s' % self.weight)

    @classmethod
    def check_arguments(cls, argv):
        logger.info('CALL %s.%s' % (cls.__name__, 'check_arguments'))
        if not cls.check_arguments_lengths(argv):
            cls.message = """It is required 4 arguments in order to \
successfuly calculate shipping.\n
They are: <origin> <destination> <receipt> <weight>.\n
e.g., florianopolis brasilia 50 7"""
        elif not cls.check_arguments_types(argv):
            cls.message = """Whereas the first two arguments should be valid \
city names, third and fourth ones should be valid numbers.\n
e.g., florianopolis brasilia 50 7"""
        else:
            return True
        return False

    @staticmethod
    def check_arguments_lengths(argv):
        logger.info('CALL %s.%s' % (
            Shipping.__name__, 'check_arguments_lengths'))
        return True if len(argv) == 5 else False

    @classmethod
    def check_arguments_types(cls, argv):
        logger.info('CALL %s.%s' % (cls.__name__, 'check_arguments_types'))
        return True if cls.is_valid_city_name(argv[1])\
            and cls.is_valid_city_name(argv[2])\
            and cls.is_valid_number(argv[3])\
            and cls.is_valid_number(argv[4]) else False

    @staticmethod
    def is_valid_city_name(city_name):
        logger.info('CALL %s.%s' % (Shipping.__name__, 'is_valid_city_name'))
        return re.match("^[a-zA-Z]+$", city_name) is not None

    @staticmethod
    def is_valid_number(number):
        logger.info('CALL %s.%s' % (Shipping.__name__, 'is_valid_number'))
        return re.match("^\d+\.?\d*$", number) is not None

    def calculate(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'calculate'))
        self.delivery_time = "-"
        self.price = "-"
        self.subtotal = 0.0
        if self.get_route_data():
            if self.check_limit():
                if self.get_price_per_kg():
                    self.sum_insurance()
                    self.sum_weight_price()
                    self.sum_fixed_tax()
                    self.sum_customs()
                    self.sum_icms()
                    self.price = float(Decimal(self.subtotal).quantize(
                        Decimal('.01'), rounding='ROUND_UP'))
        logger.debug('self.price: %s' % self.price)
        Shipping.message += "\n%s:%s, %s" % (
            self.table, self.delivery_time, self.price)
        logger.debug('Shipping.message: %s' % Shipping.message)

    def get_route_data(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'get_route_data'))
        with open(TABLES[self.table]['routes']) as csvfile:
            reader = csv.DictReader(
                csvfile, delimiter=TABLES[self.table]['delimiter'])
            for row in reader:
                if (row['origem'] == self.origin and row['destino'] ==
                        self.destination):
                    self.delivery_time = int(row['prazo'])
                    logger.debug('self.delivery_time: %s' % self.delivery_time)
                    self.insurance = float(row['seguro'])
                    logger.debug('self.insurance: %s' % self.insurance)
                    self.kg = row['kg']
                    logger.debug('self.kg: %s' % self.kg)
                    if self.table == TABLE1_NAME:
                        self.fixed = float(row['fixa'])
                        logger.debug('self.fixed: %s' % self.fixed)
                    elif self.table == TABLE2_NAME:
                        self.limit = float(row['limite'])
                        logger.debug('self.limit: %s' % self.limit)
                        self.icms = float(row['icms'])
                        logger.debug('self.icms: %s' % self.icms)
                        self.customs = float(row['alfandega'])
                        logger.debug('self.customs: %s' % self.customs)
                    return True
        return False

    def check_limit(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'check_limit'))
        if (self.table == TABLE2_NAME and self.limit > 0
                and self.weight > self.limit):
            self.delivery_time = "-"
            logger.debug('self.delivery_time: %s' % self.delivery_time)
            return False
        else:
            return True

    def get_price_per_kg(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'get_price_per_kg'))
        with open(TABLES[self.table]['price_per_kg']) as csvfile:
            reader = csv.DictReader(
                csvfile, delimiter=TABLES[self.table]['delimiter'])
            for row in reader:
                if row['nome'] == self.kg\
                    and float(row['inicial']) <= self.weight\
                    and (
                        (row['final'] != ''
                            and self.weight < float(row['final']))
                        or row['final'] == ''):
                                self.price_per_kg = float(row['preco'])
                                logger.debug(
                                    'self.price_per_kg: %s'
                                    % self.price_per_kg)
                                return True
        return False

    def sum_insurance(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_insurance'))
        self.subtotal += self.receipt * self.insurance / 100
        logger.debug('self.subtotal: %s' % self.subtotal)

    def sum_weight_price(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_weight_price'))
        self.subtotal += self.price_per_kg * self.weight
        logger.debug('self.subtotal: %s' % self.subtotal)

    def sum_fixed_tax(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_fixed_tax'))
        if self.table == TABLE1_NAME:
            self.subtotal += self.fixed
        logger.debug('self.subtotal: %s' % self.subtotal)

    def sum_customs(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_customs'))
        if self.table == TABLE2_NAME:
            self.subtotal += self.subtotal * (self.customs / 100)
        logger.debug('self.subtotal: %s' % self.subtotal)

    def sum_icms(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_icms'))
        if self.table == TABLE1_NAME:
            self.icms = TABLES[self.table]['icms']
        self.subtotal += self.subtotal / ((100 - self.icms) / 100)
        logger.debug('self.subtotal: %s' % self.subtotal)


def main():
    logger.info('CALL %s' % 'main')
    logger.info('sys.argv: %s' % sys.argv)
    logger.debug('Shipping.message: %s' % Shipping.message)
    try:
        if Shipping.check_arguments(sys.argv):
            for table in sorted(TABLES):
                Shipping(table, sys.argv).calculate()
        Shipping.message = Shipping.message.strip()
        logger.info('Shipping.message: %s' % Shipping.message)
        print Shipping.message
    except Exception as e:
        logger.error('Exception: %s' % e, exc_info=True)
        print "Oops, something went wrong."

if __name__ == '__main__':
    logger.info('--------------------------[BEGIN]--------------------------')
    logger.info('')
    main()
    logger.info('')
    logger.info('---------------------------[END]---------------------------')
