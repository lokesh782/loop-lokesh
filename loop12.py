input("Welcome to the Pirate Ship Adventure")
sam=input("'searches for treasure' or 'battle enemy ships': ")
if sam=='searches for treasure':
    shr=input("dig on island' or 'explore the cave': ")
    if shr=='dig on island':
        print("You found a hidden treasure chest. You win")
    else:
            print('You were trapped inside. Game Over.')
if sam=='battle enemy ships':
    luv=input("you want to'attack' or ' defend': ")
    if luv=='attack':
         print("You won the battle.You win")
    else:
         print("You were outnumbered.Game Over")