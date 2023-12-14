import numpy as np

class Particle:

    G = 6.67408E-11 # Gravitational constant

    def __init__(self,
    position=np.array([0, 0, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, 0, 0], dtype=float),
    name='Ball',mass=1.0):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.a_n = None
        self.a_prev = None

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
        self.name, self.mass,self.position, self.velocity, self.acceleration)

    def updatePosition(self, deltaT):
        if type(self.a_n) == type(None):
            self.position += self.velocity * deltaT
        else:
            self.position += self.velocity * deltaT + 1/6 * ((4*self.acceleration-self.a_n) * (deltaT**2))
            self.a_prev = self.a_n
        self.a_n = self.acceleration

    def updateVelocity(self, deltaT):
        if type(self.a_prev) == type(None):
            if type(self.a_n) == type(None):
                self.velocity += self.acceleration * deltaT
            else:
                self.velocity += 1/2 * (self.acceleration + self.a_n)*deltaT
        else:
            self.velocity += 1/6 * (2*self.acceleration+5*self.a_n-self.a_prev)*deltaT

        # Implementation of Beeman algorithm means the update procedure must be as such:
        # update position
        # update acceleration
        # update velocity

    def resetGravitationalAcceleration(self):
        self.acceleration = np.array([0,0,0], dtype=float)

    def updateGravitationalAcceleration(self, body):
        r = np.linalg.norm(body.position-self.position) # finds distance between 2 bodies
        direction_vector = (body.position-self.position)/r # unit vector for the direction of the acceleration
        force_mag = Particle.G * body.mass * self.mass / r**2 # Magnitude of the gravitational force

        self.acceleration += (force_mag/self.mass)*direction_vector

    def kineticEnergy(self):
        velocity_squared = np.linalg.norm(self.velocity)**2
        K = 1/2 * self.mass * velocity_squared
        return K

    def momentum(self):
        momentum = self.mass * self.velocity
        return momentum
        # calculates the linear momentum vector of the particle

    def potentialEnergy(self, particle):
        r = np.linalg.norm(particle.position-self.position) # distance between this particle and the other particle
        GPE = Particle.G * self.mass * particle.mass/r # formula for gravitational potential energy

        return GPE

