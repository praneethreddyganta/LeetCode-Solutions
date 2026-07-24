# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        counter=0      
        while temp:
            temp=temp.next
            counter+=1
        curr=head
        prev=None
        n1=counter-n+1
        if n1==1:
            return head.next
        count=1
        while curr and count<n1:
            prev=curr
            curr=curr.next
            count+=1
        if curr:
            prev.next=curr.next
        return head

        