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

#Write your code below this line 👇
user_choice = input("What do you choose?  Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice = int(user_choice)
if user_choice > 2 or user_choice < 0:
    print("Invalid choice!  You lose!")
    exit()

computer_choice = random.randint(0, 2)
hands = [rock, paper, scissors]
comp_rock = ["draw", "win", "lose"]
comp_paper = ["lose", "draw", "win"]
comp_scissor = ["win", "lose", "draw"]

rps_game = [comp_rock, comp_paper, comp_scissor]
outcome = rps_game[computer_choice][user_choice]
#print(user_choice) #DEBUG
#print(computer_choice) #DEBUG
#print(outcome) #DEBUG

print(f"You chose:\n {hands[user_choice]}")
print(f"Computer chose:\n {hands[computer_choice]}")
if outcome != "draw":
    print(f"You {outcome}")
else:
    print("The game is a draw.")