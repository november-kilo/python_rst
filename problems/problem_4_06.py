"""
http://www.braeunig.us/space/problem.htm#4.6
Calculate the eccentricity of the orbit for the satellite in problem 4.5.
SOLUTION,
   Given:  Rp = 6,578,140 m
           Vp = 7,850 m/s

   Equation (4.20),
      e = Rp * Vp2 / GM - 1
      e = 6,578,140 * 7,8502 / 3.986005*1014 - 1
      e = 0.01696
"""
from Constants import Constants
from OrbitalMechanics import OrbitalMechanics
from Util import Util


class Problem406:
    @staticmethod
    def do_problem():
        mu = Util.get_input('mu (km^3 / s^2)', Constants.EARTH_MU)
        rp = Util.get_input('periapsis radius (m)', 6578.14)
        vp = Util.get_input('periapsis velocity (km/s)', 7.85)
        om = OrbitalMechanics(mu)
        
        e = om.eq20(rp, vp)
        
        print(f'e = %g' % e)
