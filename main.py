#!/usr/bin/env python
# coding: utf-8
import sys
import logging
import logging.config

from settings import TABLES, LOGGING
from shipping import Shipping

logger = logging.getLogger(__name__)
logging.config.dictConfig(LOGGING)


def main():
    logger.info('CALL %s' % 'main')
    logger.info('sys.argv: %s' % sys.argv)
    try:
        if not Shipping.check_arguments_length(sys.argv):
            message = '''It is required 4 arguments in order to successfuly \
calculate shipping.\n
They are: <origin> <destination> <receipt> <weight>.\n
e.g., florianopolis brasilia 50 7'''
            logger.warning('message: %s' % message)
        elif not Shipping.check_arguments_types(sys.argv):
            message = '''Whereas the first two arguments should be valid city \
names, third and fourth ones should be valid numbers.\n
e.g., florianopolis brasilia 50 7'''
            logger.warning('message: %s' % message)
        else:
            message = ''
            for table in sorted(TABLES):
                shipping = Shipping(table, sys.argv)
                shipping.calculate()
                message += '%s:%s, %s\n' % (
                    shipping.table, shipping.delivery_time, shipping.price)
            message = message.strip()
            logger.info('message: %s' % message)
    except Exception:
        message = 'Oops, something went wrong.'
        logger.exception('message: %s' % message)
    finally:
        print message

if __name__ == '__main__':
    logger.info('--------------------------[BEGIN]--------------------------')
    logger.info('')
    main()
    logger.info('')
    logger.info('---------------------------[END]---------------------------')
