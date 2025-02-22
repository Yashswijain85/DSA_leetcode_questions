class Node:
  def __init__(self, data):
    # Creation of Node 
    self.data = data 
    self.nextPtr = None 
# self --> tells us that on which object I am referring to at that point of time 
class LinkedList:
  # linked list initialization
  def __init__(self):
    self.head = None 
  
  def insertAtBeginning(self, new_data): 
    new_node = Node(new_data)
    new_node.nextPtr = self.head 
    self.head = new_node 
  
  def printLL(self): 
    temp = self.head 
    while(temp): 
      print(temp.data, end = " ")
      temp = temp.nextPtr
  
  def insertAtEnd(self,new_data):
    new_node = Node(new_data) 
    temp = self.head 
    while temp.nextPtr:
      temp = temp.nextPtr
    temp.nextPtr = new_node
  
  # function to insert new_data after a particular node 
  def insertAfterNode(self, prev_node, new_data):
    if prev_node is None:
      print("Error : Given node must be available inside the linked list")
      return 
    
    new_node = Node(new_data)
    new_node.nextPtr = prev_node.nextPtr 
    prev_node.nextPtr = new_node 

  # function to count the total no. of nodes in a given linked list 
  def countNodes(self): 
    count = 0 
    temp = self.head 
    while temp: 
      count += 1
      temp = temp.nextPtr 
    print("\n")
    return count 

  # function to search for a given data in a Linkedlist, if the data is available return true otherwise false 
  def searchNode(self, nodeData):
    if self.head is None: 
      return False 

    temp = self.head
    while temp:
      if temp.data == nodeData:
        return True 
      temp = temp.nextPtr
    return False


linkedlist1 = LinkedList()
linkedlist1.insertAtBeginning(10)
linkedlist1.insertAtBeginning(20)
linkedlist1.insertAtBeginning(30)
linkedlist1.insertAtEnd(40)
linkedlist1.insertAtEnd(50)
linkedlist1.insertAtEnd(60)
linkedlist1.insertAfterNode(linkedlist1.head.nextPtr.nextPtr, 70)
linkedlist1.printLL() 
print("Count : ",linkedlist1.countNodes())
# function call for searchNode()
nodeData = 50
if(linkedlist1.searchNode(nodeData)):
  print("Data is available in the given linkedlist")
else:
  print("Data is not available in the given linkedlist")
