#
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
income = float(input("Enter your income: "))
if 18 <= age < 60:
    if gender == 'M':
        
        if income > 1000000:
            tax = income * 0.30
            print(f"Tax = Rs{tax:.2f}")
        elif 500000 < income <= 1000000:
            tax = income * 0.20
            print(f"Tax = Rs{tax:.2f}")
        elif income <= 500000:
            tax = income * 0.10
            print(f"Tax = Rs{tax:.2f}")
        else:
            print("Invalid income input.")
    elif gender == 'F':
        if income > 1000000:
            tax = income * 0.25
            print(f"Tax = Rs{tax:.2f}")
        elif 500000 < income <= 1000000:
            tax = income * 0.15
            print(f"Tax = Rs{tax:.2f}")
        elif income <= 500000:
            tax = income * 0.05
            print(f"Tax = Rs{tax:.2f}")
        else:
            print("Invalid income input.")
    else:
        print("Invalid gender input. Please enter 'M' or 'F'.")
elif age >= 60:
    if income > 1000000:
        tax = income * 0.20
        print(f"Tax = Rs{tax:.2f}")
    elif income <= 1000000:
        tax = income * 0.10
        print(f"Tax = Rs{tax:.2f}")
    else:
        print("Invalid income input.")
else:
    print("You are not eligible for tax calculation based on age.")
