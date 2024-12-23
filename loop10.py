
print("Welcome to the Haunted Castle")
choice = input("Do you want to 'enter the castle' or 'run away'? ")
if choice == "enter the castle":
    door_choice = input("Choose a door: 'red', 'green', or 'black': ")
    if door_choice == "red":
        print("You entered a room full of flames. Game Over.")
    elif door_choice == "green":
        print("You found the treasure. You Win!")
    elif door_choice == "black":
        print("You were captured by ghosts. Game Over.")
    
