
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
show_type = input("Enter the show type (Matinee/Evening): ").capitalize()
if age < 12:
    if show_type == 'Matinee':
        print("Ticket = Rs500")
    elif show_type == 'Evening':
        print("Ticket = Rs700")
    else:
        print("Invalid show type. Please enter 'Matinee' or 'Evening'.")
elif 12 <= age < 60:
    if gender == 'M':
        if show_type == 'Matinee':
            print("Ticket = Rs800")
        elif show_type == 'Evening':
            print("Ticket = Rs100")
        else:
            print("Invalid show type. Please enter 'Matinee' or 'Evening'.")
    elif gender == 'F':
        
        if show_type == 'Matinee':
            print("Ticket = Rs700")
        elif show_type == 'Evening':
            print("Ticket = Rs900")
        else:
            print("Invalid show type. Please enter 'Matinee' or 'Evening'.")
    else:
         print("Invalid input.")
 
