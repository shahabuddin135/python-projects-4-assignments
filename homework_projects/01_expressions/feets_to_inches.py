

def feet_to_inches(feet):
    inches = 12
    inches = feet * inches
    
    return inches


if __name__ == '__main__':
    feet = float(input("Enter Feet: "))
    result = feet_to_inches(feet)

    print(result)