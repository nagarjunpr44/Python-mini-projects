import random

# r=random.randrange(-1,11) does not include 11
#r=random.randint(-1,11)

top_of_range=input("Enter your range : \n")
t=top_of_range

if t.isdigit():
    t=int(t)
    
    if t<=0:
        print("Please enter a number greater than zero ")
        quit()
else:
    print("Please enter a number next time ")
    quit()

random_number=random.randint(0,t)
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a guess : ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please enter a number next time ")
        continue

    if user_guess==random_number:
        print("you got it right")
        break
    elif user_guess>random_number:
        print("Your guess was greater than the number")
    else:
        print("Your guess was lesser than the number")    

print("You got it in ",guesses,"guesses")
