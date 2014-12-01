#!/usr/bin/env python
# coding: utf-8
import unittest
import sys
from cStringIO import StringIO

from mock import patch

from axado import Shipping, main
from settings import TABLES, TABLE1_NAME, TABLE2_NAME


class ShippingStaticMethodsTestCase(unittest.TestCase):
    def test_check_arguments_lengths_1(self):
        """
        Shipping.check_arguments_lengths should return True with 5 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_lengths(argv))

    def test_check_arguments_lengths_2(self):
        """
        Shipping.check_arguments_lengths should return False with less than 5
        arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', ]
        self.assertFalse(Shipping.check_arguments_lengths(argv))

    def test_check_arguments_lengths_3(self):
        """
        Shipping.check_arguments_lengths should return False with more than 5
        arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', '5', '6', ]
        self.assertFalse(Shipping.check_arguments_lengths(argv))

    def test_is_valid_city_name_1(self):
        """
        Shipping.is_valid_city_name should return True with a valid city name
        """
        self.assertTrue(Shipping.is_valid_city_name('Florianopolis'))

    def test_is_valid_city_name_2(self):
        """
        Shipping.is_valid_city_name should return False with an ivalid city
        name
        """
        self.assertFalse(Shipping.is_valid_city_name('florianopolis50'))

    def test_is_valid_number_1(self):
        """
        Shipping.is_valid_number should return True with a valid number
        """
        self.assertTrue(Shipping.is_valid_number('50.001'))

    def test_is_valid_number_2(self):
        """
        Shipping.is_valid_number should return False with an invalid number
        """
        self.assertFalse(Shipping.is_valid_number('florianopolis50'))


class ShippingClassMethodsTestCase(unittest.TestCase):
    def test_check_arguments_1(self):
        """
        Shipping.check_arguments should return True with right number and types
        of arguments
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        check_arguments = Shipping.check_arguments(argv)
        self.assertTrue(check_arguments)

    def test_check_arguments_2(self):
        """
        Shipping.check_arguments should set proper Shipping.message with a
        wrong number of paremeters
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6', '7']
        message = """It is required 4 arguments in order to \
