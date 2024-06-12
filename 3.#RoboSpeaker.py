import pyttsx3
engine = pyttsx3.init()

while True:
    x = input("Enter what to speak: ")
    if x == 'q':
        break

    engine.say(x)
    engine.runAndWait()


    