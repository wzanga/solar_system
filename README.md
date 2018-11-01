# Solar System Demo

Overview
============
This project is a special case of the gravitational nbody problem applied to the solar system

Basic Usage
===========
The principal class used for the simulation is 'nbp' which stands for "N-body problem" 

1.It is initialized with the name of the bodies we would like to simulate:
For exemple ['SUN','MERCURY','VENUS','EARTH','MARS',............,'PLUTO']

2.The initial conditions for each body must be given
By default, you should use the orbital velocities of the body w.r.t the Sun
These orbital velocities are attributes of the << body class >> (see body.py)

That's it!
