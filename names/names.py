import time

#binary search tree
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # print(f"value: {value}")
        if value < self.value:  #checks if smaller, go left
        # go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            #go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            #go left
            if not self.left:
                return False
            else:
                #recursion
                return self.left.contains(target)

        else:  #target is >= self.value
            #go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        #recursion
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    # def for_each(self, cb):
    #     cb(self.value)

    #     if self.left:
    #         self.left.for_each(cb)
    #     if self.right:
    #         self.right.for_each(cb)

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
# print(names_1)
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

#this implementation is creating two loops which has a really bad runtime given the objectives. it creates a big loop and then an inner loop and churns through those comparing value to value for each loop and then appending to a list. my goal is to improve the efficiency using a binary search tree
duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

#we need to set up a bst
bst = BinarySearchTree(names_1[0])
# print(names_1[0])
for x in names_1[1:]:
    #print(x)
    bst.insert(x)
#this is going to load up the names into the bst binary search tree
    
# for x in bst:
#     print(x)

for y in names_2:
    if bst.contains(y):
        duplicates.append(y)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# class BinarySearchTreeTests(unittest.TestCase):
#     def setUp(self):
#         self.bst = BinarySearchTree(5)

    # def test_contains(self):
    #     self.bst.insert(2)
    #     self.bst.insert(3)
    #     self.bst.insert(7)
    #     self.assertTrue(self.bst.contains(7))
    #     self.assertFalse(self.bst.contains(8))

#need to modify my bst class to compare values of similarity in strings not numbers?