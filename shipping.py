#!/usr/bin/env python
# coding: utf-8
import re
import csv
import logging
import logging.config
from decimal import Decimal

from settings import TABLE1_NAME, TABLE2_NAME, TABLES, LOGGING

logger = logging.getLogger(__name__)
logging.config.dictConfig(LOGGING)


class Shipping():

    def __init__(self, table, argv):
        self.table = table
        self.origin = argv[1].lower()
        self.destination = argv[2].lower()
        self.receipt = float(argv[3])
        self.weight = float(argv[4])
        self.calculate()

    @staticmethod
    def is_valid_city_name(city_name):
        return re.match("^[a-zA-Z]+$", city_name) is not None

    @staticmethod
    def is_valid_number(number):
        return re.match("^\d+\.?\d*$", number) is not None

    @staticmethod
    def check_arguments_length(argv):
        return True if len(argv) == 5 else False

    @staticmethod
    def check_arguments_type(argv):
        return True if Shipping.is_valid_city_name(argv[1])\
            and Shipping.is_valid_city_name(argv[2])\
            and Shipping.is_valid_number(argv[3])\
            and Shipping.is_valid_number(argv[4]) else False

    def get_route_data(self):
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

    def get_price_per_kg(self):
        with open(TABLES[self.table]['price_per_kg']) as csvfile:
            reader = csv.DictReader(
                csvfile, delimiter=TABLES[self.table]['delimiter'])
            for row in reader:
                if (row['nome'] == self.kg and row['final'] != '' and (
                        float(row['inicial']) <= self.weight <
                        float(row['final']))):
                    self.price_per_kg = float(row['preco'])
                    return True
                elif (row['nome'] == self.kg and row['final'] == '' and (
                        float(row['inicial']) <= self.weight)):
                    self.price_per_kg = float(row['preco'])
                    return True
        return False

    @staticmethod
    def check_arguments(argv):
        if not Shipping.check_arguments_length(argv):
            print """It is required 4 arguments in order to successfuly \
calculate shipping.\n
They are: <origin> <destination> <receipt> <weight>.\n
e.g., florianopolis brasilia 50 7"""
        elif not Shipping.check_arguments_type(argv):
            print """Whereas the first two arguments should be valid city \
names, third and fourth ones should be valid numbers.\n
e.g., florianopolis brasilia 50 7"""
        else:
            return True
        return False

    def check_limit(self):
        if self.table == TABLE2_NAME and self.weight > self.limit:
            self.delivery_time = "-"
            return False
        else:
            return True

    def sum_insurance(self):
        self.subtotal += self.receipt * self.insurance / 100

    def sum_fixed_tax(self):
        if self.table == TABLE1_NAME:
            self.subtotal += self.fixed

    def sum_weight_price(self):
        self.subtotal += self.price_per_kg * self.weight

    def sum_customs(self):
        if self.table == TABLE2_NAME:
            self.subtotal += self.subtotal * (self.customs / 100)

    def sum_icms(self):
        if self.table == TABLE1_NAME:
            self.icms = TABLES[self.table]['icms']
        self.subtotal += self.subtotal / ((100 - self.icms) / 100)

    def calculate(self):
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
        print "%s:%s, %s" % (self.table, self.delivery_time, self.price)
