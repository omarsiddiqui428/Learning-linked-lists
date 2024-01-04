#help from Chat GPT here 

class Node:
    # data, the location of the next Node
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self): #just needed to initialize a linked list. "Constructor"
        self.head = None #Initalizing the list like list = []

    def print_list(self): #I understand this
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next #TODO- current_node.next is just a build in way to go to the next node right?
            #.next is a pointer
            #all objects are just memory locations

    def append(self, data):
        new_node = Node(data) #this is calling the init function for the Node class. Command + Click will take you to what it's calling which is the init functoin for the Node class
        #Node(data), calling the class like a function, the class is the blueprint, this is an object which is an instance of a class
        if self.head is None:
            self.head = new_node
            return
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next #TODO: gettint to the last node here right, and then take the next one which is unfilled to add the new data
            # at this point last_node is the last element of the LL
            last_node.next = new_node

    def get(self,node_number):
        current_node = self.head
        index = 0
        while current_node:
            if index == node_number:
                return current_node.data
            index += 1
            current_node = current_node.next
        return None


    def prepend(self,data):
        #Does knowing how to do this come from experience?
        #Super confused at this structure
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self,node_number):
        current_node = self.head
        if node_number == 0:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        index = 0
        while current_node and index != node_number:
            prev_node = current_node
            current_node = current_node.next
            index += 1

        if current_node is None:
            return

        prev_node.next = current_node.next
        current_node = None

x = LinkedList()

for i in range(10):
    x.append(i) # TODO: this is making a linked list 1,2,3,4,5,6,7,8,9where there's that forced order right?
    #TODO- so in print, do Linked lists look the same as regular lists?
    #TODO- can we look at an example of code where this is implemented?
    #TODO- can I get a small linked list project for next time so I can start practicing with this data structure?

x.print_list()

# Getting an element at a specific index
element = x.get(3)
print("Element at index 3:", element)

# Prepending an element to the list
x.prepend(100)
print("After prepending 100:")
x.print_list()

# Removing an element at a specific index
x.remove(5)
print("After removing element at index 5:")
x.print_list()
