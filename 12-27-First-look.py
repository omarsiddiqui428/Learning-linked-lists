class Node:
    # data, the location of the next Node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self): #just needed to initialize a linked list
        self.head = None #TODO- what is this?

    def print_list(self): #I understand this
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next #TODO- current_node.next is just a build in way to go to the next node right?

    def append(self, data):
        new_node = Node(data) #TODO- what is node(data) doing here?
        if self.head is None:
            self.head = new_node
            return
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next #TODO: gettint to the last node here right, and then take the next one which is unfilled to add the new data
            # at this point last_node is the last element of the LL
            last_node.next = new_node

    # find function - return the Node Object. Not just the element it stores.
    # prepend function - instead of adding to the end of the list, add to the beginning (think about moving the head)
    # remove function - if you remove from the middle of the list, the previous element should now point to the one after the removed element


x = LinkedList()

for i in range(10):
    x.append(i) # TODO: this is making a linked list 1,2,3,4,5,6,7,8,9where there's that forced order right?
    #TODO- so in print, do Linked lists look the same as regular lists?
    #TODO- can we look at an example of code where this is implemented?
    #TODO- can I get a small linked list project for next time so I can start practicing with this data structure?

x.print_list()
