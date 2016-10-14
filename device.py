import math
import random
from ray import Ray

# goal - a device should not require O(n) time to pop 
# could use stack - but generators open up possibilities of less memory

class Device:
    """represent a measuring device for the angles of the rays
    
    Considered using a stack, where the device pops off the next
    element each time, but ended up going with generators to
    avoid saving every single value, and running the risk of 
    being left with an empty stack. Generators seem to better 
    model the polling of the actual measuring device.
    """

    def __init__(
            self, init_angle=0.0, noise=0.0, speed=0.0, hz=1.0, 
            name="Default_Device"):
        """represent device with generator that yields angles"""
        self.generator = self.gen_device(init_angle, noise, speed) 
        self.name = name
        self.hz = hz
        self.time_step = 1 / hz
        self.local_time = 0.0
        # last_val is the last recorded angle (at time = local_time) 
        self.last_val = init_angle

    def global_poll(self, time):
        """give a global_time for seconds since device started
        
        If time is in the past (before local_time) just return last_val,
        that way the device doesn't need to have a full history of all
        measured values.

        Only poll the generator again if we need to.
        """
        while time >= self.local_time + self.time_step:
            # need new data - update time and last_val
            self.local_time += self.time_step
            self.last_val = self.generator.__next__() 
        return self.last_val 

    def simple_poll(self):
        """just return the next value, whatever that value is"""
        self.local_time += self.time_step
        return self.generator.__next__()

    def freeze_time_poll(self, time):
        """don't advance the current_time for testing only"""
        return self.generator.__next__()

    def __str__(self):
        return self.name + " | " + str(self.hz)

    def __repr__(self):
        return str(self)

    ###############################################################
    ############ various generators for device testing ############
    ###############################################################

    def perfect_device(angle):
        """always return this angle"""
        while True:
            yield angle

    def noisy_device(angle, noise):
        """center on angle, but add some randomness (with noise val)"""
        while True:
            # center random noise at 0
            yield angle + noise * (random.random() - 0.5)

    def rotating_device(init_angle, speed):
        """start at init_angle, and go speed (+/-) counterclockwise"""
        angle = init_angle 
        while True:
            # increment by speed, but wrap around after 360 degrees
            angle += speed
            angle = angle % (2 * math.pi)
            yield angle 

    def gen_device(self, init_angle=0, noise=0, speed=0):
        """general device - give init, randomness, turn speed (+/-)"""
        # to avoid multiple devs messing with each other
        self.angle = init_angle
        while True:
            self.angle += (speed + noise * (random.random() - 0.5))
            self.angle = self.angle % (2 * math.pi) 
            yield self.angle
