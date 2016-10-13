from ray import Ray
from device import Device
import utils 


# build a bunch of Rays - based on the device
# for now - have one ray at (0, 0) with 0 ish degrees, with one spinning one
# printout when intersect

noisy_zero = Device(Device.gen_device(0, 10, 0), "noisy_zero", 0.5)
rotating_zero = Device(Device.gen_device(0, 10, 10), "rotating_zero", 0.5)

for i in range(100):
    ray_a = Ray((0, 0), noisy_zero.simple_poll())
    ray_b = Ray((-1, -1), rotating_zero.simple_poll())
    i = utils.find_intersection(ray_a, ray_b)
    if i:
        print (ray_a, ray_b, i)

# next steps - user input, menu, other generators etc

import pdb; pdb.set_trace()

