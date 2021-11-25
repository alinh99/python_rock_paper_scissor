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
game_images = [rock, paper, scissors]
# users choice
limits = 2
users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

while users_choice > 2 or users_choice < 0:
  print("Invalid input, Type 0 for Rock, 1 for Paper, 2 for Scissors.")
  users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
print(game_images[users_choice])
  # computer choice
computer_choice = random.randint(0, 2)
print("Computer choice:")
print(game_images[computer_choice])

# compare users choice with computer choice
if users_choice == computer_choice:
  print("It's a draw game.")
elif users_choice == 0 and computer_choice == 1:
  print("Computer wins.")
elif users_choice == 0 and computer_choice == 2:
  print("User wins")
elif users_choice == 1 and computer_choice == 0:
  print("User wins.")
elif users_choice == 1 and computer_choice == 2:
  print("Computer wins.")
elif users_choice == 2 and computer_choice == 0:
  print("Computer wins.")
elif users_choice == 2 and computer_choice == 1:
  print("User wins.")
