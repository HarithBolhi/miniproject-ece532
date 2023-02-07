import json


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    # Return True if the element is in the tree
    def search(self, d):
        current = self.root  # Start from the root
        while current != None:
            if d < current.element2:
                current = current.left
            elif d > current.element2:
                current = current.right
            else:  # element2 matches current.element2
                return True  # element2 is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, a, b, c, d, e):
        if self.root == None:
            self.root = self.createNewNode(a, b, c, d, e)  # Create a new root
        else:
            # Locate the parent node
            parent = None
            current = self.root
            while current != None:
                if c < current.element2:
                    parent = current
                    current = current.left
                elif c > current.element2:
                    parent = current
                    current = current.right
                else:
                    return False  # Duplicate node not inserted

            # Create the new node and attach it to the parent node
            if c < parent.element2:
                parent.left = self.createNewNode(a, b, c, d, e)
            else:
                parent.right = self.createNewNode(a, b, c, d, e)

        self.size += 1  # Increase tree size
        return True  # element2 inserted

    # Create a new TreeNode for element2 e
    def createNewNode(self, a, b, c, d, e):
        return TreeNode(a, b, c, d, e)

    # Return the size of the tree
    def getSize(self):
        return self.size

    # Inorder traversal from the root
    def inorder(self):
        self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
        if r != None:
            self.inorderHelper(r.left)
            print(r.element3, end="\n")
            self.inorderHelper(r.right)

    # Postorder traversal from the root
    def postorder(self):
        self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
        if root != None:
            self.postorderHelper(root.left)
            self.postorderHelper(root.right)
            print(root.element3, end="\n")

    # Preorder traversal from the root
    def preorder(self):
        self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
        if root != None:
            print(root.element3, end="\n")
            self.preorderHelper(root.left)
            self.preorderHelper(root.right)

    # Returns a path from the root leading to the specified element2
    def path(self, c):
        list = []
        current = self.root  # Start from the root

        while current != None:
            list.append(current)  # Add the node to the list
            if c < current.element2:
                current = current.left
            elif c > current.element2:
                current = current.right
            else:
                break

        return list  # Return an array of nodes

    # Delete an element2 from the binary search tree.
    # Return True if the element2 is deleted successfully
    # Return False if the element2 is not in the tree
    def delete(self, c):
        # Locate the node to be deleted and its parent node
        parent = None
        current = self.root
        while current != None:
            if c < current.element2:
                parent = current
                current = current.left
            elif c > current.element2:
                parent = current
                current = current.right
            else:
                break  # element2 is in the tree pointed by current

        if current == None:
            return False  # element2 is not in the tree

        # Case 1: current has no left children
        if current.left == None:
            # Connect the parent with the right child of the current node
            if parent == None:
                self.root = current.right
            else:
                if c < parent.element2:
                    parent.left = current.right
                else:
                    parent.right = current.right
        else:
            # Case 2: The current node has a left child
            # Locate the rightmost node in the left subtree of
            # the current node and also its parent
            parentOfRightMost = current
            rightMost = current.left

            while rightMost.right != None:
                parentOfRightMost = rightMost
                rightMost = rightMost.right  # Keep going to the right

            # Replace the element2 in current by the element2 in rightMost
            current.element2 = rightMost.element2

            # Eliminate rightmost node
            if parentOfRightMost.right == rightMost:
                parentOfRightMost.right = rightMost.left
            else:
                # Special case: parentOfRightMost == current
                parentOfRightMost.left = rightMost.left

        self.size -= 1
        return True  # element2 deleted

    # Return true if the tree is empty
    def isEmpty(self):
        return self.size == 0

    # Remove all elements from the tree
    def clear(self):
        self.root == None
        self.size == 0

    # Return the root of the tree
    def getRoot(self):
        return self.root

    def read1_list(self):
        # for reading also binary mode is important
        with open('Num.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list

    def read2_list(self):
        # for reading also binary mode is important
        with open('ActiveHour.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list

    def read3_list(self):
        # for reading also binary mode is important
        with open('Frequency.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list

    def read4_list(self):
        # for reading also binary mode is important
        with open('StationName.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list

    def read5_list(self):
        # for reading also binary mode is important
        with open('TrainType.json', 'rb') as fp:
            n_list = json.load(fp)
            return n_list


class TreeNode:
    def __init__(self, a, b, c, d, e):
        self.element = a, b, c, d, e
        self.element2 = d
        self.element3 = c, b, d, e
        self.left = None  # Point to the left node, default None
        self.right = None  # Point to the right node, default None
