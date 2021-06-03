# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        
        seen_nodes = set()
        curr_node = head # 1-1
        prev_node = None
        
        while curr_node != None: 

            if curr_node.val in seen_nodes: 
                prev_node.next = curr_node.next 
                curr_node = prev_node 

            else: 
                seen_nodes.add(curr_node.val) 

            prev_node = curr_node 
            curr_node = curr_node.next 
            
        # return llist
        return head