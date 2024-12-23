
print("Welcome to the Underwater World")
choice = input("Do you want to 'dive deeper' or 'surface'? ")
if choice == "dive deeper":
    underwater_choice = input("Do you want to 'search for pearls' or 'chase the fish'? ").lower()
    if underwater_choice == "search for pearls":
        print("You found a rare pearl. You Win!")
    elif underwater_choice == "chase the fish":
        print("You got lost underwater. Game Over.")
    else:
        print("Invalid choice. Please choose either 'search for pearls' or 'chase the fish'.")
elif choice == "surface":
    print("You returned safely.")
else:
    print("Invalid choice. Please choose either 'dive deeper' or 'surface'.")
