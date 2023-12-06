from Particle import Particle

import numpy
test1args = dict(
    position=numpy.array([0, 100, 0], dtype=float),
    velocity=numpy.array([0, 10, 0], dtype=float),
    acceleration=numpy.array([0, -10, 0], dtype=float),
    name="Ball",
    mass=500.0
)
Ball=Particle(**test1args)
print(Ball)
for i in range(5):
     Ball.update(0.1)
print(Ball)
