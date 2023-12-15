# Phys281-Gravity-Simulation
DEPENDENCIES: The project requires the following python packages: matplotlib, numpy, astropy, spiceypy, poliastro, copy

TO RUN THE SIMULATION: run the Solar-System-Simulation.py file to generate the SimulationResults.npy file. To view the results of the simulation, run the drawSimulation.py file.

What each file does:
Particle.py - contains the Particle class which provides the code necessary to simulate a body (assumed pointlike) of arbitrary mass, velocity, and position.
initialState.py - contains the getBodyState class, which uses the astropy package to generate ephemerides for solar system objects.
Solar-System-Simulation.py - contains the code to simulate an N-body gravitational system. By default, it contains the sun and the inner planets.
drawSimulation.py - reads the SimulationResults.npy file, and displays the results of the simulation in a 3-dimensional pyplot.

particle_testing.py - a unit test used early on to make sure the Particle class is working as expected.
testInitialState.py - a unit test of the initialState.py file, the results of this test were compared against ephemeris obtained manually from the JPL Horizons page at https://ssd.jpl.nasa.gov/horizons.cgi
testKE.py - tests both the KineticEnergy() method from the Particle class and the ability to read a previously generated .npy file
testParticle.py - another test of the Particle class, simulating a basic scenario of a ball under constant acceleration.
