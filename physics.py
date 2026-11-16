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
    while True:
    print("\nPhysics Calculator")
    print("1. Speed")
    print("2. Density")
    print("3. Force")
    print("4. Work done")
    print("5. Power")

    choice = input("Choose an operation (1-5): ")

    if choice == "1":
        distance = float(input("Distance: "))
        time = float(input("Time: "))
        print("Speed =", calculate_speed(distance, time))
    elif choice == "2":
        mass = float(input("Mass: "))
        volume = float(input("Volume: "))
        print("Density =", calculate_density(mass, volume))
    elif choice == "3":
        mass = float(input("Mass: "))
        acceleration = float(input("Acceleration: "))
        print("Force =", calculate_force(mass, acceleration))
    elif choice == "4":
        force = float(input("Force: "))
        distance = float(input("Distance: "))
        print("Work done =", calculate_workdone(force, distance))
    elif choice == "5":
        force = float(input("Force: "))
        velocity = float(input("Velocity: "))
        print("Power =", calculate_power(force, velocity))
    else:
        print("Invalid choice")

    again = input("Do you want to continue? (yes/no): ")
    if again.lower() == "no":
        print("Goodbye!")
        break
