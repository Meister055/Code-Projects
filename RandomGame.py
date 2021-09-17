# Boring imports
import random as rd

tryText = "try"
guesses = 0
ranNum = rd.randint(1, 10)
name = input("What's your name? ")
print("Hello " + name + "!")
while guesses < 5:
  guesses += 1
  guess = input("Enter a guess: ")
  try:
    float(guess)
  except ValueError:
    guesses -=1
    print("Invalid input, please try again.")
    continue
  if int(guess) < ranNum:
    print("Too low! Try again.")
  if int(guess) > ranNum:
    print("Too high! Try again.")
  if int(guess) == ranNum:
    if guesses > 1:
      tryText = "tries"
      print("Great job! The number was: " + str(ranNum) + " and you got it in " + str(guesses) + " " + tryText + "!")
      break

