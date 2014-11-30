#!/usr/bin/env python
# coding: utf-8
import unittest

from axado import Shipping
from settings import TABLE1_NAME, TABLE2_NAME


class ShippingStaticMethodsTestCase(unittest.TestCase):
    def test_check_arguments_lengths_1(self):
        """
        Shipping.check_arguments_lengths() should return True with 5 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_lengths(argv))

    def test_check_arguments_lengths_2(self):
        """
        Shipping.check_arguments_lengths() should return False with less than 5
        arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', ]
        self.assertFalse(Shipping.check_arguments_lengths(argv))

    def test_check_arguments_lengths_3(self):
        """
        Shipping.check_arguments_lengths() should return False with more than 5
        arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', '5', '6', ]
        self.assertFalse(Shipping.check_arguments_lengths(argv))

    def test_is_valid_city_name_1(self):
        """
        Shipping.is_valid_city_name() should return True with a valid city name
        """
        self.assertTrue(Shipping.is_valid_city_name('Florianopolis'))

    def test_is_valid_city_name_2(self):
        """
        Shipping.is_valid_city_name() should return False with an ivalid city
        name
        """
        self.assertFalse(Shipping.is_valid_city_name('florianopolis50'))

    def test_is_valid_number_1(self):
        """
        Shipping.is_valid_number() should return True with a valid number
        """
        self.assertTrue(Shipping.is_valid_number('50.001'))

    def test_is_valid_number_2(self):
        """
        Shipping.is_valid_number() should return False with an invalid number
        """
        self.assertFalse(Shipping.is_valid_number('florianopolis50'))


class ShippingClassMethodsTestCase(unittest.TestCase):
    def test_check_arguments_1(self):
        """
        Shipping.check_arguments should return True with right number and types
        of arguments
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        check_arguments = Shipping.check_arguments(argv)
        self.assertTrue(check_arguments)

    def test_check_arguments_2(self):
        """
        Shipping.check_arguments should set proper Shipping.message with a
        wrong number of paremeters
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6', '7']
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
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6', '7']
        check_arguments = Shipping.check_arguments(argv)
        self.assertFalse(check_arguments)

    def test_check_arguments_4(self):
        """
        Shipping.check_arguments should set proper Shipping.message with wrong
        types of arguments
        """
        argv = ['axado.py', '50', 'Florianopolis', 'SaoPaulo', '6']
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
        argv = ['axado.py', '50', 'Florianopolis', 'SaoPaulo', '6']
        check_arguments = Shipping.check_arguments(argv)
        self.assertFalse(check_arguments)

    def test_check_arguments_types_1(self):
        """
        Shipping.check_arguments_types() should return True with valid
        arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_2(self):
        """
        Shipping.check_arguments_types() should return False with second
        argument as an invalid city name
        """
        argv = ['axado.py', '1', 'brasilia', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_3(self):
        """
        Shipping.check_arguments_types() should return False with third
        argument as an invalid city name
        """
        argv = ['axado.py', 'florianopolis', '1', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_4(self):
        """
        Shipping.check_arguments_types() should return False with fourth
        argument as an invalid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', 'saopaulo', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_5(self):
        """
        Shipping.check_arguments_types() should return False with fifth
        argument as an invalid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', 'saopaulo', ]
        self.assertFalse(Shipping.check_arguments_types(argv))


class ShippingTestCase(unittest.TestCase):
    def test___init__1(self):
        """
        Shipping.__init__() should properly initialize self.table
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.table, TABLE1_NAME)

    def test___init__2(self):
        """
        Shipping.__init__() should properly initialize self.origin
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.origin, 'saopaulo')

    def test___init__3(self):
        """
        Shipping.__init__() should properly initialize self.destination
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.destination, 'florianopolis')

    def test___init__4(self):
        """
        Shipping.__init__() should properly initialize self.receipt
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.receipt, 50.0)

    def test___init__5(self):
        """
        Shipping.__init__() should properly initialize self.weight
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        self.assertEqual(shipping.weight, 6.0)


class ShippingTable1TestCase(unittest.TestCase):
    def test_calculate(self):
        """
        Shipping.calculate() should properly set Shipping.message
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        message = "\n%s:%s, %s" % (TABLE1_NAME, 1, 106.29)
        Shipping.message = ''
        shipping.calculate()
        self.assertEqual(Shipping.message, message)

    def test_get_route_data_1(self):
        """
        Shipping.get_route_data shoud properly set self.delivery_time
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.delivery_time, 1)

    def test_get_route_data_2(self):
        """
        Shipping.get_route_data shoud properly set self.insurance
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.insurance, 3.0)

    def test_get_route_data_3(self):
        """
        Shipping.get_route_data shoud properly set self.kg
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.kg, 'central')

    def test_get_route_data_4(self):
        """
        Shipping.get_route_data shoud properly set self.fixed
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE1_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.fixed, 8.0)


class ShippingTable2TestCase(unittest.TestCase):
    def test_calculate(self):
        """
        Shipping.calculate() should properly set Shipping.message
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        message = "\n%s:%s, %s" % (TABLE2_NAME, 4, 138.92)
        Shipping.message = ''
        shipping.calculate()
        self.assertEqual(Shipping.message, message)

    def test_get_route_data_1(self):
        """
        Shipping.get_route_data shoud properly set self.delivery_time
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.delivery_time, 4)

    def test_get_route_data_2(self):
        """
        Shipping.get_route_data shoud properly set self.insurance
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.insurance, 7.0)

    def test_get_route_data_3(self):
        """
        Shipping.get_route_data shoud properly set self.kg
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.kg, 'central')

    def test_get_route_data_4(self):
        """
        Shipping.get_route_data shoud properly set self.limit
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.limit, 100.00)

    def test_get_route_data_5(self):
        """
        Shipping.get_route_data shoud properly set self.icms
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.icms, 6.0)

    def test_get_route_data_6(self):
        """
        Shipping.get_route_data shoud properly set self.customs
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping(TABLE2_NAME, argv)
        shipping.get_route_data()
        self.assertEqual(shipping.customs, 6.0)


if __name__ == '__main__':
    unittest.main()
