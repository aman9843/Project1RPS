# Rock, Paper, Scissor Game using python code:

import random
Choice = ['Rock', 'Paper', 'Scissors']
while True:
    print('Welcome')
    user_count = 0
    comp_count = 0
    for i in range(1, 4):
        print("Round-", i)
        print("Enter the value 1.Rocky 2.Paper 3.Scissors")
        your_choice = int(input())

        if(your_choice == 1):
            print("You have Selected Rock!")
            your_choice = "Rock"
        elif (your_choice == 2):
            print("You have Selected Paper!")
            your_choice = "Paper"
        elif (your_choice == 3):
            print("You have Selected Scissor!")
            your_choice = "Scissors"
        else:
            print("Wrong choice Please select again !")
            break

        computer_choice = random.choice(Choice)
        print("Computer Choice", computer_choice)
        if(your_choice == computer_choice):
            print("Draw!")
        elif((your_choice == 'Rock' and computer_choice == 'Scissors') or     (
              your_choice == 'Paper' and computer_choice == 'Rock')  or   (
              your_choice == 'Scissors' and computer_choice == 'Paper')):
            user_count = user_count + 1
        elif ((your_choice == 'Scissors' and computer_choice == 'Rock') or     (
              your_choice == 'Rock' and computer_choice == 'Paper')  or   (
              your_choice == 'Paper' and computer_choice == 'Scissors')):
            comp_count = comp_count + 1


    if(user_count > comp_count):
        print("Hurray You Win !")
    elif(user_count<comp_count):
        print("Sorry You Lose Computer Wins")
    else:
        print("Draw")
    print("Do You Want To Play Again? Yes or No")
    x = input('Enter Yes or No')
    if(x == 'Yes' or x == 'yes' or x == 'YES'):
        continue
    else:
        break

