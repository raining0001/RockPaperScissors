import random

rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice_img = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
guess = random.randint(0,2)
print(f"You choose\n{choice_img[user]}")
print(f"Guess choose\n{choice_img[guess]}")

if user == 0 and guess == 1:
  print("You lost!")
  if user == 0 and guess == 2 :
   print("You won!")
elif user == 1 and guess == 0 :
  print("You won!")
  if user == 1 and guess == 2 :
   print("You lost!")
elif user == 2 and guess == 0 :
  print("You lost!")
  if user == 2 and guess == 1 :
   print("You won!")
else:
  print("It's a draw!")