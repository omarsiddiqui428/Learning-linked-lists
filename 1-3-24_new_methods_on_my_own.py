#On my own: adding get, remove, and prepend. Basically only got the logic, struggling with the actual code 
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
        node_count = 0
        # when node_count = node_number, then print the data of that node

    def prepend(self,data):
        new_node = Node(data)
        last_node = last_node.next
        #everything has to move over one node, and then the node with the new data can be added at the beginning


    def remove(self,node_number):
        #remove the specified node
        #does everything then have to change places?

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

#TODO- Write a "get" method to get any element in the list
#TODO- write prepend and remove method
#TODO- write a main method where you create list, print stuff out, and edit lists
