class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False


    # # reference to the next node in the list
    # self.next_node = next_node


  def reverse_list(self):
    # TO BE COMPLETED
    #need to set up a current, next, and prev. prev isn't there because this isn't a dll.
    current = self.head
    next = None
    previous = None

    while current is not None:
      # print(f"current.value: {current.value}, current.next_node: {current.next_node.value} ") #this breaks
      next = current.next_node
      current.next_node = previous #switch
      previous = current #swap
      current = next #another swap
      self.head = previous
    pass

    # cur = self
    # new = cur.next
    # cur.next = None
    # while new != None:
    # prev = cur
    # cur = new
    # new = cur.next
    # cur.next = prev

  #  prev = None
  #  current = listHead
  #  next = listHead.next
  
  #  while current:
  #      next = current.next
  #      current.next = prev
  #      prev = current
  #      current = next
  #  listhead = prev