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
for a in range(0, n):
    print("Enter number at index", a, )
    item = int(input())
    num.append(item)
print(num)
for b in range(0,len(num)):
   a= target -num[b]
   if a in num and b != num.index(a):
       print ((b,num.index(a)))
       break
        
   # next solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range (0,n):
            a = target - nums[i]
            if a in nums and i != nums.index(a):
                return (i,nums.index(a))
        
                
        
