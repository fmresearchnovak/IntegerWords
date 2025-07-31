
import unittest

from integerwords.IntegerWords import EnglishInteger

class TestIntegerWords(unittest.TestCase):

    def test_main_functionality(self):
        self.assertEqual(str(EnglishInteger(1)), "one")
        self.assertEqual(str(EnglishInteger(50)), "fifty")
        self.assertEqual(str(EnglishInteger(52)), "fifty two")
        self.assertEqual(str(EnglishInteger(331002651)), "three hundred thirty one million two thousand six hundred fifty one")

        self.assertEqual(str(EnglishInteger(0)), "zero")
        self.assertEqual(str(EnglishInteger(446744073709551615)), 
            "four hundred fourty six quadrillion seven hundred fourty four trillion seventy three billion seven hundred nine million five hundred fifty one thousand six hundred fifteen")
        self.assertEqual(str(EnglishInteger(3002)), "three thousand two")


    # TODO: add tests for set_value and get_value

    # TODO: add tests for intw() helper method


if __name__ == '__main__':
    unittest.main()

