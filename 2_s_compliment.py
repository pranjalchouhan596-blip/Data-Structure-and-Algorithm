"""2's compliment= two's compliment means representing a negative number in binary form,
1. we have to convert the raw number in binary
2. then add a zero in the startingmost place
3. replace zero with one and one with zero
4. add one in that new binary number
5. then the number we will get will be a two's compliment"""

def add_binary(a: str,)->str:
    binary_str=bin(int(a,2)+1)[2:]
    return binary_str
ans=0
def binary(n):
    global ans
    pow=1
    while n!=0:
        rem=n%2
        n=n//2
        if rem==0:
            ans=ans+1*pow
            pow=pow*10
        if rem==1:
            ans=ans+0*pow
            pow=pow*10
    ans=ans+1*pow
    ans_str=str(ans)
    return add_binary(ans_str)

num=int(input("enter a number to get it's two's compliment: "))
final= binary(num)
print(final)

