"""
A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class. RingBuffer has two methods, append and get. The append method adds elements to the buffer. The get method returns all of the elements in the buffer in a list in their given order. It should not return any None values in the list even if they are present in the ring buffer.
"""

# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity #ask about how this works exactly. oh. this is the way of building out a memory efficient list. preallocating resources. duh.

  def append(self, item):
    #The append method adds elements to the buffer.
    #think out the plan:
    #append is meant to add an item to the buffer. this will need to use storage (above). if we append an item to the buffer, we need to make sure we know whether or not the buffer is at it's capacity because ring buffers are of a fixed size (capacity above). This is why they begin to overlap and overwrite values that are added. "current" will serve as our count to measure how many items are currently in the ring buffer. Sound good?
    print(f"self: {self}, item: {item}")
    print(f"before: self.storage, {self.storage}, item: {item}")
    self.storage[self.current] = item
    print(f"after: self.storage, {self.storage}, item: {item}")
    #okay this is setting the first item in the buffer and overwriting it like so
    # before: self.storage, ['a', None, None, None, None], item: b
    # after: self.storage, ['b', None, None, None, None], item: b
    #need to update current because we are adding an item upon invoking this method
    self.current += 1
    #now we see
    # before: self.storage, ['a', 'b', 'c', None, None], item: d
    # after: self.storage, ['a', 'b', 'c', 'd', None], item: d
    #compare?
    if self.current == self.capacity:
      print(f"wwwwww")
      print(f"self.current: {self.current}, self.capacity: {self.capacity}")  #this is not firing -- it is actually firing, you just can't see it because of how the tests run.
      #we need to compare to reinitialize the beginning of where items should be put in to the buffer because we are at capacity, so next time this runs, it will insert where the first "oldest" one was from the previous "filling up" of the buffer. i think. test is failing.
      self.current = 0
    pass
    

  def get(self):
    #The get method returns all of the elements in the buffer in a list in their given order. It should not return any None values in the list even if they are present in the ring buffer.
    #this needs to return a list but have a condition of a given value being "is not "None" it seems.
    #print(f"self.storage: {self.storage}")
    for x in self.storage:
      print(x)
      # a
      # b
      # c
      # d
      # None
      # F
    #this is not right because 1. we have a none and 2. there are 6 items, and it's missing the E from the test. We need to return our list of everything except the Nones
    return [x for x in self.storage if x is not None]
    #i just really got the feeling of python being an "English" language
    # f
    # g
    # h
    # i
    # e
    # .
    #test passes now but why is it spitting out a period at the end?
    pass