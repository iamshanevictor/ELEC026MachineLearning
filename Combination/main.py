from Calculator import Calculator
from PrimeComposite import isPrime

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

def solve(num):
  primes = []
  composites = []
  
  for i in range(1, num + 1):
    if isPrime(i):
      primes.append(i)
    else:
      composites.append(i)
  
  print("All Prime: ", primes)
  print("All Composite: ", composites)

def main():
  select = int(input("Enter a Number [1 = Calculator | 2 = PrimeComposite | 3 = Exit]: "))

  def primecomposite():
    num = int(input("Enter a NUmber: "))

    solve(num)

  def calc():
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    z = int(input("Enter Operation: "))

    compute(a, b, z)
    
  def error():
    print("Select Numbers 1 and 2 ONLY!")
    main()

  if select == 1:
    calc()
  elif select == 2:
    primecomposite()
  elif select < 1 or select > 2:
    error()

main()

