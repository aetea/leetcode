# problem https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # --- set starting position ---
        curr_node = head
        prev_node = None
        
        # --- loop thru llist till the end ---
        while curr_node != None: 
            if curr_node.next == None:
                head = curr_node
            
            # --- reverse all pointers ---
            # save current.next in a new variable
            next_node = curr_node.next
            # update current.next to point to prev node
            # if no prev node, then current.next points to nothing
            curr_node.next = prev_node
            
            # --- update position tracker ---
            prev_node = curr_node 
            curr_node = next_node 
          
        return head

    