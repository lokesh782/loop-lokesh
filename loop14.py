input("Welcome to the Cybersecurity Mission")
sam=input("'trace the hacker' or 'secure the system': ")
if sam=='trace the hacker':
    shr=input("You want to 'track their IP' or 'decode their message': ")
    if shr=='track their IP':
        print("You caught the hacker. You Win!")
    else:
            print('The message was a trap. Game  over')
if sam=='secure the system':
   fut=input("'shut down the server' or 'upgrade the firewall': ")
   if fut=='shut down the server':
        print('The attack was stopped. You Win')
   else:
        print('The hacker bypassed it. Game Over')