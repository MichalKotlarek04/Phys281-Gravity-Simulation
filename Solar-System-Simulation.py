from Simulation import Simulation
from Particle import Particle # This import is technically optional, it is only needed if you are defining an additional body in the extraBodies list
import astropy.constants as const

dT = 1 # time interval for the simulation in seconds.
simulation_time = 1 # time the system is being simulated, in years
solarBodies = [["sun",const.M_sun.value],
                ["earth",const.M_earth.value],
                ["mercury",3.302e23],
                ["venus",48.685e23],
                ["mars",6.4171e23]]
                # The planetary masses I have used here, unless imported from the astropy package, were obtained from JPL ephemeris tables
                # Further bodies can be added as elements in this list, for example ["jupiter", const.M_jup.value]
                # Any bodies that won't have astropy ephemerides can be manually defined in this list, using the Particle class:
                 # additionalBody = Particle(name="Body Name", mass=bodyMass, position=[x,y,z], velocity = [vx,vy,vz])

iterations = int(simulation_time*3600*24*365/dT) # how many times the simulation is to be iterated

solarSystem = Simulation(solarBodies, deltaT=dT)
print(solarSystem.__str__())
for i in range(iterations):
    solarSystem.iterate()
solarSystem.saveSimulation()
