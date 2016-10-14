from ray import Ray
from device import Device
import utils 


def build_device():
    """based on user's input, initialize a device object"""

    # get the user's input
    device_name = input("Enter the name of the device: ")

    # try to parse immediately so the user can try again
    origin_str = input(("Enter " + device_name + 
                        "'s location (ex: (1, 2)): "))
    origin = parse_origin_str(origin_str)

    init_angle = input(("Enter " + device_name + 
                        "'s initial angle in radians (ex: 0.0): "))
    noise = input(("Enter " + device_name + 
                   "'s noise constant (ex: 0.5): "))
    speed = input(("Enter " + device_name + 
                   "'s rotational speed (ex: 2.0): "))
    hz = input(("Enter " + device_name + 
                "'s frequency in hz (ex: 60.0): "))

    Device_A = Device(float(init_angle), float(noise), float(speed), 
            float(hz), device_name)
    return (origin_str, Device_A)


def parse_origin_str(origin_str):
    """take a string like "(1, 2)" and return 1 and 2 as a tuple"""
    origin_str = origin_str[1:len(origin_str)-1]
    for i in range(len(origin_str)):
        if origin_str[i] == ",":
            return (float(origin_str[:i]), float(origin_str[(i+1):]))
    # if there was no comma, something bad happened
    raise NameError('Could not parse device location')


def gather_info():    
    """ask the user for the information on the setup"""

    print("\nEnter information for the first device")
    origin_str_a, device_a = build_device()
    origin_a = parse_origin_str(origin_str_a)

    print("\nEnter information for the second device")
    origin_str_b, device_b = build_device()
    origin_b = parse_origin_str(origin_str_b)

    monitor_str = input("\nEnter monitor's frequency in hz (ex: 75.0): ")
    monitor_freq = float(monitor_str)

    return (origin_a, device_a, origin_b, device_b, monitor_freq)


def run(count, origin_a, device_a, origin_b, device_b, monitor_freq):
    """given the setup parameters - run trials (print outs for now)"""
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
    params = gather_info() 
    print(("\nFirst Ray, Degree    ||| Second Ray, Degree   |||" + 
           " Intersection Points"))
    run(40, params[0], params[1], params[2], params[3], params[4])
