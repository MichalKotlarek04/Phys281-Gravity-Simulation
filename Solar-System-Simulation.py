from Particle import Particle
from initialState import getBodyState
import astropy.constants as const
import copy
import numpy as np

# These variable can be edited at will by the user.
dT = 1800 # time interval for the simulation in seconds.
simulation_time = 10 # time the system is being simulated, in years
solarBodies = [["sun",const.M_sun.value],
                ["earth",const.M_earth.value],
                ["mercury",3.302e23],
                ["venus",48.685e23],
                ["mars",6.4171e23]]
                # The planetary masses I have used here, unless imported from the astropy package, were obtained from JPL ephemeris tables
                # Further bodies can be added as elements in this list, for example ["jupiter", const.M_jup.value]

extraBodies = [] # Any bodies that won't have astropy ephemerides can be manually defined in this list, using the Particle class:
                 # additionalBody = Particle(name="Body Name", mass=bodyMass, position=[x,y,z], velocity = [vx,vy,vz])


# It is recommended that these variables are not edited by the user.
timePassed = 0 # variable to keep track of how much time has passed in the simulation
data = [] # empty list; deep copies of all bodies will be added to this.
iterations = int(simulation_time*3600*24*365/dT) # how many times the simulation is to be iterated
KE = 0 # Variable to keep track of the total kinetic energy in the simulation
PE = 0 # Likewise for potential energy. KE+PE should remain constant if conservation laws are being followed.
momentum = [0,0,0] # likewise for total momentum, albeit with a vector quantity
bodiesList = [] # All the bodies (defined by Particle class) will be kept in this list
conservationTrackingList = [] # list to keep track of total energy and momentum at each 100th iteration


for bodyName in solarBodies:
    posvel = getBodyState(bodyName[0]).initialState
    pos, vel = posvel[0], posvel[1]
    newBody = Particle(position=pos,velocity=vel,name=bodyName[0],mass=bodyName[1])
    bodiesList.append(newBody)

data.append(bodiesList)

for i in range(iterations):
    for body in bodiesList:
        body.updatePosition(dT)

    for body in bodiesList:
        body.resetGravitationalAcceleration()
        excludedBodyList = bodiesList.copy()
        excludedBodyList.remove(body)
        for otherBody in excludedBodyList:
            body.updateGravitationalAcceleration(otherBody)
        body.updateVelocity(dT)
    # Updates the gravitational acceleration, position, and velocity on each body
    # excludedBodyList is necessary because each body is acted on by all other bodies in the simulation
    # Position is updated first, because it directly impacts the gravitational force, so it should not be updated body-by-body with the others.

    timePassed += dT
    if i % 100 == 0: # every 100 iterations:
        dataAppendList = []
        print("Time Passed: {}s/{:5f}d/{:5f}y".format(timePassed,timePassed/86400,timePassed/3.1536e7))
        for body in bodiesList:
            KE += body.kineticEnergy() # adds each body's kinetic energy to the total KE of the simulation.
            momentum += body.momentum() # adds each body's momentum to the total momentum of the simulation to check for conservation of momentum.
            dataAppendList.append(copy.deepcopy(body)) # adds each body as a deep copy to the list that will later be appended to the saved file.

            excludedBodyList = bodiesList.copy()
            excludedBodyList.remove(body)
            for otherBody in excludedBodyList:
                PE += body.potentialEnergy(otherBody)

        data.append(dataAppendList)

        print("Total energy of the simulation (KE+PE): {:7e}".format(KE+PE))
        print("Magnitude of total momentum: {}\n".format(np.linalg.norm(momentum)))
        # Displays the quantities that should be conserved, in an easy-to-read format.

        conservationTrackingList.append([timePassed, np.linalg.norm(momentum), (KE+PE)])

        KE = 0
        PE = 0
        momentum = [0,0,0]
        # resets the quantities that are calculated freshly each time.

np.savez("SimulationData", x=data,y=conservationTrackingList, allow_pickle=True)

