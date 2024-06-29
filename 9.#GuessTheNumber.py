import random

class Guess:
    i = 1
    def __init__(self):
        print("Welcome to the Game".center(50))

    def user(self):
        self.user_input = input("Guess the number: ")
    
    def computer(self):
        self.comp = str(random.randint(1, 100))
        # print('computer:', self.comp)

    def condition(self):
        if self.user_input == self.comp:
            print("""It's a match! Your total attempts are: """, Guess.i)
            exit()
        
        elif self.user_input > self.comp:
            Guess.i+=1
            print("Please guess a lower number!")

        elif self.user_input < self.comp:
            Guess.i+=1
            print("Please guess a higher number!")


guess = Guess()
guess.computer()
while True:
    guess.user()
    guess.condition()