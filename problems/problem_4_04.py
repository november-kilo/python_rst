"""
http://www.braeunig.us/space/problem.htm#4.4

An artificial Earth satellite is in an elliptical orbit which brings it to
an altitude of 250 km at perigee and out to an altitude of 500 km at apogee.
Calculate the velocity of the satellite at both perigee and apogee.


SOLUTION,

   Given:  Rp = (6,378.14 + 250) * 1,000 = 6,628,140 m
           Ra = (6,378.14 + 500) * 1,000 = 6,878,140 m

   Equations (4.16) and (4.17),

      Vp = SQRT[ 2 * GM * Ra / (Rp * (Ra + Rp)) ]
      Vp = SQRT[ 2 * 3.986005*1014 * 6,878,140 / (6,628,140 * (6,878,140 + 6,628,140)) ]
      Vp = 7,826 m/s

      Va = SQRT[ 2 * GM * Rp / (Ra * (Ra + Rp)) ]
      Va = SQRT[ 2 * 3.986005*1014 * 6,628,140 / (6,878,140 * (6,878,140 + 6,628,140)) ]
      Va = 7,542 m/s
"""
from Constants import Constants
from OrbitalMechanics import OrbitalMechanics
from Util import Util


class Problem404:
    @staticmethod
    def do_problem():
        mu = Util.get_input('mu (m^3/s^2)', Constants.EARTH_MU)
        r = Util.get_input('central body radius (m)', Constants.EARTH_RADIUS)
        rp = Util.get_input('periapsis (km)', 250)
        ra = Util.get_input('apoapsis (km)', 500)

        om = OrbitalMechanics(mu)
        rp = (rp + r) * 1000
        ra = (ra + r) * 1000

        vp = om.eq16(rp, ra)
        va = om.eq17(rp, ra)

        print('Vp = ' + str(vp) + ' m/s\nVa = ' + str(va) + ' m/s')
