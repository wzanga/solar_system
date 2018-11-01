# Solar System Demo

Overview
============
This project is a special case of the gravitational nbody problem applied to the solar system

Basic Usage
===========
The principal class used for the simulation is 'nbp' which stands for "N-body problem" 

1. It is initialized with the name of the bodies we would like to simulate
For exemple nbp = nbp(['SUN','MERCURY','VENUS','EARTH','MARS']) initialize the n-body problem with the sun, Mercury, Venus, the Earth and Mars

2. Each body must be given an initial state
Advice : You may want to use the orbital velocities of the body w.r.t the Sun
These orbital velocities are attributes of the class 'body' (see body.py)

That's it!
