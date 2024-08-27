import random
import math

def guessNumberGame():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1-100!")

    masterKey = random.randint(1,100)
    attempts = 0
    while True:
        try:
            playerGuess = int(input("Take a guess! : "))
            attempts += 1
            if playerGuess > masterKey:
                print("Too high! Try again! : ")
            elif playerGuess < masterKey:
                print("Too low! Try again! :")
            else:
                print(f"Congrats! You guessed the number in {attempts} attempts!")
                break
            
        except ValueError:
                print("Invalid input try again! ")
if __name__ == "__main__":
    guessNumberGame()