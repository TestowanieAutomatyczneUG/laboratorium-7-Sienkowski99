import unittest
from sample.zad2 import *
from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class

class CheckerParameterizedPackage(unittest.TestCase):

    @parameterized.expand([
        ("halibutZZiemniakamimmmmmmPycha!!!111oneone", True),
        ("HASLo!23", True),
        ("HumanistaBeletrysta2137()", True),
        ("haaaaaaaaaaaaaaaa)", False),
        ("haslomalarskie128e", False),
    ])
    def test_one_parameterized_string_input(self, text, expected_validation):
        self.assertEqual(self.tmp.ValidPassword(text), expected_validation)

    def setUp(self):
        self.tmp = Checker()

    @parameterized.expand([
        (23, ValueError),
        ([], ValueError),
        (True, ValueError),
    ])
    def test_one_parameterized_exceptions(self, thingy, expected):
        self.assertRaises(expected, self.tmp.ValidPassword, thingy)


@parameterized_class(('input', 'expected'), [
        ("Haslo123@", True),
        ("!!!!!!!!!!!!!!!!", False),
        ("237942789374892738", False),
        ("ARBITER", False),
        ("HassaN0)", True)
])
class CheckerParameterizedPackage2(unittest.TestCase):
    def setUp(self):
        self.tmp = Checker()

    def test_second_parameterized(self):
        self.assertEqual(self.tmp.ValidPassword(self.input), self.expected)


if __name__ == '__main__':
    unittest.main()
