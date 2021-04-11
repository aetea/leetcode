# https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/


def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    if len(s) != len(t):
        return False
    
    # create dict for letters in s
    s_dict = {}
    for char in s:
        s_dict[char] = s_dict.get(char, 0) + 1
        
    # create dict for letters in t
    t_dict = {}
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
        
    # check if s and t have the same set of letters
    if s_dict.keys() != t_dict.keys(): 
        return False
    
    # check if s and t have same number of each letter
    for letter in s_dict:      
        if s_dict[letter] != t_dict[letter]:
            return False
    
    return True