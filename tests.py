#!/usr/bin/env python
# coding: utf-8
import unittest

from axado import Shipping


class ShippingStaticMethodsTestCase(unittest.TestCase):
    def test_is_valid_city_name_with_an_invalid_city_name(self):
        """
        Shipping.is_valid_city_name() should return False with an invalid city
        name
        """
        self.assertFalse(Shipping.is_valid_city_name('florianopolis50'))

    def test_is_valid_city_name_with_a_valid_city_name(self):
        """
        Shipping.is_valid_city_name() should return True with a valid city name
        """
        self.assertTrue(Shipping.is_valid_city_name('Florianopolis'))

    def test_is_valid_number_with_an_invalid_number(self):
        """
        Shipping.is_valid_number() should return False with an invalid number
        """
        self.assertFalse(Shipping.is_valid_number('florianopolis50'))

    def test_is_valid_number_with_a_valid_number(self):
        """
        Shipping.is_valid_number() should return True with a valid number
        """
        self.assertTrue(Shipping.is_valid_number('50.001'))

    def test_check_arguments_lengths_with_5_arguments(self):
        """
        Shipping.check_arguments_lengths() should return True with 5 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_lengths(argv))

    def test_check_arguments_lengths_with_3_arguments(self):
        """
        Shipping.check_arguments_lengths() should return False with 3 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', ]
        self.assertFalse(Shipping.check_arguments_lengths(argv))

    def test_check_arguments_lengths_with_7_arguments(self):
        """
        Shipping.check_arguments_lengths() should return False with 7 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', '5', '6', ]
        self.assertFalse(Shipping.check_arguments_lengths(argv))


class ShippingClassMethodsTestCase(unittest.TestCase):
    def test_check_arguments_types_with_2nd_argument_as_an_invalid_city_name(
            self):
        """
        Shipping.check_arguments_types() should return False if 2nd argument
        is an invalid city name
        """
        argv = ['axado.py', '1', 'brasilia', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_with_2nd_argument_as_a_valid_city_name(
            self):
        """
        check_arguments_types() should return True if 2nd argument is a valid
        city name
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_with_3rd_argument_as_an_invalid_city_name(
            self):
        """
        check_arguments_types() should return False if 3rd argument is an
        invalid city name
        """
        argv = ['axado.py', 'florianopolis', '1', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_with_3rd_argument_as_a_valid_city_name(
            self):
        """
        check_arguments_types() should return True if 3rd argument is a valid
        city name
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_with_4th_argument_as_an_invalid_number(
            self):
        """
        check_arguments_types() should return False if 4th argument is an
        invalid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', 'saopaulo', '7', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_with_4th_argument_as_a_valid_number(self):
        """
        check_arguments_types() should return True if 4th argument is a valid
        number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_with_5th_argument_as_an_invalid_number(
            self):
        """
        check_arguments_types() should return False if 5th argument is an
        invalid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', 'saopaulo', ]
        self.assertFalse(Shipping.check_arguments_types(argv))

    def test_check_arguments_types_with_5th_argument_as_a_valid_number(self):
        """
        check_arguments_types() should return True if 5th argument is a valid
        number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_types(argv))

if __name__ == '__main__':
    unittest.main()
