# COS 101 assignment
def calculate_speed(distance, time):
    """1.  Speed = Distance / time """
    if time == 0:
         return "Time Cannot be zero"
    return distance / time

def calculate_density(mass, volume):
    """2.  density = mass / volume """
    if volume == 0:
         return "volume Cannot be zero"
    return mass / volume

def calculate_force(mass, acceleration):
    """3.  force= mass * acceleration """
    
    return mass * acceleration

def calculate_workdone(force, distance):
    """4.  workdone = force * distance """
    
    return force * distance

def calculate_power(force, velocity):
    """5.  power= force * velocity """
    
    return force * velocity