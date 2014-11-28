#!/usr/bin/env python
# coding: utf-8
import unittest

from shipping import Shipping


class ShippingStaticTestCase(unittest.TestCase):
    def test_is_valid_city_name_with_an_invalid_city_name(self):
        """
        is_valid_city_name() should return False with an invalid city name
        """
        self.assertFalse(Shipping.is_valid_city_name('florianopolis50'))

    def test_is_valid_city_name_with_a_valid_city_name(self):
        """
        is_valid_city_name() should return True with a valid city name
        """
        self.assertTrue(Shipping.is_valid_city_name('Florianopolis'))

    def test_is_valid_number_with_an_invalid_number(self):
        """
        is_valid_number() should return False with an invalid number
        """
        self.assertFalse(Shipping.is_valid_number('florianopolis50'))

    def test_is_valid_number_with_a_valid_number(self):
        """
        is_valid_number() should return True with a valid number
        """
        self.assertTrue(Shipping.is_valid_number('50.001'))

    def test_check_arguments_length_with_5_arguments(self):
        """
        check_arguments_length() should return True with 5 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_length(argv))

    def test_check_arguments_length_with_3_arguments(self):
        """
        check_arguments_length() should return False with 3 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', ]
        self.assertFalse(Shipping.check_arguments_length(argv))

    def test_check_arguments_length_with_7_arguments(self):
        """
        check_arguments_length() should return False with 7 arguments
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', '5', '6', ]
        self.assertFalse(Shipping.check_arguments_length(argv))

    def test_check_arguments_type_with_second_argument_as_an_invalid_city_name(
            self):
        """
        check_arguments_type() should return False if second argument is an
        invalid city name
        """
        argv = ['axado.py', '1', 'brasilia', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_type(argv))

    def test_check_arguments_type_with_second_argument_as_a_valid_city_name(
            self):
        """
        check_arguments_type() should return True if second argument is a
        valid city name
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_type(argv))

    def test_check_arguments_type_with_third_argument_as_an_invalid_city_name(
            self):
        """
        check_arguments_type() should return False if third argument is an
        invalid city name
        """
        argv = ['axado.py', 'florianopolis', '1', '50', '7', ]
        self.assertFalse(Shipping.check_arguments_type(argv))

    def test_check_arguments_type_with_third_argument_as_a_valid_city_name(
            self):
        """
        check_arguments_type() should return True if third argument is a
        valid city name
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_type(argv))

    def test_check_arguments_type_with_fourth_argument_as_an_invalid_number(
            self):
        """
        check_arguments_type() should return False if fourth argument is an
        invalid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', 'saopaulo', '7', ]
        self.assertFalse(Shipping.check_arguments_type(argv))

    def test_check_arguments_type_with_fourth_argument_as_a_valid_number(
            self):
        """
        check_arguments_type() should return True if fourth argument is a
        valid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_type(argv))

    def test_check_arguments_type_with_fifth_argument_as_an_invalid_number(
            self):
        """
        check_arguments_type() should return False if fifth argument is an
        invalid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', 'saopaulo', ]
        self.assertFalse(Shipping.check_arguments_type(argv))

    def test_check_arguments_type_with_fifth_argument_as_a_valid_number(
            self):
        """
        check_arguments_type() should return True if fifth argument is a
        valid number
        """
        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]
        self.assertTrue(Shipping.check_arguments_type(argv))

if __name__ == '__main__':
    unittest.main()
