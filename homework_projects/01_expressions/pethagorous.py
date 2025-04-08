import math

def find_hypotenuse():
    
    ab = float(input("Enter the length for A_B (cm): "))
    ac = float(input("Enter the length for A_C (cm): "))
    
    hypotenuse = math.sqrt( ab**2 + ac*ac)
    
    return hypotenuse

if __name__ == '__main__':
   result = find_hypotenuse()
   print(f"{result:.2f}")