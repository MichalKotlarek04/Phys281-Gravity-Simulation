from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import copy
from Particle import Particle
import numpy as np

def print_particle(particle):
    print("Particle: {}".format(particle.name))
    print("  Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))

dataIn = np.load("SimulationData.npz", allow_pickle=True)
bodiesList = dataIn["x"][0]
conservationTrackingList = dataIn["y"]
dataIn = dataIn["x"][1:]

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
    print_particle(dataIn[0][counter])
    counter += 1
    # Creates the x,y and z position lists and plots them for each body.

ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
plt.legend()
plt.show()
# PLots, labels, and shows the position lists of each body.

cTL_t = [] # time
cTL_m = [] # momentum
cTL_e = [] # energy
for i in range(len(conservationTrackingList)):
    cTL_t.append(conservationTrackingList[i][0])
    cTL_m.append(conservationTrackingList[i][1])
    cTL_e.append(conservationTrackingList[i][2])


plt.plot(cTL_t, cTL_m, label="Momentum")
plt.xlabel("Time, s")
plt.ylabel("Momentum, kg m s^-1")
plt.legend()
plt.show()

plt.plot(cTL_t,cTL_e, label="Energy")
plt.xlabel("Time, s")
plt.ylabel("Energy, J")
plt.legend()
plt.show()
