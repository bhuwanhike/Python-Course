import random, time, difflib

def main():

    total_time_per_sentence = 0
    accuracy_per_sentence = 0

    while(True):

        sentences = [
            "Python is an amazing programming language.",
            "Practice makes perfect.",
            "Typing speed matters in coding challenges.",
            "Never stop learning and building projects."
        ]
        word_count = sum((len(s.split()) for s in sentences))
        random.shuffle(sentences)

        print('-'*10, 'Welcome to Typing Test', '-'*10)

        start_Test = input("Press enter key to start the test: ")
        
        if start_Test == '':
            
            start = time.time()
            for sentence in sentences:
                print(sentence)
                typed_Sentence = input("")
                word_count+=len(typed_Sentence.split())
                if typed_Sentence == 'q':
                    break
                seq = difflib.SequenceMatcher(None, sentence, typed_Sentence)
                ratioAccuracy = seq.ratio()
                accuracy_per_sentence+=ratioAccuracy
             
            stop = time.time()
            total_time_per_sentence+=(stop-start)
            if total_time_per_sentence < 1:
                total_time_per_sentence = 1
            avg_accuracy = (accuracy_per_sentence/len(sentences))*100

            print(f"WPM count: ",(word_count//    total_time_per_sentence )*60)
            print(f"Accuracy: ",avg_accuracy)
            
            choice = input("Press enter to play again or press q to exit the test: ")
            if choice == "q":
                total_time_per_sentence = 0
                accuracy_per_sentence = 0
                break
            else:
                total_time_per_sentence = 0
                accuracy_per_sentence = 0
            


if __name__ == '__main__':
    main()
