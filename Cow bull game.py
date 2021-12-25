#Cow bull game
#Importing random to generate a random number
import random

#Defining a variable for user input
a=0
count=0
#Rules for user
print("You have got 5 chances! For every correct guess you will have 1 cow and for wrong guess you will have 1 bull")
#initial score
bull=0
cow=0
#Generating a random 2 digit number

while count<5:
    count+=1
    x=random.randint(10,99)
    a = int(input("Guess a two digit number: "))
    if a==x:
     cow+=1
     print("Bull", bull, "cow", cow)
    else:
     bull+=1
     print("Bull", bull, "cow", cow)
print("You have total ", cow, " cow and ", bull, " bull")