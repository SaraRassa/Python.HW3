n=int(input("How many numbers do you want to enter? "))
L=[]
for i in range(n):
    a=float(input("Enter numbers: "))
    L.append(a)
print(L)
if L==sorted(L):
        print("list is sorted.")
else:
        print("list in NOT sorted.")
       
