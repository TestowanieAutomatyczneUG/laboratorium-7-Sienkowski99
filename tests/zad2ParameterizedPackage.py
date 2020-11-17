# import unittest
# from sample.zad2 import *
# from nose.tools import assert_equal, assert_raises
# from parameterized import parameterized, parameterized_class
#
#
# class CheckerParameterizedPackage(unittest.TestCase):
#
#     def setUp(self):
#         self.tmp = Checker()
#
#     @parameterized.expand([
#         ("halibutZZiemniakamimmmmmmPycha!!!111oneone", True),
#         ("HASLo!23", True),
#         ("HumanistaBeletrysta2137()", True),
#         ("haaaaaaaaaaaaaaaa)", False),
#         ("haslomalarskie128e", False),
#         ("Haslo123@", True),
#         ("!!!!!!!!!!!!!!!!", False),
#         ("237942789374892738", False),
#         ("ARBITER", False),
#         ("HassaN0)", True)
#     ])
#     def test_one_parameterized_string_input(self, text, expected_validation):
#         self.assertEqual(self.tmp.ValidPassword(text), expected_validation)
#
#     @parameterized.expand([
#         (23, ValueError),
#         ([], ValueError),
#         (True, ValueError),
#     ])
#     def test_one_parameterized_exceptions(self, thingy, expected):
#         self.assertRaises(expected, self.tmp.ValidPassword, thingy)
#
#
# @parameterized_class(('input', 'expected'), [
#         ("halibutZZiemniakamimmmmmmPycha!!!111oneone", True),
#         ("HASLo!23", True),
#         ("HumanistaBeletrysta2137()", True),
#         ("haaaaaaaaaaaaaaaa)", False),
#         ("haslomalarskie128e", False),
#         ("Haslo123@", True),
#         ("!!!!!!!!!!!!!!!!", False),
#         ("237942789374892738", False),
#         ("ARBITER", False),
#         ("HassaN0)", True)
#     ])
# class CheckerParameterizedPackage2(unittest.TestCase):
#     def setUp(self):
#         self.tmp = Checker()
#
#     def test_second_parameterized(self):
#         self.assertEqual(self.tmp.ValidPassword(self.input), self.expected)
#
#
# @parameterized_class(('input', 'expected'), [
#         (23, ValueError),
#         ([], ValueError),
#         (True, ValueError),
#     ])
# class CheckerParameterizedPackage2Exceptions(unittest.TestCase):
#     def setUp(self):
#         self.tmp = Checker()
#
#     def test_one_parameterized_exceptions(self):
#         self.assertRaises(self.expected, self.tmp.ValidPassword, self.input)
#
#
# @parameterized([
#         ("halibutZZiemniakamimmmmmmPycha!!!111oneone", True),
#         ("HASLo!23", True),
#         ("HumanistaBeletrysta2137()", True),
#         ("haaaaaaaaaaaaaaaa)", False),
#         ("haslomalarskie128e", False),
#         ("Haslo123@", True),
#         ("!!!!!!!!!!!!!!!!", False),
#         ("237942789374892738", False),
#         ("ARBITER", False),
#         ("HassaN0)", True)
#     ])
# def test_one_parameterized_string_input(text, expected_validation):
#     assert_equal(Checker().ValidPassword(text), expected_validation)
#
#
# @parameterized([
#         (23, ValueError),
#         ([], ValueError),
#         (True, ValueError),
#     ])
# def test_one_parameterized_exceptions(thingy, expected):
#     assert_raises(expected, Checker().ValidPassword, thingy)
#
#
# if __name__ == '__main__':
#     unittest.main()
