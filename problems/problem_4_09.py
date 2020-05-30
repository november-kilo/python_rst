"""
http://www.braeunig.us/space/problem.htm#4.9

Calculate the eccentricity of the orbit for the satellite in problem 4.8.


SOLUTION,

   Given:  r1 = 6,628,140 m
           v1 = 7,900 m/s
            = 89o

   Equation (4.27),

      e = SQRT[ (r1 * v12 / GM - 1)2 * sin2  + cos2  ]
      e = SQRT[ (6,628,140 * 7,9002 / 3.986005*1014 - 1)2 * sin2(89) + cos2(89) ]
      e = 0.0416170
"""
from Constants import Constants
from OrbitalMechanics import OrbitalMechanics
from Util import Util


class Problem409:
    @staticmethod
    def do_problem():
        r = Util.Util.get_input('burnout radius (m)', 6628140)
        v = Util.Util.get_input('burnout velocity (m/s)', 7900)
        z = Util.Util.get_input('burnout zenith (deg)', 89)
        mu = Util.Util.get_input('mu (m^3 / s^2', Constants.EARTH_MU)
        om = OrbitalMechanics(mu)
        e = om.eq27(r, v, z)
        print(f'eccentricity = %g' % e)
