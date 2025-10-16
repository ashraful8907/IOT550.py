from math import log

def compound_interest_calculator(savings:float, interest:float, years:float ) -> float:


    interest_rate = (interest / 100) + 1

    years_to_double = log(2)/log(interest_rate)


    year = 0
    for i in range(years):
        savings = savings * interest_rate
        year += 1
        print (f"Savings after year {year}: {round(savings,2)} ")
        
    print(f"It will take {years_to_double} years to double your money.")
    return

savings = float(input("what is the total savings you have?: "))
interest = float(input("What is the interest rate as a percentage?: "))
years = int(input("How many years are you holding?: "))

compound_interest_calculator(savings, interest, years)