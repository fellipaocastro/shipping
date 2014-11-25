#!/usr/bin/env python
# coding: utf-8

import sys
import re
import csv
from decimal import Decimal

from settings import DATABASES


class Axado():

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
        return True if Axado.is_valid_city_name(argv[1])\
            and Axado.is_valid_city_name(argv[2])\
            and Axado.is_valid_number(argv[3])\
            and Axado.is_valid_number(argv[4]) else False

    def lookup_table_routes(self):
        with open(DATABASES['table']['routes']) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row['origem'] == self.origin and row['destino'] ==
                        self.destination):
                    self.delivery_time = int(row['prazo'])
                    self.insurance = float(row['seguro'])
                    self.kg = row['kg']
                    self.fixed = float(row['fixa'])
                    return True
        return False

    def lookup_table_price_per_kg(self):
        with open(DATABASES['table']['price_per_kg']) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row['nome'] == self.kg and (
                        float(row['inicial']) <= self.weight <=
                        float(row['final']))):
                    self.price_per_kg = float(row['preco'])
                    return True
        return False

    def main(self):
        if not self.check_arguments_length(sys.argv):
            print """It is required 4 arguments in order to successfuly \
calculate shipping.\n
They are: <origin> <destination> <receipt> <weight>.\n
e.g., florianopolis brasilia 50 7"""
        elif not self.check_arguments_type(sys.argv):
            print """Whereas the first two arguments should be valid city \
names, third and fourth ones should be valid numbers.\n
e.g., florianopolis brasilia 50 7"""
        else:
            self.origin = sys.argv[1].lower()
            self.destination = sys.argv[2].lower()
            self.receipt = float(sys.argv[3])
            self.weight = float(sys.argv[4])
            # self.receipt = float(Decimal(sys.argv[3]).quantize(
            #     Decimal('.01'), rounding='ROUND_UP'))
            # self.weight = float(Decimal(sys.argv[4]).quantize(
            #     Decimal('.01'), rounding='ROUND_UP'))

            print "%s - %s - %s - %s" % (
                self.origin, self.destination, self.receipt, self.weight)

            if not self.lookup_table_routes():
                print """NOT FOUND"""
            else:
                print "%s - %s - %s - %s" % (
                    self.delivery_time, self.insurance, self.kg, self.fixed)
                if not self.lookup_table_price_per_kg():
                    print """NOT FOUND"""
                else:
                    print "%s" % self.price_per_kg

if __name__ == '__main__':
    axado = Axado()
    axado.main()
