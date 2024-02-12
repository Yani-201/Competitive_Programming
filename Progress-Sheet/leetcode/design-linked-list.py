class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
    
class MyLinkedList:

    def __init__(self):  
        self.head=None
        self.size=0
        # self.tail=self.head

    def get(self, index: int) -> int:
        current=self.head
        while current and index>0:
            current=current.next
            index-=1

        if current:
            return current.val
        return -1

    def addAtHead(self, val: int) -> None:
        temp=Node(val)
        temp.next=self.head
        self.head=temp
        # self.size+=1

    def addAtTail(self, val: int) -> None:
        temp=Node(val)
        current=self.head
        while current and current.next:
            current=current.next

        if current:
            current.next = temp
        else:
            self.head=temp

    def addAtIndex(self, index: int, val: int) -> None:
  
        dummy=Node(1)  
        dummy.next=self.head 
        current=dummy
        
        while current and index>0:
            current=current.next
            index-=1
        if not current:
            return

        temp=Node(val)  
        temp.next=current.next
        current.next=temp
        self.head=dummy.next
        

    def deleteAtIndex(self, index: int) -> None:
        dummy=Node(1)  
        dummy.next=self.head 
        current=dummy

        while index>0 and current:
            current=current.next
            index-=1

        if not current:
            return
        
        if current.next:
            current.next=current.next.next

        self.head=dummy.next


            
        


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)