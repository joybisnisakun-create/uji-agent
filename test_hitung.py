import unittest
from hitung import bagi, kurang

class TestHitung(unittest.TestCase):
    def test_bagi_normal(self):
        self.assertEqual(bagi(10, 2), 5.0)
        self.assertEqual(bagi(-9, 3), -3.0)
        self.assertAlmostEqual(bagi(1, 3), 0.3333333, places=6)

    def test_bagi_nol(self):
        with self.assertRaises(ValueError) as ctx:
            bagi(5, 0)
        self.assertEqual(str(ctx.exception), "pembagi nol")

    def test_kurang(self):
        self.assertEqual(kurang(10, 4), 6)
        self.assertEqual(kurang(3, 7), -4)
        self.assertEqual(kurang(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
