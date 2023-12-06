import numpy as np

class Particle:

    G = 6.67408E-11 # Gravitational constant

    def __init__(self,
    position=np.array([0, 0, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, -10, 0], dtype=float),
    name='Ball',mass=1.0):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
        self.name, self.mass,self.position, self.velocity, self.acceleration)

    def update(self, deltaT):
        self.position += self.velocity*deltaT
        self.velocity += self.acceleration*deltaT

    def updateGravitationalAcceleration(self, body):
        r = np.linalg.norm(body.position-self.position) # finds distance between 2 bodies
        direction_vector = (body.position-self.position)/r # unit vector for the direction of the acceleration
        force_mag = Particle.G * body.mass * self.mass / r**2 # Magnitude of the gravitational force

        self.acceleration = (force_mag/self.mass)*direction_vector

    def kineticEnergy(self):
        velocity_squared = np.linalg.norm(self.velocity)**2
        K = 1/2 * self.mass * velocity_squared
        return K
