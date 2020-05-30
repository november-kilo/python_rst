"""
http://www.braeunig.us/space/problem.htm#4.8

A satellite is launched into Earth orbit where its launch vehicle burns out at
an altitude of 250 km.  At burnout the satellite's velocity is 7,900 m/s with the
zenith angle equal to 89 degrees.  Calculate the satellite's altitude at perigee
and apogee.


SOLUTION,

   Given:  r1 = (6,378.14 + 250) * 1,000 = 6,628,140 m
           v1 = 7,900 m/s
            = 89o

   Equation (4.26),

      (Rp / r1)1,2 = ( -C ± SQRT[ C2 - 4 * (1 - C) * -sin2  ]) / (2 * (1 - C))

      where  C = 2 * GM / (r1 * v12)
             C = 2 * 3.986005*1014 / (6,628,140 * 7,9002)
             C = 1.927179

      (Rp / r1)1,2 = ( -1.927179 ± SQRT[ 1.9271792 - 4 * -0.927179 * -sin2(89) ]) / (2 * -0.927179)
      (Rp / r1)1,2 = 0.996019 and 1.082521

   Perigee Radius, Rp = Rp1 = r1 * (Rp / r1)1

      Rp = 6,628,140 * 0.996019
      Rp = 6,601,750 m

      Altitude @ perigee = 6,601,750 / 1,000 - 6,378.14 = 223.6 km

   Apogee Radius, Ra = Rp2 = r1 * (Rp / r1)2

      Ra = 6,628,140 * 1.082521
      Ra = 7,175,100 m

      Altitude @ agogee = 7,175,100 / 1,000 - 6,378.14 = 797.0 km
"""
from Constants import Constants
from OrbitalMechanics import OrbitalMechanics
from Util import Util


class Problem408:
    @staticmethod
    def do_problem():
        r = Util.get_input('central body radius (km)', Constants.EARTH_RADIUS)
        r1 = Util.get_input('burnout altitude (km)', 250)
        r1 = (r + r1) * 1000
        v1 = Util.get_input('burnout velocity (m/s)', 7900)
        gamma1 = Util.get_input('burnout zenith (deg)', 89)
        mu = Util.get_input('mu (m^3/s^2)', Constants.EARTH_MU)
        om = OrbitalMechanics(mu)
        
        rp, ra, c = om.eq26(r1, v1, gamma1)
        altitude_at_periapsis = (rp / 1000) - r
        altitude_at_apoapsis = (ra / 1000) - r
        
        print(f'Altitude at periapsis: %g km' % altitude_at_periapsis)
        print(f'Altitude at apoapsis: %g km' % altitude_at_apoapsis)
