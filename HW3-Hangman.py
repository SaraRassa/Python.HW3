import random
List=['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']
word=random.choice(List)
L=[]
joon=len(word)+3
print("You can try ",joon," times.")
while joon>0:
    for a in word:
        if a in L:
            print(a,end="")
        else:
            print("-",end="")
    user_char=input("\nEnter a letter: ")
    user_char=user_char.lower()

    if user_char in word:
        print("YES")
        L.append(user_char)
    else:
        joon=joon-1
        print("NO" "\nYou can try ",joon," more times")
    if len(word)==len(L):
   
        print(word,"\nYou win")
        break

