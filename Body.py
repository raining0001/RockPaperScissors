from art import rock , paper , scissors
import random

class Main:
    def __init__(self,user,guess,choice_img):
        self.user = user 
        self.guess = guess
        self.choice_img = choice_img

    def user_input(self):
        self.choice_img = [rock,paper,scissors]
        self.user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
        self.guess = random.randint(0,2)
        print(f"You choose\n{self.choice_img[self.user]}")
        print(f"Guess choose\n{self.choice_img[self.guess]}")


    def game(self):
        if self.user == 0 and self.guess == 1:
            print("You lost!")
        if self.user == 0 and self.guess == 2 :
            print("You won!")
        elif self.user == 1 and self.guess == 0 :
            print("You won!")
        if self.user == 1 and self.guess == 2 :
            print("You lost!")
        elif self.user == 2 and self.guess == 0 :
            print("You lost!")
        if self.user == 2 and self.guess == 1 :
            print("You won!")
        else:
            print("It's a draw!")
