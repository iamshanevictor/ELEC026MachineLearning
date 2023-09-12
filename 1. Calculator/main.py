from Calculator import Calculator

def compute(a, b, z):
    if z == 1:
        print("The Sum is: ", Calculator.add(a, b))
    elif z == 2:
        print("The ___ is: ", Calculator.subtract(a, b))
    elif z == 3:
        print("The _____ is: ", Calculator.multiply(a, b))
    elif z == 4:
        print("The ____ is: ", Calculator.divide(a, b))
    elif z<4 or z>1:
        print("Invalid")

def main():
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    z = int(input("Enter Operation: "))

    compute(a, b, z)

main()