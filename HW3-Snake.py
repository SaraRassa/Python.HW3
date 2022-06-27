n=int(input("Enter snake's lenght: "))
Snake=[]
for i in range(n):
    if i%2==0:
        Snake.append("*")
    else:
        Snake.append("#")
a=''.join(Snake)
print(a)

