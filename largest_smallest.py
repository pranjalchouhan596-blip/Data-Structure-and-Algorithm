"""this is a program to find the largest and smallest number in an array"""

sz=int(input("enter the size of an array : ")) # declared variable globally
arr=[0]*sz # Pre-allocate a fixed-size list filled with zeros
def largest(arr):
    max_val=float('-inf')
    for i in range(sz):
        if arr[i]>max_val:
            max_val=arr[i]
    return max_val

def smallest(arr):
    min_val=float('+inf')
    for i in range(sz):
        if arr[i]<min_val:
            min_val=arr[i]
    return min_val

for i in range(sz):
    arr[i]=int(input(f"enter array element at position {i} : "))
print("the smallest number in the array is : ",smallest(arr))
print("the largest number in the array is : ",largest(arr))