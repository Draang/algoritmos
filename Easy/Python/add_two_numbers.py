
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currentNodel1=l1
        currentNodel2=l2
        string1=''
        string2=''
        while currentNodel1 is not None:
            v=currentNodel1.val
            string1=string1+str(v)
            currentNodel1=currentNodel1.next
        while currentNodel2 is not None:
            v=currentNodel2.val
            string2=string2+str(v)
            currentNodel2=currentNodel2.next
        first=None
        prev=None
        for i in str(int(string1[::-1])+int(string2[::-1]))[::-1]:
            node=ListNode(int(i))
            if first is None:
                
                first=node
                prev=first
            else:
                prev.next=node
                prev=node
        return first