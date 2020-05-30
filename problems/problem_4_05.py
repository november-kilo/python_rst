"""
http://www.braeunig.us/space/problem.htm#4.5

A satellite in Earth orbit passes through its perigee point at an altitude of
200 km above the Earth's surface and at a velocity of 7,850 m/s.  Calculate the
apogee altitude of the satellite.


SOLUTION,

   Given:  Rp = (6,378.14 + 200) * 1,000 = 6,578,140 m
           Vp = 7,850 m/s

   Equation (4.18),

      Ra = Rp / [2 * GM / (Rp * Vp2) - 1]
      Ra = 6,578,140 / [2 * 3.986005*1014 / (6,578,140 * 7,8502) - 1]
      Ra = 6,805,140 m

      Altitude @ apogee = 6,805,140 / 1,000 - 6,378.14 = 427.0 km
"""
from Constants import Constants
from OrbitalMechanics import OrbitalMechanics
from Util import Util


class Problem405:
    @staticmethod
    def do_problem():
        mu = Util.get_input('mu (m^3/s^2)', Constants.EARTH_MU)
        r = Util.get_input('central body radius (km)', Constants.EARTH_RADIUS)
        rp = Util.get_input('periapsis radius (km)', 200)
        vp = Util.get_input('periapsis velocity (m / s)', 7850)
        om = OrbitalMechanics(mu)
        
        rp = (rp + r) * 1000
        ra = om.eq18(rp, vp) / 1000 - r
        
        print('Apoapsis radius = %g' % ra)
