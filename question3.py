"""#
two sum


given an array(list) of integer nums and an integer target, returns indices
of the two nums such the are add up to target.
you may asume that each input would have exactly one solution and you may not use same element twice.
you can return the answer in any order.

example:
input:num =[2,7,11,15] , target =9
output: [0,1]
because num[0]+num[1] == 9
"""

target =int(input("enter the target"))
num =[]
n= int(input("enter the size list"))
for a in range(0, n+1):
    print("Enter number at index", a, )
    item = int(input())
    num.append(item)
print(num)
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j] == target:
            print([i,j])
        else:
            pass




