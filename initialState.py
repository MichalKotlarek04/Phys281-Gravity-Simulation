from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from spiceypy import sxform, mxvg
from poliastro import constants
from astropy.constants import G

class getBodyState:
    t = Time("2019-11-27 17:00:00.0", scale="tdb")
    def __init__(self, body):
        pos, vel = get_body_barycentric_posvel(body, t, ephemeris="jpl")

        state_vector = [pos.xyz[0].to("m").value,
                    pos.xyz[1].to("m").value,
                    pos.xyz[2].to("m").value,
                    vel.xyz[0].to("m/s").value,
                    vel.xyz[1].to("m/s").value,
                    vel.xyz[2].to("m/s").value]


        trans = sxform("J2000", "ECLIPJ2000", t.jd)

        statevececl = mxvg(trans, state_vector)

        position = [statevececl[0], statevececl[1], statevececl[2]]
        velocity = [statevececl[3], statevececl[4], statevececl[5]]

        # finds initial position and velocity (with respect to solar system barycentre) of the body
        self.initial_state = [position, velocity]
