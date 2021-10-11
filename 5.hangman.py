word = "jemoeder"
maximum = 10
round = 0
finished = False

while not finished:
   print("Guess the word or guess the letter?\n")
   choice = input("(1): Letter (2): Word:\n")
   if choice == "1" or choice == "2":
      print("Choice has made\n")
      if choice == "1":
         letter = input("Pick a letter:\n")
         if len(letter) > 1:
            print("Thats more than 2 letters!")
         else:
            index = word.find(letter)
            print(index)

      round = round + 1
   else:
      print("1 or 2 is the only choice\n")

   print("Only ", maximum - round, " left")