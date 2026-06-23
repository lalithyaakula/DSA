
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1=headA
        curr2=headB
        len1,len2=0,0
        while curr1:
                len1+=1
                curr1=curr1.next
        while curr2:
                len2+=1
                curr2=curr2.next
        diff=abs(len1-len2)
        curr1=headA
        curr2=headB
        while diff:
            if len1>len2:
                curr1=curr1.next
                diff-=1
            else:
                curr2=curr2.next
                diff-=1
        while curr1 and curr2:
            if curr1==curr2:
                return curr1
            else:
                curr1=curr1.next
                curr2=curr2.next