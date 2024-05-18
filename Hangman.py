import random

print(" /\/\/\  HANGMAN  \/\/\/ ")
name = input("Your Name ? ")
print("Good Luck, ", name, " !")

words = ["python","computer", "technology", "sports", "field", "employ", "solve", "trick", "budget"]
word = random.choice(words)
      
print("Guess the characters ..")
guesses = " "
chances = 10

while(chances > 0):
    remained = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            remained += 1

    if remained == 0:
        print()
        print("YOU WON THE GAME")
        print("ANSWER: ", word)
        break

    print()
    guess = input("Guess the character: ")

    guesses += guess

    if guess not in word:
        chances -= 1
        print("wrong")
        print("You have ", chances, "more guesses")

        if chances == 0:
            print()
            print("YOU LOST THE GAME")
            print("ANSWER: ", word)


