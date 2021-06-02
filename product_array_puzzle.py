"""A Product Array Puzzle

Given an array arr[] of n integers, construct a Product Array prod[]
(of same size) such that prod[i] is equal to the product of all the
elements of arr[] except arr[i]. """


def mul(arr,n):
    if n==1:
        print(0)
        return
    i,temp = 1,1
    pod = [1 for i in range(n)]
    for i in range(n):
        pod[i]=temp
        temp *=arr[i]
    temp =1
    for i in range(n-1,-1,-1):
        pod[i] *= temp
        temp *= arr[i]
    for i in range(n):
        print(pod[i],end=",")
    return






def prrod(arr,n):
    pd=1
    for i in arr:
        pd *=i
    for i in arr:
        print(int(pd*(i**-1)),end=",")

arr=[1,2,3,4]
n=len(arr)

mul(arr,n)
print("\n")
prrod(arr,n)
