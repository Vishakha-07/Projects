#coding for stone paper scissor game

import random
#Asking user for his/her name
a=str(input("What is your name? "))
print("Hello ", a, " Let's play stone, paper, scissor!")

#Total chance
print("You have got 5 chances")
#Initializing chance
chance=1

#Initializing score
you=0
comp=0

#Initializing user variable
z=0

#Creating a list from where computer can randomly choose
foo = ["stone", "paper", "scissor"]

while chance<=5:

# Asking user to choose between stone, paper or scissor
 z=str(input("Enter your choice: Stone, Paper or Scissor- "))
#Changing user's input in lower case
 x=z.lower()

#Computer randomly choosing from list
 y = random.choice(foo)

#stone beats scissor
 if (x=="stone" and y=="scissor"):
  print("you won")
  you=you+1
  print("computer choice is ", y)
  chance += 1

 #scissor beats paper
 elif x=="scissor" and y=="paper":
  print("you won")
  you = you + 1
  print("computer choice is ", y)
  chance += 1

#paper beats stone
 elif x=="paper" and y=="stone":
  print("you won")
  you = you + 1
  print("computer choice is ", y)
  chance += 1

 #condition of tie between user and computer
 elif x==y:
  print("It's a tie")
  print("computer choice is also", y)
  chance += 1

 #conditions in which computer can win
 else:
  print("computer won")
  comp=comp+1
  print("computer choice is ", y)
  chance += 1

#Total Scoring of User and computer
if you>comp:
    print("You won! Your total score is: ", you, " and computer total score is ",comp )
elif you==comp:
    print("It's a tie Your score: ", you , " and Computer's score: ", comp)
else:
    print("Computer won! Computer total score is ", comp, " and Your score is: ", you)
