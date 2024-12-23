#
meal_type = input("Do you want vegetarian or non-vegetarian food? (Enter 'vegetarian' or 'non-vegetarian'): ").lower()

if meal_type == 'vegetarian':
    vegetarian_choice = input("Do you want Salad or Pasta? (Enter 'Salad' or 'Pasta'): ").lower()
    if vegetarian_choice == 'salad':
        print("You have chosen Salad.")
    elif vegetarian_choice == 'pasta':
        print("You have chosen Pasta.")
    else:
        print("Invalid choice! Please choose either 'Salad' or 'Pasta'.")
elif meal_type == 'non-vegetarian':
    non_vegetarian_choice = input("Do you want Chicken or Fish? (Enter 'Chicken' or 'Fish'): ").lower()
    if non_vegetarian_choice == 'chicken':
        print("You have chosen Chicken.")
    elif non_vegetarian_choice == 'fish':
        print("You have chosen Fish.")
    else:
        print("Invalid choice! Please choose either 'Chicken' or 'Fish'.")
else:
    print("Invalid choice! Please enter 'vegetarian' or 'non-vegetarian'.")
