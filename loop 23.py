
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
experience = int(input("Enter your experience (in years): "))
if 21 <= age <= 35:
    if gender == 'M':
        if experience >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == 'F':
        if experience >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
    else:
        print("Invalid gender input. Please enter 'M' or 'F'.")
elif age > 35:
    print("Manager Role")
else:
    print("You are not eligible for a role based on age.")
