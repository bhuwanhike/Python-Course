import random

class Game:
    moves = ['Snake', 'Water', 'Gun']
    def __init__(self):
        print("Welcome to the Game".center(50))
        self.user = ''
        self.computer = ''
        self.user_score = 0
        self.computer_score = 0

        
    def user_input(self):
        self.user = input("Your move: ").lower()
        if self.user == 'q':
            print("Your total score: ", game.user_score, "             Computer score: ", game.computer_score)
            self.scoring()
            exit()

    
    def computer_move(self):
        self.computer = random.choice(self.moves).lower()
        print("Computer: "+ self.computer)

    
    def scoring(self):
        if self.user_score == self.computer_score:
            print("It's a draw!")
        
        elif self.user_score > self.computer_score:
            print("Congratulations! You won the game.")

        elif self.user_score < self.computer_score:
            print("Better luck next time! You lost the game.")
    
    def condition(self):

        if self.user == self.computer:
            print("That's a draw!")
        # You won!
        elif (self.user == 'snake' and self.computer == 'water') or (self.user == 'water' and self.computer == 'gun') or (self.user == 'gun' and self.computer == 'snake'):
            self.user_score += 5
            print("You won!")
        
        # You lose!
        elif (self.user == 'gun' and self.computer == 'water') or (self.user == 'snake' and self.computer == 'gun') or (self.user == 'water' and self.computer == 'snake'):
            self.computer_score += 5
            print("You lose!")
      
           
game = Game()
while True:
    game.user_input()
    game.computer_move()
    game.condition()
    
        
       