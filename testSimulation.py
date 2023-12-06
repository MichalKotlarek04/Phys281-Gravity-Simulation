from Simulation import *
from os import path

def print_particle(particle):
    print("Particle: {}".format(particle.name))
    print("  Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("  {}: {}".format(attribute, particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


print("The Earth and Satellites Location after {0} seconds is:".format((2000*6)))
print_particle(Earth)
print_particle(Satellite)
if path.exists("TwoBodyTest.npy"):
    print("The file TwoBodyTest.npy has been created.")

print("testing reading it back in")
DataIn = np.load("TwoBodyTest.npy", allow_pickle=True)

print("Printing First Entry")
print("{}".format(int(DataIn[0][0])))  #time
print_particle(DataIn[0][1])  # Earth
print_particle(DataIn[0][2])  # Satellite

print("Printing Fifth Entry")
print("{}".format(int(DataIn[4][0])))  #time
print_particle(DataIn[4][1])  # Earth
print_particle(DataIn[4][2])  # Satellite

print("Printing Last Entry")
print("{}".format(int(DataIn[-1][0])))  #time
print_particle(DataIn[-1][1])  # Earth
print_particle(DataIn[-1][2])  # Satellite
