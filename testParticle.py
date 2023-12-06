from Particle import Particle 
import matplotlib.pyplot as plt 
import math
import numpy as np


# initialise your particle
Ball = Particle(
    position=np.array([0, 100, 0]),
    velocity=np.array([20, 50, 0]),
    acceleration=np.array([0, -10, 0]),  # g=-10 m/s^2 in y-direction
    name="Ball",
    mass=500.
)
print(Ball)

time = 0  # initial time stamp
deltaT = 1e-3  # time steps of 1ms

times = []
y = [] 

# run simulation until ball hits the ground
while Ball.position[1] > 0.0:
    # store the time stamps
    times.append(time)

    # store the y-position
    y.append(Ball.position[1])

    # update the time
    time += deltaT

    # update the positions and velocities
    Ball.update(deltaT)


# print out some information
print(max(times))
print(max(y))
print(len(times))

# plot the data
plt.plot(times, y, 'r-', label='trajectory')
plt.xlabel('time (s)')
plt.ylabel('y-position (m)')
plt.legend()
plt.show()

