# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i+1]
        else:
            i += 1      
        
    return len(nums)
    
    
input=[0,0,1,1,1,2,2,3,3,4]
output=[0,1,2,3,4]

len = removeDuplicates(input) 

print(f"{input[0:len]}")