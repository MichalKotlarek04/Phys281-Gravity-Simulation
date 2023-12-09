import numpy as np
from Particle import Particle
import copy
from Ephemerides import getBodyState
earthMass = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass
)
satPosition = earthRadius + (35786 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite = Particle(
    position=np.array([satPosition, 0, 0]),
    velocity=np.array([0, satVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=100.
)

dT = 6 # Sets the time interval
time_passed = 0
Data = [] # deep copy
loop_test_condition = 1

for j in range(200000):
    Earth.updateGravitationalAcceleration(Satellite)
    Satellite.updateGravitationalAcceleration(Earth)
    # Calculates new acceleration vectors for Earth and Satellite
    Earth.update(dT)
    Satellite.update(dT)
    # Updates position and velocity with the Euler method
    time_passed += dT

    if int(loop_test_condition) == 1:
        Data.append([time_passed, copy.deepcopy(Earth), copy.deepcopy(Satellite)])
        loop_test_condition = 0.01
    else:
        loop_test_condition += 0.01

np.save("TwoBodyTest", Data, allow_pickle=True)
