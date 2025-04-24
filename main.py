print(" Welcome ot the Prime Number Checker")
print(" Let's see if your number is prime or not")

# Get number from the user
num = int(input(" Enter a number:"))

# Check if number is prime
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f" oh no!{num} is NOT a prime number")
            break
    else:
        print(f" Yay {num} is a PRIME number")
else:
    print("Number less than 2 are NOT prime") 
print("Thanks for playing! Keep learning and exploring")               