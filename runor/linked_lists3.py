
class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        
        cur_node = self.head
        
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def len(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count

    def find_middle(self):
        length = self.len()
        middle_index = (length // 2) + 1
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1
            if count == middle_index - 1:
                print('middle_index',middle_index)
                return cur_node.data


class Solution:
    def middleNode(self, head):
        llist = LinkedList()
        for i in range(len(head)):
            llist.append(head[i])

        print('len',llist.len())
        print('>>>>', llist.find_middle())


Solution().middleNode([1,2,3,4,5,6,7,8])

