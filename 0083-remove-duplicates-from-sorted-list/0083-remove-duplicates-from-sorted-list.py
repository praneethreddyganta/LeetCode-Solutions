# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        seen=set()
        current=head
        prev= None
        while current:
            if current.val not in seen:
                seen.add(current.val)
                prev=current 
                

            else:
                prev.next=current.next
            current=current.next   
        return head