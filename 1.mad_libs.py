from random import randrange

correct = False
questions =  [
   {
      "question":"Basketball is the best {answer} in the world",
      "answer":"sport"
   },
   {
      "question": "Love is what makes the {answer} go round.",
      "answer": "world"
   },
   {
      "question":"My gym locker stinks because I'm always leaving my dirty {answer} in there!!",
      "answer":"socks",
   },
   {
      "question": "Once that {answer} music comes on, it's time to shut down your acceptance speech!",
      "answer": "radio"
   }
]
question_dict = questions[randrange(len(questions))]


print("Guess the next question ------------")
print("------------------------------------")
print(question_dict["question"])
print("------------------------------------")

while not correct:
   answer = input('My answer is: ')
   if answer == question_dict["answer"]:
      correct = True
      print(format(question_dict["question"]))
   else:
      print("incorrect")
      print(question_dict["question"].format(answer))