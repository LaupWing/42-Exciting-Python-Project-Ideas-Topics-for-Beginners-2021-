from random import randrange
numbers = input('Range of numbers: ')
guess_number = randrange(int(numbers))
correct = False

while not correct:
   answer = input('My answer is: ')
   if int(answer) == guess_number:
      print('Correct! The answer was: ', guess_number)
      correct = True
   else:
      print("Wrong! Guess again")