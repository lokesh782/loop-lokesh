
print("Welcome to the Space Adventure")
choice = input("Do you want to 'land on Mars' or 'fly to Jupiter'? ")

if choice == "land on mars":
    mars_choice = input("Do you want to 'explore' or 'build a base'? ")
    if mars_choice == "explore":
        print("You found alien artifacts. You Win!")
    
    elif mars_choice == "build a base":
        print("You ran out of resources. Game Over.")
    
    else:
        print("Invalid choice. Please choose either 'explore' or 'build a base'.")
    
elif choice == "fly to jupiter":
    print("Your spaceship crashed. Game Over.")
    
else:
    print("Invalid choice. Please choose either 'land on Mars' or 'fly to Jupiter'.")
