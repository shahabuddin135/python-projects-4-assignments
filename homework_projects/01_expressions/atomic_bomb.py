

def boom(m):
    c = 299792458
    e = m* (c**2)
    return e
    
mass = float(input("Enter the mass (kg): "))
energy = boom(mass)

print(f"Energy released: {energy}J")

if __name__ == '__main__':
   energy = boom(mass)

print(f"Energy released: {energy}J")