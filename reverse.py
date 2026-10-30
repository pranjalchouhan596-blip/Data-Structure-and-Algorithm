"""this is a program to reverse an integer"""

n= int(input("enter a number to get reverse: "))
n1=n
rem=0
ans=0
while n>0:
    rem=n%10
    n=n//10
    ans=ans*10+rem

print(f"the reverse of number {n1} is {ans}.")