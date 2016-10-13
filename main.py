from ray import Ray
from device import Device
import utils 


# build a bunch of Rays - based on the device
# for now - have one ray at (0, 0) with 0 ish degrees, with one spinning one
# printout when intersect


# devices for testing
perfect_zero = Device(Device.gen_device(0, 0, 0), "perfect_zero", 0.5)
noisy_zero = Device(Device.gen_device(0, 0.1, 0), "noisy_zero", 0.5)
rotating_zero = Device(Device.gen_device(0, 0, 0.1), "rotating_zero", 0.5)

def intersection_test_one():
    """ray_a at 0 with some noise, ray_b rotating"""
    count = 0
    for i in range(100):
        ray_a = Ray((0, 0), noisy_zero.simple_poll())
        ray_b = Ray((-1, -1), rotating_zero.simple_poll())
        i = utils.find_intersection(ray_a, ray_b)
        if i:
            print (ray_a, "|||", ray_b, "|||", i)
            count += 1
    import pdb; pdb.set_trace()

# next steps - user input, menu, other generators etc

intersection_test_one()

