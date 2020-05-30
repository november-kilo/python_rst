"""
http://www.braeunig.us/space/problem.htm#4.10
Calculate the angle  from perigee point to launch point for the satellite
in problem 4.8.
SOLUTION,
   Given:  r1 = 6,628,140 m
           v1 = 7,900 m/s
            = 89o
   Equation (4.28),
      tan  = (r1 * v12 / GM) * sin  * cos  / [(r1 * v12 / GM) * sin2  - 1]
      tan  = (6,628,140 * 7,9002 / 3.986005*1014) * sin(89) * cos(89)
	       / [(6,628,140 * 7,9002 / 3.986005*1014) * sin2(89) - 1]
      tan  = 0.48329
       = arctan(0.48329)
       = 25.794o
"""
import math

from Constants import Constants
from OrbitalMechanics import OrbitalMechanics
from Util import Util


class Problem410:
    @staticmethod
    def do_problem():
        r = Util.get_input('burnout radius (m)', 6628140)
        v = Util.get_input('burnout velocity (m/s)', 7900)
        z = Util.get_input('burnout zenith (deg)', 89)
        mu = Util.get_input('mu (m^3 / s^2', Constants.EARTH_MU)
        om = OrbitalMechanics(mu)
        true_anomaly = om.eq28(r, v, z)
        print(f'true_anomaly = %g' % math.degrees(true_anomaly))
