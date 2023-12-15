from Particle import Particle
from initialState import getBodyState
import copy
import numpy as np

# These variable can be edited at will by the user.



class Simulation:
    def __init__(self, inputBodies=[], deltaT=360):
        self.data = []
        self.dT = deltaT
        self.bodiesList = [] # All the bodies will be kept in this list
        self.timePassed = 0
        self.conservationTrackingList = [] # list to keep track of total energy and momentum at each 100th iteration

        if len(inputBodies)>0:
            for bodyName in inputBodies:
                if type(bodyName)==type(Particle()):
                    self.bodiesList.append(bodyName)
                else:
                    try:
                        posvel = getBodyState(bodyName[0]).initialState
                        pos, vel = posvel[0], posvel[1]
                        newBody = Particle(position=pos,velocity=vel,name=bodyName[0],mass=bodyName[1])
                        self.bodiesList.append(newBody)
                    except:
                        raise Exception("Unable to generate ephemeris for {}, try defining it manually".format(bodyName[0]))
        else:
            raise ValueError("List of bodies was empty - have you entered the correct list as inputBodies?")
        self.data.append(self.bodiesList)
        # Takes the user-defined bodies into the list of bodies being simulated as well as ephemerides for solar bodies if present
    def __str__(self):
        return("Time passed:{0}, Time interval dT: {1}, Number of bodies: {2}".format(self.timePassed,self.dT,len(self.bodiesList)))

    def iterate(self, silent=False):
        for body in self.bodiesList:
            body.updatePosition(self.dT)

        for body in self.bodiesList:
            body.resetGravitationalAcceleration()
            excludedBodyList = self.bodiesList.copy()
            excludedBodyList.remove(body)
            for otherBody in excludedBodyList:
                body.updateGravitationalAcceleration(otherBody)
            body.updateVelocity(self.dT)
        # Updates the gravitational acceleration, position, and velocity on each body
        # excludedBodyList is necessary because each body is acted on by all other bodies in the simulation
        # Position is updated first, because it directly impacts the gravitational force, so it should not be updated body-by-body with the others.

        self.timePassed += self.dT
        if self.timePassed/self.dT % 100 == 0: # every 100 iterations:
            KE = 0 # Variable to keep track of the total kinetic energy in the simulation
            PE = 0 # Likewise for potential energy. KE+PE should remain constant if conservation laws are being followed.
            momentum = [0,0,0] # likewise for total momentum, albeit with a vector quantity
            dataAppendList = []
            # resets the quantities that are calculated freshly each time.

            for body in self.bodiesList:
                KE += body.kineticEnergy() # adds each body's kinetic energy to the total KE of the simulation.
                momentum += body.momentum() # adds each body's momentum to the total momentum of the simulation to check for conservation of momentum.
                dataAppendList.append(copy.deepcopy(body)) # adds each body as a deep copy to the list that will later be appended to the saved file.

                excludedBodyList = self.bodiesList.copy()
                excludedBodyList.remove(body)
                for otherBody in excludedBodyList:
                    PE += body.potentialEnergy(otherBody)

                self.data.append(dataAppendList)
            if silent == False:
                print("Time Passed: {}s/{:5f}d/{:5f}y".format(self.timePassed,self.timePassed/86400,self.timePassed/3.1536e7))
                print("Total energy of the simulation (KE+PE): {:7e}".format(KE+PE))
                print("Magnitude of total momentum: {}\n".format(np.linalg.norm(momentum)))
                # Displays the quantities that should be conserved, in an easy-to-read format.

            self.conservationTrackingList.append([self.timePassed, np.linalg.norm(momentum), (KE+PE)])

    def saveSimulation(self, outputfile="SimulationData"):
        np.savez(outputfile, x=self.data,y=self.conservationTrackingList, allow_pickle=True)
