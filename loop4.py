num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is divisible by 2.")
    if num % 5 == 0:
        print("The number is also divisible by 5.")
    else:
        print("The number is not divisible by 5.")
else:
    print("The number is not divisible by 2.")
