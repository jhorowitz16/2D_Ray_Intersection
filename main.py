from ray import Ray
from device import Device
import utils 
import argparse


def build_device(init_angle, noise, speed, freq, name):
    """based on user's input, initialize a device object"""
    return Device(init_angle, noise, speed, freq, name)


def run(count, device_a, a_x, a_y, device_b, b_x, b_y, monitor_freq):
    """given the setup parameters - run trials (print outs for now)"""
    print(("\nFirst Ray, Degree    ||| Second Ray, Degree   |||" + 
           " Intersection Points"))
    origin_a = (a_x, a_y)
    origin_b = (b_x, b_y)
    c, time = 0, 0
    monitor_time_step = 1 / monitor_freq
    while c < count:
        ray_a = Ray(origin_a, device_a.global_poll(time))
        ray_b = Ray(origin_b, device_b.global_poll(time))
        inter = utils.find_intersection(ray_a, ray_b)
        print (ray_a, "|||", ray_b, "|||", inter)
        time += monitor_time_step
        c += 1


if __name__=="__main__":

    # parse the command line arguments with argparse
    parser = argparse.ArgumentParser()
    p = parser
    p.aa = parser.add_argument

    # device_a content
    p.aa("device_a", help="name of first device")
    p.aa("device_a_x", help="x coordinate of first device", type=float)
    p.aa("device_a_y", help="y coordinate of first device", type=float)
    p.aa("device_a_angle", help="initial angle of first device", type=float)
    p.aa("device_a_noise", help="noise constant of first device", type=float)
    p.aa("device_a_speed", help="turn speed of first device", type=float)
    p.aa("device_a_freq", help="poll frequency of first device", type=float)

    # device_b content
    p.aa("device_b", help="name of second device")
    p.aa("device_b_x", help="x coordinate of second device", type=float)
    p.aa("device_b_y", help="y coordinate of second device", type=float)
    p.aa("device_b_angle", help="initial angle of second device", type=float)
    p.aa("device_b_noise", help="noise constant of second device", type=float)
    p.aa("device_b_speed", help="turn speed of second device", type=float)
    p.aa("device_b_freq", help="poll frequency of second device", type=float)

    # experiment content
    p.aa("monitor_freq", help="monitor frequency in hz", type=float)
    p.aa("time_steps", help="number of times monitor captures", type=float)

    # based on the input - construct the two devices
    args = parser.parse_args()
    Device_A = build_device(args.device_a_angle, args.device_a_noise, 
            args.device_a_speed, args.device_a_freq, args.device_a)
    Device_B = build_device(args.device_b_angle, args.device_b_noise, 
            args.device_b_speed, args.device_b_freq, args.device_b)
    
    # run experiment at the monitor frequency (ex: 40 time steps)
    run(args.time_steps, Device_A, args.device_a_x, args.device_a_y, 
            Device_B, args.device_b_x, args.device_b_y, args.monitor_freq)

