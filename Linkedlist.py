class ListNode:
    def __init__(self,value,link=None) -> None:
        self.value = value
        self.link = link
        
class LinkedlList:
    def __init__(self) -> None:
        self._head = None
        self.N = 0
        
    def add(self,value):
        """
        Paramters 
        ---------
        Value: any
           Add a new node to the begining with this value
        
        """
        new_node = ListNode(value)
        head_before = self._head
        self._head = new_node
        new_node.next = head_before
        self.N += 1
    def add_last(self,value):
        new_node = ListNode(value)
        node = self._head
        while node.next:
            node = node.next
        node.next = new_node
        self.N += 1
    def remove_first(self):
        """ 
        Rmove and return the first value from the linked list or 
        do nothing and return None if it is alredy empty 
        """
        ret = None
        if self._head:
            ret = self._head.value
            head = self._head.next 
            self.N -= 1
        return ret
            
            
    def __str__(self) -> str:
        s = "LinkedList"
        node = self._head
        while node:
            s += "{} ==> ".format(node.value)
            node = node.next
        return s 
    def __len__(self):
        return self.N
            
            
L = LinkedlList()
L.add(20)
L.add(10)
L.add("Tesfaye")
L.add("Naramo")
print(L)
print(len(L))
print(L.remove_first())
print(L)
print(len(L))