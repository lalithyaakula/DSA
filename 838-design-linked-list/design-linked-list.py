class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:
    def __init__(self):
        self.head=None
    def get(self, index: int) -> int:
        curr=self.head
        count=0
        while curr:
            if count==index:
                return curr.val
            else:
                count+=1
                curr=curr.next
        return -1
    def addAtHead(self, val: int) -> None:
        new=Node(val)
        new.next=self.head
        self.head=new
    def addAtTail(self, val: int) -> None:
        new=Node(val)
        curr=self.head
        if curr==None:
            self.head=new
        else:
            while curr.next:
                curr=curr.next
            curr.next=new

    def addAtIndex(self, index: int, val: int) -> None:
        curr=self.head
        new=Node(val)
        count=0
        while curr:
            count+=1
            curr=curr.next
        if index==0:
            self.addAtHead(val)
            return
        elif index>count:
            return
        else:
            curr=self.head
            count=0
            while count!=index-1:
                curr=curr.next
                count+=1
            new.next=curr.next
            curr.next=new
    def deleteAtIndex(self, index: int) -> None:
        # Empty list
        if self.head is None:
            return

        # Delete head
        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        count = 0

        # Move to the (index - 1)th node
        while curr and count < index - 1:
            curr = curr.next
            count += 1

        # Invalid index
        if curr is None or curr.next is None:
            return

        # Delete the node
        curr.next = curr.next.next



            


