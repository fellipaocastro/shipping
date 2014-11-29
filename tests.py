#!/usr/bin/env python
# coding: utf-8
import unittest

from axado import Shipping


class ShippingStaticMethodsTestCase(unittest.TestCase):
    def test_check_arguments_lengths_1(self):
        """
        Shipping.check_arguments_lengths() should return True with 5 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_lengths(argv))

    def test_check_arguments_lengths_2(self):
        """
        Shipping.check_arguments_lengths() should return False with 3 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', ]
        self.assertFalse(Shipping.check_arguments_lengths(argv))

    def test_check_arguments_lengths_3(self):
        """
        Shipping.check_arguments_lengths() should return False with 7 arguments
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
        Shipping.is_valid_city_name() should return False with a not valid city
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
        Shipping.is_valid_number() should return False with a not valid number
        """
        self.assertFalse(Shipping.is_valid_number('florianopolis50'))


class ShippingClassMethodsTestCase(unittest.TestCase):
    def test_check_arguments_1(self):
        """
        Shipping.check_arguments should set proper Shipping.message in case it
        receives a wrong number of paremeters
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6', '7']
        message = """It is required 4 arguments in order to \
successfuly calculate shipping.\n
They are: <origin> <destination> <receipt> <weight>.\n
e.g., florianopolis brasilia 50 7"""
        Shipping.check_arguments(argv)
        self.assertEqual(message, Shipping.message)

    def test_check_arguments_2(self):
        """
        Shipping.check_arguments should return False in case it receives a
        wrong number of paremeters
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6', '7']
        check_arguments = Shipping.check_arguments(argv)
        self.assertFalse(check_arguments)

    def test_check_arguments_types_1(self):
        """
        Shipping.check_arguments_types() should return True if second argument
        is a valid city name
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_2(self):
        """
        Shipping.check_arguments_types() should return False if second argument
        is not a valid city name
        """
        argv = ['axado.py', '1', 'brasilia', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_3(self):
        """
        Shipping.check_arguments_types() should return True if third argument
        is a valid city name
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_4(self):
        """
        Shipping.check_arguments_types() should return False if third argument
        is not a valid city name
        """
        argv = ['axado.py', 'florianopolis', '1', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_5(self):
        """
        Shipping.check_arguments_types() should return True if fourth argument
        is a valid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_6(self):
        """
        Shipping.check_arguments_types() should return False if fourth argument
        is not a valid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', 'saopaulo', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_7(self):
        """
        Shipping.check_arguments_types() should return True if fifth argument
        is a valid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_8(self):
        """
        Shipping.check_arguments_types() should return False if fifth argument
        is not a valid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', 'saopaulo', ]
        self.assertFalse(Shipping.check_arguments_types(argv))


class ShippingTestCase(unittest.TestCase):
    def test___init__1(self):
        """
        Shipping.__init__() should properly initialize Shipping.table
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping('tabela', argv)
        self.assertEqual(shipping.table, 'tabela')

    def test___init__2(self):
        """
        Shipping.__init__() should properly initialize Shipping.origin
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping('tabela', argv)
        self.assertEqual(shipping.origin, 'saopaulo')

    def test___init__3(self):
        """
        Shipping.__init__() should properly initialize Shipping.destination
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping('tabela', argv)
        self.assertEqual(shipping.destination, 'florianopolis')

    def test___init__4(self):
        """
        Shipping.__init__() should properly initialize Shipping.receipt
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping('tabela', argv)
        self.assertEqual(shipping.receipt, 50.0)

    def test___init__5(self):
        """
        Shipping.__init__() should properly initialize Shipping.weight
        """
        argv = ['axado.py', 'SaoPaulo', 'Florianopolis', '50', '6']
        shipping = Shipping('tabela', argv)
        self.assertEqual(shipping.weight, 6.0)

if __name__ == '__main__':
    unittest.main()
