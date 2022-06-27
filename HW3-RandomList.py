import random

n=int(input("How many numbers do you want in the list? "))
L=random.sample(range(0,1000),n)
print("List= ",L)