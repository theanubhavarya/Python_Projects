# ROBOSPEAKER PROJECT!

import pyttsx3
engine = pyttsx3.init()
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Anubhav!")
    print("NOTE: Press q to exit.")
    while True:
        x = input("Enter what you want me to pronounce: ")
        if x == "q":
            engine.say("Bye Bye Friend")
            engine.runAndWait()
            print("Bye Bye Friend!".center(50, "~"))
            break
        command = engine.say(x)
        engine.runAndWait()