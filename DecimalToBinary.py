"""A program to convert decimal number into binary number using basic functions and logics
here we use // so that we don't get a float number if there will be a float number, whenever the 
number is divides it will never become zero. and the loop will run infinitely"""

num = int(input("enter a number to convert into binary :"))
pow=1
ans=0
while(num>0):
    rem = num%2
    num= num//2

    ans+= rem*pow
    pow= pow*10
print("the number in binary is :",ans)