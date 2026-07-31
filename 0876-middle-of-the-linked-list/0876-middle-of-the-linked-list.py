# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            temp=temp.next
            count+=1
        
        count=count//2
        temp2=head
        while temp2:
            if count==0:
                return temp2
            else:
                temp2=temp2.next
                count-=1
        