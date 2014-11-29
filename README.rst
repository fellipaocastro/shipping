Shipping
========

This is a shipping calculator that estimates the time and cost of delivery
based on given route, receipt value and item's weight.

Requirements
------------

- Python 2.7.8
- pip 1.5.6

Setup
-----

.. code-block:: bash

    $ ./manage.sh setup

Usage
-----

.. code-block:: bash

    $ ./manage.sh run <origin> <destination> <receipt> <weight>

Log
---

    /tmp/shipping_YYYY-MM-DD.log (e.g., /tmp/shipping_2014-11-29.log)

.. code-block:: bash

    $ ./manage.sh log

Test
----

.. code-block:: bash

    $ ./manage.sh test

Source code check
-----------------

.. code-block:: bash

    $ ./manage.sh check
