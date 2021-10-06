from random import randrange
dice_number = randrange(6)
correct = False

while not correct:
   print('Dice game! Guess the number between 1 and 6')
   print('What is your guess?')
   user_input = input()

   if int(dice_number) == int(user_input):
      correct = True
      print('You got it!')
   else:
      print('It was wrong!')
      print('Dice number:', dice_number)