successfuly calculate shipping.\n
They are: <origin> <destination> <receipt> <weight>.\n
e.g., florianopolis brasilia 50 7"""
        Shipping.check_arguments(argv)
        self.assertEqual(message, Shipping.message)

    def test_check_arguments_3(self):
        """
        Shipping.check_arguments should return False with a wrong number of
        paremeters
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6', '7']
        check_arguments = Shipping.check_arguments(argv)
        self.assertFalse(check_arguments)

    def test_check_arguments_4(self):
        """
        Shipping.check_arguments should set proper Shipping.message with wrong
        types of arguments
        """
        argv = ['axado.py', '50', 'florianopolis', 'saopaulo', '6']
        message = """Whereas the first two arguments should be valid \
city names, third and fourth ones should be valid numbers.\n
e.g., florianopolis brasilia 50 7"""
        Shipping.check_arguments(argv)
        self.assertEqual(message, Shipping.message)

    def test_check_arguments_5(self):
        """
        Shipping.check_arguments should return False with wrong types of
        arguments
        """
        argv = ['axado.py', '50', 'florianopolis', 'saopaulo', '6']
        check_arguments = Shipping.check_arguments(argv)
        self.assertFalse(check_arguments)

    def test_check_arguments_types_1(self):
        """
        Shipping.check_arguments_types should return True with valid
        arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_2(self):
        """
        Shipping.check_arguments_types should return False with second
        argument as an invalid city name
        """
        argv = ['axado.py', '1', 'brasilia', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_3(self):
        """
        Shipping.check_arguments_types should return False with third
        argument as an invalid city name
        """
        argv = ['axado.py', 'florianopolis', '1', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_4(self):
        """
        Shipping.check_arguments_types should return False with fourth
        argument as an invalid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', 'saopaulo', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_5(self):
        """
        Shipping.check_arguments_types should return False with fifth
        argument as an invalid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', 'saopaulo', ]
        self.assertFalse(Shipping.check_arguments_types(argv))


class ShippingTestCase(unittest.TestCase):
    def test___init__1(self):
        """
        Shipping.__init__ should properly initialize self.table
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.table, TABLE1_NAME)

    def test___init__2(self):
        """
        Shipping.__init__ should properly initialize self.origin
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.origin, 'saopaulo')

    def test___init__3(self):
        """
        Shipping.__init__ should properly initialize self.destination
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.destination, 'florianopolis')

    def test___init__4(self):
        """
        Shipping.__init__ should properly initialize self.receipt
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.receipt, 50.0)

    def test___init__5(self):
        """
        Shipping.__init__ should properly initialize self.weight
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.weight, 6.0)

    def test_calculate_1(self):
        """
        Shipping.calculate should properly set Shipping.message
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        message = "%s:%s, %s" % (TABLE1_NAME, 1, 106.29)
        shipping.calculate()
        self.assertEqual(Shipping.message, message)

    def test_get_price_per_kg_1(self):
        """
        Shipping.get_price_per_kg should properly set self.price_per_kg if any
        row matches the following rule:
        row['nome'] == self.kg
        and float(row['inicial']) <= self.weight
        and row['final'] != ''
        and self.weight < float(row['final'])
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.kg = 'central'
        shipping.get_price_per_kg()
        self.assertEqual(shipping.price_per_kg, 7.0)

    def test_get_price_per_kg_2(self):
        """
        Shipping.get_price_per_kg should return True if any row matches the
        following rule:
        row['nome'] == self.kg
        and float(row['inicial']) <= self.weight
        and row['final'] != ''
        and self.weight < float(row['final'])
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.kg = 'central'
        get_price_per_kg = shipping.get_price_per_kg()
        self.assertTrue(get_price_per_kg)

    def test_get_price_per_kg_3(self):
        """
        Shipping.get_price_per_kg should properly set self.price_per_kg if any
        row matches the following rule:
        row['nome'] == self.kg
        and float(row['inicial']) <= self.weight
        and row['final'] == ''
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '34']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.kg = 'central'
        shipping.get_price_per_kg()
        self.assertEqual(shipping.price_per_kg, 10.0)

    def test_get_price_per_kg_4(self):
        """
        Shipping.get_price_per_kg should return True if any row matches the
        following rule:
        row['nome'] == self.kg
        and float(row['inicial']) <= self.weight
        and row['final'] == ''
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '34']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.kg = 'central'
        get_price_per_kg = shipping.get_price_per_kg()
        self.assertTrue(get_price_per_kg)

    def test_get_price_per_kg_5(self):
        """
        Shipping.get_price_per_kg should return False if no row matches the
        following rule:
        row['nome'] == self.kg
        and float(row['inicial']) <= self.weight
        and (
            (row['final'] != ''
                and self.weight < float(row['final']))
            or row['final'] == '')
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.kg = 'central2'
        get_price_per_kg = shipping.get_price_per_kg()
        self.assertFalse(get_price_per_kg)

    def test_sum_insurance_1(self):
        """
        Shipping.sum_insurance should properly set self.subtotal
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.subtotal = 0.0
        shipping.insurance = 3.0
        shipping.sum_insurance()
        self.assertEqual(shipping.subtotal, 1.5)

    def test_sum_weight_price_1(self):
        """
        Shipping.sum_weight_price should properly set self.subtotal
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.subtotal = 1.5
        shipping.price_per_kg = 7.0
        shipping.sum_weight_price()
        self.assertEqual(shipping.subtotal, 43.5)

    def test_sum_icms_1(self):
        """
        Shipping.sum_icms should properly set self.subtotal
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.subtotal = 51.5
        shipping.sum_icms()
        self.assertEqual(shipping.subtotal, 106.2872340425532)


class ShippingTable1TestCase(unittest.TestCase):
    def test_get_route_data_1(self):
        """
        Shipping.get_route_data shoud properly set self.delivery_time
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.delivery_time, 1)

    def test_get_route_data_2(self):
        """
        Shipping.get_route_data shoud properly set self.insurance
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.insurance, 3.0)

    def test_get_route_data_3(self):
        """
        Shipping.get_route_data shoud properly set self.kg
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.kg, 'central')

    def test_get_route_data_4(self):
        """
        Shipping.get_route_data shoud properly set self.fixed
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.fixed, 8.0)

    def test_get_route_data_5(self):
        """
        Shipping.get_route_data shoud return True if any row matches the
        following rule:
        row['origem'] == self.origin and row['destino'] == self.destination
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        get_route_data = shipping.get_route_data()
        self.assertTrue(get_route_data)

    def test_get_route_data_6(self):
        """
        Shipping.get_route_data should return False if no row matches the
        following rule:
        row['origem'] == self.origin and row['destino'] ==
        self.destination
        """
        argv = ['axado.py', 'manaus', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        get_route_data = shipping.get_route_data()
        self.assertFalse(get_route_data)

    def test_check_limit_1(self):
        """
        Shipping.check_limit should return True
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        check_limit = shipping.check_limit()
        self.assertTrue(check_limit)

    def test_sum_fixed_tax_1(self):
        """
        Shipping.sum_fixed_tax should properly set self.subtotal
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.subtotal, shipping.fixed = 43.5, 8.0
        shipping.sum_fixed_tax()
        self.assertEqual(shipping.subtotal, 51.5)

    def test_sum_customs_1(self):
        """
        Shipping.sum_customs should not change the value of self.subtotal
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.subtotal = 51.5
        shipping.sum_customs()
        self.assertEqual(shipping.subtotal, 51.5)

    def test_sum_icms_1(self):
        """
        Shipping.sum_icms should properly set self.icms
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.subtotal = 51.5
        shipping.sum_icms()
        self.assertEqual(shipping.icms, TABLES[TABLE1_NAME]['icms'])


class ShippingTable2TestCase(unittest.TestCase):
    def test_get_route_data_1(self):
        """
        Shipping.get_route_data shoud properly set self.delivery_time
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.delivery_time, 4)

    def test_get_route_data_2(self):
        """
        Shipping.get_route_data shoud properly set self.insurance
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.insurance, 7.0)

    def test_get_route_data_3(self):
        """
        Shipping.get_route_data shoud properly set self.kg
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.kg, 'central')

    def test_get_route_data_4(self):
        """
        Shipping.get_route_data shoud properly set self.limit
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.limit, 100.00)

    def test_get_route_data_5(self):
        """
        Shipping.get_route_data shoud properly set self.icms
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.icms, 6.0)

    def test_get_route_data_6(self):
        """
        Shipping.get_route_data shoud properly set self.customs
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.customs, 6.0)

    def test_get_route_data_7(self):
        """
        Shipping.get_route_data shoud return True if any row matches the
        following rule:
        row['origem'] == self.origin and row['destino'] == self.destination
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        get_route_data = shipping.get_route_data()
        self.assertTrue(get_route_data)

    def test_get_route_data_8(self):
        """
        Shipping.get_route_data shoud return False if no row matches the
        following rule:
        row['origem'] == self.origin and row['destino'] ==
        self.destination
        """
        argv = ['axado.py', 'manaus', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        get_route_data = shipping.get_route_data()
        self.assertFalse(get_route_data)

    def test_check_limit_1(self):
        """
        Shipping.check_limit should return True with self.limit <= 0
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.limit = 0
        check_limit = shipping.check_limit()
        self.assertTrue(check_limit)

    def test_check_limit_2(self):
        """
        Shipping.check_limit should return True with self.limit > 0 and
        self.weight <= self.limit
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.limit = 100.00
        check_limit = shipping.check_limit()
        self.assertTrue(check_limit)

    def test_check_limit_3(self):
        """
        Shipping.check_limit should properly set self.delivery_time
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.limit = 5.00
        shipping.check_limit()
        self.assertEqual(shipping.delivery_time, "-")

    def test_check_limit_4(self):
        """
        Shipping.check_limit should return True with self.limit > 0 and
        self.weight > self.limit
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.limit = 5.00
        check_limit = shipping.check_limit()
        self.assertFalse(check_limit)

    def test_sum_fixed_tax_1(self):
        """
        Shipping.sum_fixed_tax should not change the value of self.subtotal
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.subtotal = 63.5
        shipping.sum_fixed_tax()
        self.assertEqual(shipping.subtotal, 63.5)

    def test_sum_customs_1(self):
        """
        Shipping.sum_customs should properly set self.subtotal
        """
        argv = ['axado.py', 'saopaulo', 'florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.subtotal, shipping.customs = 63.5, 6.0
        shipping.sum_customs()
        self.assertEqual(shipping.subtotal, 67.31)


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.original_sys_argv = sys.argv
        sys.argv = ['axado.py', 'saopaulo', 'florianopolis',
                    '50', '6']

    def tearDown(self):
        sys.argv = self.original_sys_argv

    def test_main_1(self):
        """
        main should properly print Shipping.message
        """
        message = "%s:%s, %s\n%s:%s, %s\n" % (
            TABLE1_NAME, 1, 106.29, TABLE2_NAME, 4, 138.92)
        with patch('sys.stdout', new=StringIO()) as fake_sys_stdout:
            main()
            self.assertEqual(fake_sys_stdout.getvalue(), message)

    def test_main_2(self):
        """
        main should properly print Shipping.message
        """
        message = "%s:%s, %s\n%s:%s, %s\n" % (
            TABLE1_NAME, 1, 106.29, TABLE2_NAME, 4, 138.92)
        with patch('sys.stdout', new=StringIO()) as fake_sys_stdout:
            main()
            self.assertEqual(fake_sys_stdout.getvalue(), message)


if __name__ == '__main__':
    unittest.main()
