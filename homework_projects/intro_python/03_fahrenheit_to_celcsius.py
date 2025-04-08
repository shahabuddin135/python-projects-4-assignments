temp_input = float(input("enter temperature in fahrenheit"))
def f_to_c(f):
    return (f-32)*5.0/9.0
print(f"{f_to_c(temp_input):.2f}")