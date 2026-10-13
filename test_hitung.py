import unittest
from hitung import bagi, kurang, kali, pangkat, bagi_bulat, modulo, faktorial

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

    def test_kali(self):
        self.assertEqual(kali(3,4),12)
        self.assertEqual(kali(-2,5),-10)
        self.assertEqual(kali(0,10),0)

    def test_pangkat(self):
        self.assertEqual(pangkat(2,3),8)
        self.assertEqual(pangkat(5,0),1)
        self.assertEqual(pangkat(-2,3),-8)

    def test_bagi_bulat(self):
        self.assertEqual(bagi_bulat(7,3),2)
        self.assertEqual(bagi_bulat(-7,3),-3)
        with self.assertRaises(ValueError):
            bagi_bulat(5,0)

    def test_modulo(self):
        self.assertEqual(modulo(7,3),1)
        self.assertEqual(modulo(-7,3),2)
        with self.assertRaises(ValueError):
            modulo(5,0)

    def test_faktorial(self):
        self.assertEqual(faktorial(0), 1)
        self.assertEqual(faktorial(1), 1)
        self.assertEqual(faktorial(5), 120)
        with self.assertRaises(ValueError) as ctx:
            faktorial(-3)
        self.assertEqual(str(ctx.exception), "n negatif")

if __name__ == "__main__":
    unittest.main()
