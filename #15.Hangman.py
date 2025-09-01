from getpass import getpass


# print(True or False)


def game_start():

  
    Word = getpass("\nEnter the word, don't worry your typed word will not be visible to the guesser!: ").upper()
    blanks_list = ['_']*len(Word)

    player_Lives = 5
    
    while True :

        print(f'''\nLives: {player_Lives} \n''')       
        
        print(' '.join(blanks_list))

        guessed_letters_list = []

   
        if player_Lives == 0:
            print("\nNo more lives left! You lose the game.")
            break

        if ''.join(blanks_list) == Word:
            print("\nCongratulations! You won the game.")
            break


        Guessed_Letter = input("\nGuess the letter: ").upper()

        if (Guessed_Letter not in Word) or (Guessed_Letter in guessed_letters_list):
            player_Lives-=1

        if Guessed_Letter == "":
                print("Please enter a valid letter!")
                continue

        
        for i,c in enumerate(Word):

            
            if c == Guessed_Letter:
                
                blanks_list[i] = Guessed_Letter
                guessed_letters_list.append(Guessed_Letter)

def main():
    
    
    print("-"*20,'Welcome to Hangman',"-"*20)
   
    while(True):

        choice = input("Press enter to continue or q to exit: ")
        if choice =='q':
            break
     
        game_start()
        choiceAgain = input("\nDo you want to play again? Press 1 for yes or q for exit.")

        if choiceAgain == '1':
            continue
        if choiceAgain == 'q':
            break


if __name__ == "__main__":
    main()
    # pass
    