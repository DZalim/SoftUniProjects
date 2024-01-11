def calculate_simple_interest(amount, rate, term):
    simple_interest = float(amount) * float(rate) * float(term)
    return f"Simple Interest: ${simple_interest:.2f}"


def calculate_compound_interest(amount, rate, term, times):
    compound_interest = float(amount) * (1 + (float(rate)/float(times))) ** (float(term)*float(times)) - float(amount)
    return f"Compound Interest: ${compound_interest:.2f}"


def calculate_loan_payment(amount, rate, term):
    monthly_interest = (float(rate)/12)
    monthly_payment = float(amount) * (monthly_interest/(1-(1/(1+monthly_interest)**float(term))))
    return f"Monthly payment: ${monthly_payment:.2f}"


def calculate_future_value_of_savings(amount, rate, term):
    future_value_simple_interest = float(amount) * (1 + (float(rate) * float(term)))
    future_value_compound_interest = float(amount) * (1 + float(rate)) ** float(term)
    return f"Future Value Using Simple Annual Interest: ${future_value_simple_interest:.2f}\n\
Future Value Using Compounded Annual Interest: ${future_value_compound_interest:.2f}"


def main_menu(action):
    if action == "1":
        print("Calculate Simple Interest")
        principal_amount = input("Enter principal amount: ")
        annual_interest_rate = input("Enter annual interest rate (as a decimal): ")
        time = input("Enter time (in years): ")
        return calculate_simple_interest(principal_amount, annual_interest_rate, time)
    elif action == "2":
        print("Calculate Compound Interest")
        principal_amount = input("Enter principal amount: ")
        annual_interest_rate = input("Enter annual interest rate (as a decimal): ")
        time = input("Enter time (in years): ")
        number_of_times = input("Enter the number of times interest is compounded per year: ")
        return calculate_compound_interest(principal_amount, annual_interest_rate, time, number_of_times)
    elif action == "3":
        print("Calculate Loan Payment")
        principal_amount = input("Enter principal amount: ")
        annual_interest_rate = input("Enter annual interest rate (as a decimal): ")
        time = input("Enter time (in years): ")
        return calculate_loan_payment(principal_amount, annual_interest_rate, time)
    elif action == "4":
        print("Calculate Future Value of Savings")
        investment_amount = input("Enter investment amount: ")
        annual_interest_rate = input("Enter annual interest rate (as a decimal): ")
        time = input("Enter time (in years): ")
        return calculate_future_value_of_savings(investment_amount, annual_interest_rate, time)
    elif action == "5":
        return "Goodbye!"


while True:
    print("Main Menu:")
    print(" 1. Calculate Simple Interest")
    print(" 2. Calculate Compound Interest")
    print(" 3. Calculate Loan Payment")
    print(" 4. Calculate Future Value of Savings")
    print(" 5. Quit")
    choice_input = input("Enter your choice (1/2/3/4/5): ")
    if choice_input == "5":
        break
    result = main_menu(choice_input)
    print(result)
    continue_input = input("Do you want to perform another calculation? (yes/no): ")
    if continue_input == "no":
        print("Goodbye!")
        break
    elif continue_input == "yes":
        continue
    else:
        print("Invalid input! Try again!")
