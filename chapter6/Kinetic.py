def main():
    mass = float(raw_input("Enter the object's mass: "))
    velocity = float(raw_input("Enter the object's velocity: "))
    print "The Kinetic Energy is", kinetic_energy(mass, velocity)
def kinetic_energy(mass, velocity):
    KE = 1.0/2 * mass * velocity**2
    return KE
main()