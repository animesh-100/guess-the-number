import random

def guess(x):
  random_number=random.randint(1,x)
  guess = 0
  while guess != random_number:
    guess=int(input("Enter the number : "))
    if guess< random_number:
      print("number is too low")
    elif guess> random_number:
      print("number is too high")

  print("You have decided the right number")

guess(10)
