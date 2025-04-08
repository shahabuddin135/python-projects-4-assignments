
def find_perimeter():
    side_one = float(input("Enter the length of 1st side of Triangle: "))
    side_two = float(input("Enter the length of 2nd side of Triangle: "))
    side_three = float(input("Enter the length of 3rd side of Triangle: "))
    
    return side_one + side_two + side_three


if __name__ == '__main__':
    
    print(f"Triangle perimeter is: {find_perimeter()}")