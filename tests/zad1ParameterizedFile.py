import unittest
from sample.zad1 import *


class HammingParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("data/zad1_data_test")
      tmpHamming = Hamming()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(",")
            a, b, result = data[0], data[1], int(data[2].strip("\n"))
            self.assertEqual(tmpHamming.distance(a, b), result)
      fileTest.close()

    def test_exceptions_from_file(self):
      fileTest = open("data/zad1_exceptions_data_test")
      tmpHamming = Hamming()
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(",")
            a, b, exception = data[0], data[1], data[2].strip("\n")
            self.assertRaises(ValueError, tmpHamming.distance, a, b)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()
