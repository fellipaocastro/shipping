#!/usr/bin/env python
# coding: utf-8

import unittest

from .axado import Axado


class AxadoTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.axado = Axado()

    def test_check_arguments_length_with_5_arguments(self):
        """
        check_arguments_length() should return True with 5 arguments
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]

        self.assertTrue(self.axado.check_arguments_length(argv))

    def test_check_arguments_length_with_3_arguments(self):
        """
        check_arguments_length() should return False with 3 arguments
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', ]

        self.assertFalse(self.axado.check_arguments_length(argv))

    def test_check_arguments_length_with_7_arguments(self):
        """
        check_arguments_length() should return False with 7 arguments
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', '5', '6', ]

        self.assertFalse(self.axado.check_arguments_length(argv))

    def test_check_arguments_type_with_first_argument_as_a_digit(
            self):
        """
        check_arguments_type() should return False if first argument is a digit
        """

        argv = ['axado.py', '1', 'brasilia', '50', '7', ]

        self.assertFalse(self.axado.check_arguments_type(argv))

    def test_check_arguments_type_with_first_argument_as_a_non_digit(
            self):
        """
        check_arguments_type() should return True if first argument is a
        non-digit
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]

        self.assertTrue(self.axado.check_arguments_type(argv))

    def test_check_arguments_type_with_second_argument_as_a_digit(
            self):
        """
        check_arguments_type() should return False if second argument is a
        digit
        """

        argv = ['axado.py', 'florianopolis', '1', '50', '7', ]

        self.assertFalse(self.axado.check_arguments_type(argv))

    def test_check_arguments_type_with_second_argument_as_a_non_digit(
            self):
        """
        check_arguments_type() should return True if second argument is a
        non-digit
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]

        self.assertTrue(self.axado.check_arguments_type(argv))

    def test_check_arguments_type_with_third_argument_as_a_non_digit(
            self):
        """
        check_arguments_type() should return False if third argument is a
        non-digit
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', 'curitiba', '7', ]

        self.assertFalse(self.axado.check_arguments_type(argv))

    def test_check_arguments_type_with_third_argument_as_a_digit(
            self):
        """
        check_arguments_type() should return True if third argument is a
        digit
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]

        self.assertTrue(self.axado.check_arguments_type(argv))

    def test_check_arguments_type_with_fourth_argument_as_a_non_digit(
            self):
        """
        check_arguments_type() should return False if fourth argument is a
        non-digit
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', '50', 'curitiba', ]

        self.assertFalse(self.axado.check_arguments_type(argv))

    def test_check_arguments_type_with_fourth_argument_as_a_digit(
            self):
        """
        check_arguments_type() should return True if fourth argument is a
        digit
        """

        argv = ['axado.py', 'florianopolis', 'brasilia', '50', '7', ]

        self.assertTrue(self.axado.check_arguments_type(argv))

if __name__ == '__main__':
    unittest.main()
