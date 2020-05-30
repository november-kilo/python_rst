"""
http://www.braeunig.us/space/problem.htm#4.7

A satellite in Earth orbit has a semi-major axis of 6,700 km and an eccentricity
of 0.01.  Calculate the satellite's altitude at both perigee and apogee.


SOLUTION,

   Given:  a = 6,700 km
           e = 0.01

   Equation (4.21) and (4.22),

      Rp = a * (1 - e)
      Rp = 6,700 * (1 - .01)
      Rp = 6,633 km

      Altitude @ perigee = 6,633 - 6,378.14 = 254.9 km

      Ra = a * (1 + e)
      Ra = 6,700 * (1 + .01)
      Ra = 6,767 km

      Altitude @ apogee = 6,767 - 6,378.14 = 388.9 km
"""
from Constants import Constants
from OrbitalMechanics import OrbitalMechanics
from Util import Util


class Problem407:
    @staticmethod
    def do_problem():
        mu = Util.get_input('mu (m^3/s^2)', Constants.EARTH_MU)
        a = Util.get_input('semimajor axis (km)', 6700)
        eccentricity = Util.get_input('eccentricity (dimensionless)', 0.01)
        r = Util.get_input('central body radius (km)', Constants.EARTH_RADIUS)
        
        rp = OrbitalMechanics.eq21(a, eccentricity)
        ap = rp - r
        ra = OrbitalMechanics.eq22(a, eccentricity)
        aa = ra - r

        print('Rp = ' + str(rp) + ' km; altitude at periapsis = ' + str(ap) + ' km')
        print('Ra = ' + str(ra) + ' km; altitude at apoapsis = ' + str(aa) + ' km')
