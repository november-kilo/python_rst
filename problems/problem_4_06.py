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
from constants import EARTH_MU
from helpers import get_input
from orbital_mechanics import OrbitalMechanics

mu = get_input('mu (m^3 / s^2)', EARTH_MU)
rp = get_input('periapsis radius (m)', 6578140)
vp = get_input('periapsis velocity (m/s)', 7850)
om = OrbitalMechanics(mu)

e = om.eq20(rp, vp)

print(f'e = %g' % e)
