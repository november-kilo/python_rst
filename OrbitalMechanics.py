import math


class OrbitalMechanics:
    def __init__(self, mu):
        self.mu = mu

    def eq16(self, rp, ra):
        """Returns the periapsis velocity from mu, Rp, and Ra"""
        term1 = 2 * self.mu * ra
        term2 = rp * (ra + rp)
        return math.sqrt(term1 / term2)

    def eq17(self, rp, ra):
        """Returns the apoapsis velocity from mu, Rp, and Ra"""
        term1 = 2 * self.mu * rp
        term2 = ra * (ra + rp)
        return math.sqrt(term1 / term2)

    def eq18(self, rp, vp):
        """Returns the apoapsis radius from mu, Rp, and Vp"""
        term1 = 2 * self.mu
        term2 = rp * vp * vp
        term3 = (term1 / term2) - 1
        return rp / term3

    def eq20(self, rp, vp):
        """Returns the eccentricity from mu, Rp, and Vp"""
        term1 = rp * vp * vp
        return (term1 / self.mu) - 1

    @staticmethod
    def eq21(a, eccentricity):
        """Returns the periapsis radius from semimajor axis and eccentricity"""
        return a * (1 - eccentricity)

    @staticmethod
    def eq22(a, eccentricity):
        """Returns the apoapsis radius from semimajor axis and eccentricity"""
        return a * (1 + eccentricity)

    def eq26(self, r, v, gamma):
        """Returns the periapsis and apoapsis radius from mu, radius, velocity, and zenith angle"""
        g = math.radians(gamma)
        c = (2 * self.mu) / (r * v ** 2)
        term1 = math.sqrt(c ** 2 - (4 * (1 - c) * -(math.sin(g) ** 2)))
        term2 = 2 * (1 - c)

        r_plus = (-c + term1) / term2
        r_minus = (-c - term1) / term2

        rp = min(r_plus, r_minus) * r
        ra = max(r_plus, r_minus) * r

        return rp, ra, c

    def eq27(self, r, v, gamma):
        """Returns the eccentricity from mu, radius, velocity, and zenith angle"""
        g = math.radians(gamma)
        return math.sqrt((r * v ** 2 / self.mu - 1) ** 2 * math.sin(g) ** 2 + math.cos(g) ** 2)

    def eq28(self, r, v, gamma):
        """Returns the true anomaly from mu, radius, velocity, and zenith angle"""
        g = math.radians(gamma)
        term1 = r * v ** 2 / self.mu
        term2 = math.sin(g)
        term3 = math.cos(g)
        term4 = term1 * term2 * term3
        term5 = term1 * term2 ** 2 - 1
        return math.atan(term4 / term5)

    def eq32(self, r, v):
        """Returns the semimajor axis from mu, radius, and velocity"""
        term1 = 2 / r
        term2 = v ** 2 / self.mu
        term3 = term1 - term2
        return 1 / term3

    @staticmethod
    def eq33(azimuth_heading, latitude):
        """Returns inclination from azimuth heading and surface latitude"""
        term1 = math.cos(math.degrees(azimuth_heading))
        term2 = math.sin(math.degrees(latitude))
        return math.acos(term1 * term2)

    @staticmethod
    def eq34(azimuth_heading, latitude):
        """Returns angular distance between the ascending node and the burnout point measured in the orbital plane
        from azimuth heading and surface latitude """
        term1 = math.tan(math.radians(latitude))
        term2 = math.cos(math.radians(azimuth_heading))

        return math.atan(term1 / term2)

    @staticmethod
    def eq35(azimuth_heading, latitude):
        """Returns delta-l (angular distance between the ascending node and the burnout point measured in the orbital
        plane """
        term1 = math.sin(math.radians(latitude))
        term2 = math.tan(math.radians(azimuth_heading))
        return math.atan(term1 * term2)

    @staticmethod
    def eq36(ell, nu):
        """Returns argument of periapsis from ell and true anomaly"""
        return ell - nu

    @staticmethod
    def eq37(l_2, delta_l):
        """Returns L1 = L2 - dL"""
        return l_2 - delta_l
