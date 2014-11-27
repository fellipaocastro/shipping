#!/usr/bin/env python
# coding: utf-8
import sys
import logging
import logging.config

from axado.settings import TABLES, LOGGING
from shipping.shipping import Shipping

logger = logging.getLogger(__name__)
logging.config.dictConfig(LOGGING)

if __name__ == '__main__':
    try:
        if Shipping.check_arguments(sys.argv):
            for table in sorted(TABLES):
                Shipping(table, sys.argv)
    except Exception as e:
        logger.error('Exception: %s' % e, exc_info=True)
        print "Oops, something went wrong."
