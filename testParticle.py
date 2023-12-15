from Particle import Particle
import matplotlib.pyplot as plt
import numpy as np


# initialise your particle
Ball = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([20, 20, 0]),
    acceleration=np.array([0, -9.81, 0]),  # g=-9.81 m/s^2 in y-direction
    name="Ball",
    mass=500.
)
print(Ball)

time = 0  # initial time stamp
deltaT = 1e-5  # time steps of 0.01ms

times = []
y = []

# run simulation until ball hits the ground
while Ball.position[1] >= 0.0:
    # store the time stamps
    times.append(time)

    # store the y-position
    y.append(Ball.position[1])

    # update the time
    time += deltaT

    # update the positions and velocities
    Ball.updatePosition(deltaT)
    Ball.updateVelocity(deltaT)

# print out some information
print(max(times))
print(max(y))
print(len(times))

#The expected value from the analytical solution is 4.07747s

# plot the data
plt.plot(times, y, 'r-', label='trajectory')
plt.xlabel('time (s)')
plt.ylabel('y-position (m)')
plt.legend()
plt.show()
