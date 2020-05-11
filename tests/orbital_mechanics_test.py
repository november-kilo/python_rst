import math
import unittest

from orbital_mechanics import OrbitalMechanics


def close_enough(a, b):
    return math.isclose(a, b, rel_tol=0.00001)


class TestOrbitalMechanics(unittest.TestCase):
    def setUp(self):
        self.om = OrbitalMechanics(3.986005e14)

    def test_eq16(self):
        expected = 1.68735e+06

        actual = self.om.eq16(200, 500)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq17(self):
        expected = 674940

        actual = self.om.eq17(200, 500)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq18(self):
        expected = 0.00313151

        actual = self.om.eq18(200, 7900)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq20(self):
        expected = -0.999969

        actual = self.om.eq20(200, 7900)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq21(self):
        expected = 5400

        actual = OrbitalMechanics.eq21(6000, 0.1)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq22(self):
        expected = 6600

        actual = OrbitalMechanics.eq22(6000, 0.1)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq26(self):
        expected_rp = 2.81878
        expected_ra = 6000
        expected_c = 2128.93

        actual_rp, actual_ra, actual_c = self.om.eq26(6000, 7900, 89)

        self.assertTrue(close_enough(actual_rp, expected_rp), f'actual = %g; expected = %g' % (actual_rp, expected_rp))
        self.assertTrue(close_enough(actual_ra, expected_ra), f'actual = %g; expected = %g' % (actual_ra, expected_ra))
        self.assertTrue(close_enough(actual_c, expected_c), f'actual = %g; expected = %g' % (actual_c, expected_c))

    def test_eq27(self):
        expected = 0.999061

        actual = self.om.eq27(6000, 7900, 89)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq28(self):
        expected = -1.64083e-05

        actual = self.om.eq28(6000, 7900, 89)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq32(self):
        expected = 3001.41

        actual = self.om.eq32(6000, 7900)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq33(self):
        expected = 2.92511

        actual = OrbitalMechanics.eq33(25, 65)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq34(self):
        expected = 1.17094

        actual = OrbitalMechanics.eq34(25, 65)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq35(self):
        expected = 0.399852

        actual = OrbitalMechanics.eq35(25, 65)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq36(self):
        expected = 36

        actual = OrbitalMechanics.eq36(62, 26)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))

    def test_eq37(self):
        expected = 36

        actual = OrbitalMechanics.eq37(62, 26)

        self.assertTrue(close_enough(actual, expected), f'actual = %g; expected = %g' % (actual, expected))
