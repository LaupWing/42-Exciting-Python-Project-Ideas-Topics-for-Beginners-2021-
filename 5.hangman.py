import re
word = "jemoeder"
guess = list(len(word) * "*") 
maximum = 10
round = 2

def check(value):
   if value == word:
      print("You got it!!\n")
      print("The answer was: ", word)
      return True
   return False

while True:
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
            if check("".join(guess)):
               break
      else:
         guess_word = input("What is your guess? ")
         if check(guess_word):
            break
      round = round + 1
      if maximum == round:
         print("You lost!")
         break
   else:
      print("1 or 2 is the only choice\n")

   print("Only ", maximum - round, " left")

