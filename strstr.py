# https://leetcode.com/problems/implement-strstr/

def strStr(self, haystack: str, needle: str) -> int:
    # # --- METHOD 1:
    # if len(needle) == 0:
    #     return 0
    
    # if len(haystack) == 0 or len(needle) > len(haystack):
    #     return -1
    
    # start = 0
    # end = start + len(needle) 

    # # loop over haystack (until end_idx = len of haystack)
    # while end <= len(haystack): 
    #     # compare needle to haystack[start_idx to end_idx]
    #     if haystack[start:end] == needle:
    #         return start
    #     start += 1
    #     end += 1
        

    # # --- METHOD 2
    # for i in range(len(haystack) - len(needle) + 1): 
    #     if haystack[i:i+len(needle)] == needle: # haystack[0:1] == needle
    #         return i

    # --- NOTES: 
    # method 1 & 2 less efficient because:
    # list slicing requires making a new copy 
    # comparing two lists requires iterating over each element
        

    # --- METHOD 3: window in nested loop - more efficient, O(n * m)
    # loop over each letter in haystack
    for i in range(len(haystack) - len(needle) + 1):
        # loop over each needle-letter, but skip if no match to haystack letter
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
        # if j loops fully, then return i
        else:
            return i

    return -1