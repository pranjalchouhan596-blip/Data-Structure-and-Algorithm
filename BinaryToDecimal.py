"""this is a program to calculate binary form of any decimal number
here if we have to convert a binary to decimal we multiply 2's power to each of the 
digit of binary number, in an increasing order from right to left, and then add all the multiples."""

n=int(input("enter number to convert in decimal : "))
n1=n
pow = 1
ans=0
while(n>0):
    rem=n%10
    n=n//10
    ans= ans+(rem*pow)
    pow=pow*2

print(f"the decimal form of binary number {n1} is {ans}")