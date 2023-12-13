from Particle import Particle
from initialState import getBodyState
import astropy.constants as const
import copy
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

def print_particle(particle):
    print("Particle: {}".format(particle.name))
    print("  Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))


dT = 300 # time interval for the simulation in seconds
simulation_time = 10 # time the simulation is being simulated, in years
timePassed = 0 # variable to keep track of how much time has passed in the simulation
data = [] # empty list; deep copies of all bodies will be added to this.
iterations = int(simulation_time*3600*24*365/dT) # how many times the simulation is to be iterated
KE = 0 # VAriable to keep track of the total kinetic energy in a simulation
bodyNamesList = [["sun",const.M_sun.value],
                ["earth",const.M_earth.value],
                ["mercury",3.302e23],
                ["venus",48.685e23],
                ["jupiter",const.M_jup.value]]
# Planetary masses from JPL ephemerides

bodiesList = []
for bodyName in bodyNamesList:
    posvel = getBodyState(bodyName[0]).initialState
    pos, vel = posvel[0], posvel[1]
    newBody = Particle(position=pos,velocity=vel,name=bodyName[0],mass=bodyName[1])
    bodiesList.append(newBody)
for i in range(iterations):
    for body in bodiesList:
        body.resetGravitationalAcceleration()
        excludedBodyList = bodiesList.copy()
        excludedBodyList.remove(body)
        for otherBody in excludedBodyList:
            body.updateGravitationalAcceleration(otherBody)
    # Updates the gravitational acceleration on each body

    for body in bodiesList:
        body.update(dT)

    timePassed += dT
    if i % 100 == 0:
        #dataAppendList = [timePassed]
        dataAppendList = []
        print("Time Passed: {}s/{:5f}d/{:5f}y".format(timePassed,timePassed/86400,timePassed/3.1536e7))
        for body in bodiesList:
            KE += body.kineticEnergy()
            dataAppendList.append(copy.deepcopy(body))
        data.append(dataAppendList)
        print("Total kinetic energy of the simulation: {:7e}\n".format(KE))
        KE = 0

#'''

np.save("SimulationData", data, allow_pickle=True)

dataIn = np.load("SimulationData.npy", allow_pickle=True)
print_particle(dataIn[0][0])
print_particle(dataIn[0][1])
print_particle(dataIn[0][2])
print_particle(dataIn[-1][0])
print_particle(dataIn[-1][1])
print_particle(dataIn[-1][2])

fig = plt.figure()
ax = plt.axes(projection ='3d')
counter = 0
for body in bodiesList:
    bodyPosxList = []
    bodyPosyList = []
    bodyPoszList = []
    for i in range(len(dataIn)):
        bodyPosxList.append(dataIn[i][counter].position[0])
        bodyPosyList.append(dataIn[i][counter].position[1])
        bodyPoszList.append(dataIn[i][counter].position[2])
    ax.plot3D(bodyPosxList, bodyPosyList, bodyPoszList, label=dataIn[0][counter].name)
    counter += 1

#ax = plt.axes(projection='3d')
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
plt.legend()
plt.show()
