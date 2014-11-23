#!/usr/bin/env python
# coding: utf-8

import sys
import re
from decimal import Decimal


class Axado():

    @staticmethod
    def is_valid_city_name(city_name):
        return re.match("^[a-zA-Z]+$", city_name) is not None

    @staticmethod
    def is_valid_number(number):
        return re.match("^\d+\.?\d*$", number) is not None

    @staticmethod
    def check_arguments_length(argv):
        if len(argv) == 5:
            return True
        return False

    @staticmethod
    def check_arguments_type(argv):
        if (Axado.is_valid_city_name(argv[1])) \
                and (Axado.is_valid_city_name(argv[2])) \
                and (Axado.is_valid_number(argv[3])) \
                and (Axado.is_valid_number(argv[4])):
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
            self.receipt = float(Decimal(sys.argv[3]).quantize(
                Decimal('.01'), rounding='ROUND_UP'))
            self.weight = float(Decimal(sys.argv[4]).quantize(
                Decimal('.01'), rounding='ROUND_UP'))
            print "%s - %s - %s - %s" % (
                self.origin, self.destination, self.receipt, self.weight)

if __name__ == '__main__':
    axado = Axado()
    axado.main()
