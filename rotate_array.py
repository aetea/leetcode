# https://leetcode.com/problems/rotate-array/

def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    # # METHOD 1: remove from front, add to end --> O(n)
    # new_last_index = len(nums) - k
    # send_to_back = nums[0:new_last_index]
    # del nums[0:new_last_index]
    # nums.extend(send_to_back)
    

    # METHOD 2a: change list pointers 
    if k == 0 or len(nums) < 2:
        return
    
    if k > len(nums):
        print(f"nums has {len(nums)} elements")
        k = k % len(nums) 
    
    new_head = nums[-k:]
    idx_from_tail = len(nums) - 1
        
    while idx_from_tail > (k - 1):
        nums[idx_from_tail] = nums[idx_from_tail - k]
        idx_from_tail -= 1
        
    for idx_from_head in range(k):
        nums[idx_from_head] = new_head[idx_from_head]
       
    # # METHOD 2b: change list pointers, loop in one direction
    # new_head = nums[-k:]

    # # loop over the list backwards
    # idx_from_tail = len(nums) - 1
    # while idx_from_tail > -1: 
    #     if idx_from_tail > (k-1):
    #         nums[idx_from_tail] = nums[idx_from_tail - k]
    #     else:
    #         nums[idx_from_tail] = new_head[idx_from_tail]
    #     idx_from_tail -= 1