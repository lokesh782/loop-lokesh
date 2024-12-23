
print("Welcome to the Jungle Survival Challenge")
choice = input("Do you want to 'search for food' or 'build a shelter'? ").lower()
if choice == "search for food":
    food_choice = input("Do you want to 'hunt' or 'gather'? ").lower()
    
    if food_choice == "hunt":
        
        print("You were attacked by a wild animal. Game Over.")
    
    elif food_choice == "gather":
        
        print("You found enough food. You Win!")
    else:
        print("Invalid choice. Please choose either 'hunt' or 'gather'.")
elif choice == "build a shelter":
    
    print("Your shelter collapsed in the rain. Game Over.")
    
else:
    print("Invalid choice. Please choose either 'search for food' or 'build a shelter'.")
