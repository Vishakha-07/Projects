#Cow bull game
#Importing random to generate a random number
import random

#Defining a variable for user input
a=0

#Rules for user
print("For every correct guess you will have 1 cow and for wrong guess you will have 1 bull \n To exit the game type \"exit\"")
#initial score
bull=0
cow=0
#Generating a random 2 digit number
x=random.randint(10,99)
while a!=x and a!="exit":
    a = (input("Guess a two digit number: "))
    if a!=x:
     bull+=1
     print("Bull", bull, "cow", cow)
    else:
     cow+=1
     print("Bull", bull, "cow", cow)
    if a=="exit":
     print("Number was: ", x, "\n You have total ", cow, " cow and ", bull, " bull")