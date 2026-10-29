"""this is a program to determine if the given number is power of 2 or not"""
num=int(input("enter number to check if it is power of 2: "))

pow=0
number=num
while num>1:
    if num%2==0:
        num=num//2
        pow=pow+1
    else:
        pow=0
        break
if pow!=0:
    print(f"the number {number} is power of 2, the power is {pow}")
else:
    print("the number is not power of 2")