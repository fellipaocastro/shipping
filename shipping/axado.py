#!/usr/bin/env python
# coding: utf-8

import sys


class Axado():

    @staticmethod
    def check_arguments_length(argv):
        if len(argv) == 5:
            return True
        return False

    @staticmethod
    def check_arguments_type(argv):
        if (not argv[1].isdigit()) and (not argv[2].isdigit()) and\
           (argv[3].isdigit()) and (argv[4].isdigit()):
            return True
        return False

    def main(self):
        if not self.check_arguments_length(sys.argv):
            print """It is required 4 arguments in order to successfuly \
calculate shipping.\n
They are: <origin> <destination> <receipt> <weight>."""
        elif not self.check_arguments_type(sys.argv):
            print """Whereas the first two arguments should be non-digits, \
third and fourth ones should be digits."""
        else:
            print "%s - %s - %s - %s" % (
                sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

if __name__ == '__main__':
    axado = Axado()
    axado.main()
