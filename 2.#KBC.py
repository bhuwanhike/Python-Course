import random
questions = {"1.What is the most common full form for AI?": [["Artificial Intelligence", "Automated Integration", "Autonomous Intelligence", " Amplified Intelligence"], ["Artificial Intelligence"]] , "2.Where is India's Silicon Valley located?": [["Bengaluru", "Haryana", "New York", "California"], ["Bengaluru"]], "3.Who heads the RBI?": [["Shri Shaktikanta Das", "Sri Nivasa Goel", "Sir Osborne Smith", "Dr. Bimal Jalan"], ["Shri Shaktikanta Das"]], "4.Who created Python?": [["Guido van Rossum", "Larry Page", "Arnove Clive", "Bjarne Stroustrup"], ["Guido van Rossum"]], "5.Who created Bitcoin?": [["Satoshi Nakamoto", "Tim Berners-Lee", "Jackson Palmer", "Billy Markus"], ["Satoshi Nakamoto"]], "6.Who wrote the book Hands On Machine Learning?": [["Geron Aurelien", "Rich Hogwarts", "James Bond", "Gotham Python"], ["Geron Aurelien"]]}


print("Welcome to Kaun Banega Crorepati: ")
print("Press q to start the game: ")
a = input()
if a == 'q':
    amount = 0
    print("Your first question is on the screen:")
    for key, value in questions.items():
        if key == "6.Who wrote the book Hands On Machine Learning?":
            print("This is the jackpot question, if you give the right answer for this question you will win 7 crores otherwise you will lose all of your money, you have a choice if you want to play then press p or q or quit: ")
            opt = input("Choice: ")
            if opt == "p":
                print("Your jackpot ques. is here: ")
                print(key)
                random.shuffle(value[0])
                print(f"a.{value[0][0]}  b.{value[0][1]}  c.{value[0][2]}  d.{value[0][3]}") 
                i = input("Enter: ")
                if i == value[1][0]:
                    print("Congratulations! You won 7 crore rs.")
                    amount = 70000000
                    exit()
                else:
                    amount = 0
                    print("Sorry you lose! Your balance is:",amount)
                    exit()    
                
            elif opt == "q":
                print("Congratulations! Your winning amount is: ",amount)
                
                exit()
        print(key)
        random.shuffle(value[0])
        print(f"a.{value[0][0]}  b.{value[0][1]}  c.{value[0][2]}  d.{value[0][3]}") 
        i = input("Enter: ")
        if i == value[1][0]:
            print("Right answer! You won rs. 500")
            amount+=500
            print("Your balance: ", amount)
        else:
            print("You lose!")    
            break
           
print(amount)        
