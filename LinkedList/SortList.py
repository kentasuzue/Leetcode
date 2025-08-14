"""
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        values=[]

        ptr = head
        while ptr:
            values.append(ptr.val)
            ptr=ptr.next
        
        if len(values) <= 1:
            return head
        
        values = sorted(values)
        print(values)

        head=ListNode(values[0])
        ptr=head

        for i in range(1, len(values)):
            newNode = ListNode(values[i])
            ptr.next = newNode
            ptr = ptr.next
        
        return head
        

