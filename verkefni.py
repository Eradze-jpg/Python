#Verkefni
"""
listi=[1,2,3,4,5,6,7,8,9]
summa= 0
for tala in listi:
    summa+= tala
print("Summa listans", listi, "er", summa)
"""
"""
n= int(input("write a number"))
if n > 1:
    for i in range(2, int(n/2)+1):
        if (n % i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is not a prime number")
"""
"""
strengur= input("Sláðu inn streng: ")
strengurinn=[]
for i in strengur:
    strengurinn.append(i)
for x in strengurinn:
    print(-x)
"""
"""
n= input("Write down a string: ")
summa= 0
for i in n:
    if i== "a" or i=="e" or i=="i" or i== "o" or i=="u":
        summa+=1
print(summa)
"""
"""
summa=0
while True:
    n= input("Enter a number: (or 'done' to exit )")
    if n == "done":
        break
    else:
        y=int(n)
        summa+=y
print(summa)
"""
"""
invite=input("Enter names (seperated by spaces): ")
ans=invite.split(" ")
for i in ans:
    print("Hello,",i,"!")
"""
"""
import random
counter= 0
guess= random.randint(1, 100)
while True:
    val= int(input("Guess a number between 1 and 100: "))
    counter+=1
    if val > guess:
        print("Too high! Try again.")
    elif val < guess:
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed the number in", counter,"attempts")
"""
"""
n= input("Enter numbers(Separated by commas):")
max_summa= 0
ank= n.split(", ")
listi= []
for i in ank:
    i=int(i)
    listi.append(i)
    if i > max_summa:
        max_summa = i
print("Entered numbers:",ank)
min_summa= min(listi)
print("Maximum value:",max_summa)
print("Minimum value:",min_summa)
"""
"""
n= input("Write down a word: ")
ok= n[::-1]
if n == ok:
    print("The word is the same in reverse:",ok)
else:
    print("The word is not the same in reverse:",n)
"""

n= int(input("Write in a number: "))
for i in range(1, n):
    if n % i==0:
        print(i, end=" ")
