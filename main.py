import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#code written below this line 👇
# type 0 for rock, 1 for paper or 2 for scissor
game_image=[rock,paper,scissors]
User_choice=int(input("Type 0 for rock,Type 1 for paper,Type 2 for scissors \n"))
if(User_choice<3):
    print(game_image[User_choice])
"""if(User_choice==0):
    print(rock)
elif(User_choice==1):
    print(paper)
elif(User_choice==2):
    print(scissors)"""

Computer_choice=random.randint(0,2)

if(User_choice<3):
    print("Computer Chose : ")
    print(game_image[Computer_choice])
    """if(Computer_choice==0):
        print(rock)
    elif(Computer_choice==1):
        print(paper)
    elif(Computer_choice==2):
        print(scissors) """


if(User_choice==0 and Computer_choice==2):
    print("You Won!")
elif(User_choice==2 and Computer_choice==0):
    print("You Lose!")
elif(Computer_choice>User_choice and User_choice<3):
    print("You Lose!")
elif(Computer_choice<User_choice and User_choice<3):
    print("You Won!")
elif(Computer_choice==User_choice):
    print("Its a draw")
else:
    print("Invalid Input")