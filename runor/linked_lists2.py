
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
            return
        curr = self.head
        prev = None
        while curr != None:
            prev = curr
            curr = curr.next
        prev.next = Node(data)
        
    def print_list(self):
        curr = self.head
        string = ''
        while curr != None:
            prev = curr
            string += str(curr.val) + '-'
            curr = curr.next
        return string

    def insert_at_index(self, data, index): # 1,2,3,5
        count = 0
        curr = self.head # 1
        prev = None
        while curr != None:
            count += 1
            prev = curr
            curr = curr.next
            if count == index:
                prev.next = Node(data)
                prev.next.next = curr
                return

    def delete_at_node(self, index):
        count = 0
        curr = self.head
        prev = None
        if index == 0:
            tmps = curr.next
            self.head = tmps
            return
        while curr != None:
            count += 1
            prev = curr
            curr = curr.next
            if count == index:
                temp = curr.next
                prev.next = temp
                curr.next = None
                return

    def delete_node_by_val(self, node): # 12345
        curr = self.head
        prev =  None
        if node.val == curr.val:
            self.head = curr.next
            return
        while curr != None:
            if curr.val == node.val:
                tmp = curr.next
                prev.next = tmp
                curr.next = None
                return
            prev = curr
            curr = curr.next

    def swap_nodes(self, key_1, key_2): # 12345 ---> 24:::: 14325
        if key_1 == key_2:
            return
        curr  = self.head
        x , y = None , None # Assign None to avoid reference error
        while curr :
            if curr.val == key_1:
                x = curr # key_1 found
            if curr.val == key_2:
                y =curr # key_2 found
            curr = curr.next
        
        if x and y: # Check if both key's exist
            x.val , y.val = y.val , x.val
        else : 
            return

    def reverse_iterative(self):
        prev = None 
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt 
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(5)

# ll.insert_at_index(4, 3)
# print(ll.print_list())
# ll.delete_at_node(0)
# ll.delete_node_by_val(Node(2))
# ll.swap_nodes(2,5)
# ll.reverse_iterative()
# print(ll.print_list())

ll.reverse_recursive()
print(ll.print_list())




# tmp1 = curr # 4
# node1_prev.next = tmp1
# tmp1.next = node1.next

# tmp2 = no
# node1.next = curr.next
# prev.next = node1
# curr.next = node1.next

# tmp1 = curr # 4
# node1_prev.next = tmp1
# tmp1.next = node1.next

# tmp2 = no
# node1.next = curr.next
# prev.next = node1
