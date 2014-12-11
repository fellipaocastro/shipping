#!/usr/bin/env python
# coding: utf-8
import logging
import logging.config
import re
import csv
from decimal import Decimal

from settings import TABLES, LOGGING, TABLE1_NAME, TABLE2_NAME

logger = logging.getLogger(__name__)
logging.config.dictConfig(LOGGING)


class Shipping(object):

    def __init__(self, table, argv):
        logger.info('CALL %s.%s' % (type(self).__name__, '__init__'))

        self.table = table

        self.origin, self.destination = argv[1].lower(), argv[2].lower()

        self.receipt, self.weight = float(argv[3]), float(argv[4])

    @staticmethod
    def check_arguments_length(argv):
        logger.info('CALL %s.%s' % (
            Shipping.__name__, 'check_arguments_length'))

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

        return re.match('^[a-zA-Z]+$', city_name) is not None

    @staticmethod
    def is_valid_number(number):
        logger.info('CALL %s.%s' % (Shipping.__name__, 'is_valid_number'))

        return re.match('^\d+\.?\d*$', number) is not None

    def calculate(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'calculate'))

        self.delivery_time, self.price, self.subtotal = '-', '-', 0.0

        if self.set_route_data() and self.check_limit() and \
                self.set_price_per_kg():

                    self.sum_insurance()

                    self.sum_weight_price()

                    self.sum_fixed_tax()

                    self.sum_customs()

                    self.sum_icms()

                    self.price = float(Decimal(self.subtotal).quantize(
                        Decimal('.01'), rounding='ROUND_UP'))

    def set_route_data(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'set_route_data'))

        with open(TABLES[self.table]['routes']) as csvfile:

            reader = csv.DictReader(
                csvfile, delimiter=TABLES[self.table]['delimiter'])

            for row in reader:

                if (row['origem'] == self.origin and row['destino'] ==
                        self.destination):

                    self.delivery_time = int(row['prazo'])

                    self.insurance = float(row['seguro'])

                    self.kg = row['kg']

                    if self.table == TABLE1_NAME:

                        self.fixed = float(row['fixa'])

                    elif self.table == TABLE2_NAME:

                        self.limit = float(row['limite'])

                        self.icms = float(row['icms'])

                        self.customs = float(row['alfandega'])

                    return True
        return False

    def check_limit(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'check_limit'))

        if (self.table == TABLE2_NAME and self.limit > 0
                and self.weight > self.limit):

            self.delivery_time = '-'

            return False

        else:
            return True

    def set_price_per_kg(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'set_price_per_kg'))

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

                                return True
        return False

    def sum_insurance(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_insurance'))

        self.subtotal += self.receipt * self.insurance / 100

    def sum_weight_price(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_weight_price'))

        self.subtotal += self.price_per_kg * self.weight

    def sum_fixed_tax(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_fixed_tax'))

        if self.table == TABLE1_NAME:

            self.subtotal += self.fixed

    def sum_customs(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_customs'))

        if self.table == TABLE2_NAME:

            self.subtotal += self.subtotal * (self.customs / 100)

    def sum_icms(self):
        logger.info('CALL %s.%s' % (type(self).__name__, 'sum_icms'))

        if self.table == TABLE1_NAME:

            self.icms = TABLES[self.table]['icms']

        self.subtotal += self.subtotal / ((100 - self.icms) / 100)
