import re
word = "jemoeder"
guess = list(len(word) * "*") 
maximum = 10
round = 0
finished = False

def check(value):
   if value == word:
      print("You got it!!\n")
      print("The answer was: ", word)
      global finished
      finished = True

while not finished:
   print("Guess the word or guess the letter?\n")
   choice = input("(1): Letter (2): Word:\n")
   if choice == "1" or choice == "2":
      if choice == "1":
         letter = input("Pick a letter:\n")
         if len(letter) > 1:
            print("Thats more than 2 letters!")
         else:
            indexes = [m.start() for m in re.finditer(letter, word)]
            for index in indexes:
               guess[index] = letter
            print("".join(guess))
            check(guess)
      else:
         guess_word = input("What is your guess?")
         check(guess_word)
      round = round + 1
   else:
      print("1 or 2 is the only choice\n")

   print("Only ", maximum - round, " left")

