
print("Welcome to the Wizarding World")
subject_choice = input("Do you want to study 'spells' or 'potions'? ").lower()
if subject_choice == "spells":
    magic_choice = input("Do you want to 'practice magic' or 'compete in duels'? ").lower()
    if magic_choice == "practice magic":
        print("You mastered a powerful spell. You Win!")
    elif magic_choice == "compete in duels":
        print("You lost to a rival wizard. Game Over.")
    else:
        print("Invalid choice. Please choose either 'practice magic' or 'compete in duels'.")
elif subject_choice == "potions":
    potion_choice = input("Do you want to 'brew an elixir' or 'create poison'? ").lower()
    if potion_choice == "brew an elixir":
        print("You healed a village. You Win!")
    elif potion_choice == "create poison":
        print("Your potion backfired. Game Over.")
    else:
        print("Invalid choice. Please choose either 'brew an elixir' or 'create poison'.")
else:
    print("Invalid choice. Please choose either 'spells' or 'potions'.")
