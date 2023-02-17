


name=input("Enter your name\n")
print("Welcome ",name,"to your adventure\n")

answer=input("Where do you want to start your your adventure ,you can turn left or right please choose\n").lower()

if answer=="left":
    answer= input("You come across a river,you can walk around it or swim across(type w to walk and S to swim).\n").lower()


    if answer=="s":
        print("you swam across and was eaten by an alligator\n")
    elif answer=="w":
        print("You walked for many miles and ran out of water and died\n")
    else:
        print("Invalid input You lose")

elif answer=="right":
    answer=input("you come across a broken bridge,do you want to cross it or head back (cross/back)\n").lower()

    if answer=="cross":
        print("You cross the road and enter the next level,You won this round! \n")
    elif answer=="back":
        print("You are back to the strating point,You Lose\n")
    else:
        print("Invalid input type again")
        

else:
    print("Invalid input you lose")

print("Thank you for playing",name)