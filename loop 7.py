
print("Welcome to the Forest Adventure!")
path = input("Do you want to go left or right? ")

if path == "left":
    action = input("Do you want to explore or rest? ")
    
    if action == "explore":
        print("You found treasure!")
    elif action == "rest":
        print("You were attacked by wild animals. Game over.")
    else:
        print("Invalid choice! Please choose 'explore' or 'rest'.")
elif path == "right":
    print("You wander deeper into the forest and get lost. Game over.")
else:
    print("Invalid choice! Please choose 'left' or 'right'.")
