import unittest
import leapyear


class leaptest(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.is_leap(2000), True)

    def test2(self):
        self.assertEqual(leapyear.is_leap(2021), False)

    def test3(self):
        self.assertEqual(leapyear.is_leap(2400), True)

    def test4(self):
        self.assertEqual(leapyear.is_leap(2022), False)

    def test5(self):
        self.assertEqual(leapyear.is_leap(2800), True)


if __name__ == '__main__':
    unittest.main()
