import math

base_number = 0
argument_number = 0
natural_or_log = 0
loop = 9999

while loop > 0:
    argument_number = float(input("Enter the argument number: "))
    natural_or_log = float(input("Enter 1 for Natural, 2 to enter a Base: "))

    if natural_or_log == 1:
        base_number = 2.71828
        calculated_number = math.log(argument_number, base_number)
        print(f"The result is: {calculated_number}")

        rerun_prompt = float(input("Would you like to rerun? 1 for yes, 2 for no: "))
        if rerun_prompt == 2:
            break

    elif natural_or_log == 2:
        base_number = float(input("Enter the base number: "))
        calculated_number = math.log(argument_number, base_number)
        print(f"The result is: {calculated_number}")

        rerun_prompt = float(input("Would you like to rerun? 1 for yes, 2 for no: "))
        if rerun_prompt == 2:
            break

    else:
        print("Unkown entry, restarting...")
                                 