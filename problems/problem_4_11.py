"""
http://www.braeunig.us/space/problem.htm#4.11

Calculate the semi-major axis of the orbit for the satellite in problem 4.8.


SOLUTION,

   Given:  r1 = 6,628,140 m
           v1 = 7,900 m/s

   Equation (4.32),

      a = 1 / ( 2 / r1 - v12 / GM )
      a = 1 / ( 2 / 6,628,140 - 7,9002 / 3.986005×1014) )
      a = 6,888,430 m
"""
from Constants import Constants
from OrbitalMechanics import OrbitalMechanics
from Util import Util


class Problem411:
    @staticmethod
    def do_problem():
        mu = Util.get_input('mu (m^3 / s^2)', Constants.EARTH_MU)
        r = Util.get_input('burnout radius (m)', 6628140)
        v = Util.get_input('burnout velocity (m/s)', 7900)
        om = OrbitalMechanics(mu)
        a = om.eq32(r, v)
        print(f'semimajor axis (m) = %g' % a)
