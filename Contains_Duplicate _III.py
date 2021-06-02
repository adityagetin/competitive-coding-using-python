"""
Given an integer array nums and two integers k and t, 
return true if there are two distinct indices i and j in the 
array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

 Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        num_len = len(nums)
        if t == 0 and len(nums) == len(set(nums)):
            return False
        for idx , val in enumerate(nums):
            for j in range (idx+1 , min(idx+1+k, num_len)):
                if abs(val -nums[j]) <=t:
                    return True
                
        return False
        
