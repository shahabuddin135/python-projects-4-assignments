
def years_to_seconds():
    years = int(input("enter number of Years: "))
    years = years * 365
    return 60 * 60 * 24 * years

result = years_to_seconds()

print(f"Seconds in a year: {result}")