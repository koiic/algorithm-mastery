
class Node:
    def __init__(self, data):
        self.data = data
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
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def count_occurences(self, data):
        curr = self.head
        prev = None
        count = 0
        while curr != None:
            if curr.data == data:
                count += 1
            prev = curr
            curr = curr.next
        return count

    # def rotate(self, data):
    #     curr = self.head
    #     prev = None
    #     tmp = None
    #     if curr.data == data:
    #         cur_node = curr
    #         while cur_node:
    #             print(cur_node.data)
    #             cur_node = cur_node.next
    #         return curr
    #     while curr != None:
    #         if curr.data == data:
    #             prev.next = None
    #             tmp = curr
    #         prev = curr
    #         curr = curr.next
    #     # self.head = 
    #     prev.next = self.head
    #     cur_node = tmp
    #     while cur_node:
    #         print(cur_node.data)
    #         cur_node = cur_node.next
    #     return prev

    def rotate(self, data):
        curr = self.head
        prev = None
        tmp = None
        if curr.data == data:
            cur_node = curr
            while cur_node:
                print(cur_node.data)
                cur_node = cur_node.next
            return curr
        while curr != None:
            if curr.data == data:
                self.head = curr
                prev.next = None

                prev = self.head
                curr = curr.next
                continue
                # tmp = curr
            prev = curr
            curr = curr.next
        # self.head = 
        prev.next = self.head
        print(self.head.next.next.data)
        cur_node = prev
        while cur_node:
            # print(cur_node.data)
            cur_node = cur_node.next
        return prev

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

# print(ll.print_list())
# print(ll.count_occurences(1))
print(ll.rotate(5))