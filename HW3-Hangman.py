import random
Words=["Sara","Ali","gol","DATA","python","daFtar","ClaSS","bazi"]
word=random.choice(Words)
Attempts=10

while Attempts>0:
    print("-"*len(word))
    user_word=input("Guess a word: ")
    if user_word.lower()==word.lower():
        print("You win!")
        print("Number of attempts: ", (10-Attempts))
        break
    else:
        print("Try again")
        Attempts=Attempts-1
        print("You have ", Attempts ,"attempts left")