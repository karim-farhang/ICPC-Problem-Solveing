# A naive recursive implementation of
# Largest Independent Set problem

# A utility function to find
# max of two integers
def max(x, y):
    if (x > y):
        return x
    else:
        return y


# A binary tree node has data,
# pointer to left child and a
# pointer to right child
class node:
    def __init__(self):
        self.data = 0
        self.left = self.right = None


# The function returns size of the
# largest independent set in a given
# binary tree
def LISS(root):
    if (root == None):
        return 0

    # Calculate size excluding the current node
    size_excl = LISS(root.left) + LISS(root.right)

    # Calculate size including the current node
    size_incl = 1
    if (root.left != None):
        size_incl += LISS(root.left.left) + \
                     LISS(root.left.right)
    if (root.right != None):
        size_incl += LISS(root.right.left) + \
                     LISS(root.right.right)

    # Return the maximum of two sizes
    return max(size_incl, size_excl)


# A utility function to create a node
def newNode(data):
    temp = node()
    temp.data = data
    temp.left = temp.right = None
    return temp


# Driver Code

# Let us construct the tree
# given in the above diagram
root = newNode(20)
root.left = newNode(8)
root.left.left = newNode(4)
root.left.right = newNode(12)
root.left.right.left = newNode(10)
root.left.right.right = newNode(14)
root.right = newNode(22)
root.right.right = newNode(25)
print("size of Largest Independent Set is ", LISS(root))
