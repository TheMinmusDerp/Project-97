import random
number = random(1,9)
guess = input("Guess a number")

while chances < 5:
  if guess == number:
    print("CONGRATULATION YOU WON")
    break
  if not chances < 5:
    print("YOU LOSE!!! The number is", number, "YOU IDIOT")
  chances=chances-1
