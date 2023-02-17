print("Welcome to the quiz")

play=input("Do you want to play the game? \n")

if  play.lower() !="yes":
    print("Okay bye")
    quit()

print("Okay lets play :)\n")
moneywon=0

answer=input("What does CPU stand for?\n")

if answer.lower()=="central processing unit":
    print("Correct Answer\n")
    moneywon +=10000
    #print(moneywon)
else:
    print("Wrong answer \n You won $"+str(moneywon))
    quit()

answer = input("What is the capital of New Zealand?\n")

if answer.lower() =="wellington":
    print("Correct Answer\n")
    moneywon =moneywon +10000
   # print(moneywon)

else:
    print("Wrong answer \n You won $"+str(moneywon))
    quit()

answer=input("In what US State is the city Nashville?\n")

if answer.lower() =="tennessee":
    print("Correct Answer\n")
    moneywon +=10000

else:
    print("Wrong answer \n You won $"+str(moneywon))
    quit()

print("Congratulations You won $"+str(moneywon))