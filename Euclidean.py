import math

number_one = float(input("enter number 1: "))
number_two = float(input("enter number 2: "))
quotient = 0
remainder = 9999

while remainder > 0:
    quotient_calc = number_one/number_two
    quotient = math.floor(quotient_calc)

    remainder = number_one - (quotient*number_two)

    if remainder > 0:
        print(f"The remainder is: {remainder}")
        number_one = number_two
        number_two = remainder


    else:
        print(f"The GCD is: {number_two}")
        break
    






