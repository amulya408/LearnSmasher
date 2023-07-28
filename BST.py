class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        else:
            # If the key is equal to the root's key, insert it to the right subtree
            root.right = self._insert_recursive(root.right, key)

        return root

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self._find_min(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)

        return root

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)

    def display_tree(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self, root):
        if root:
            self._inorder_traversal(root.left)
            print(root.key, end=" ")
            self._inorder_traversal(root.right)


# Test the BinarySearchTree implementation
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insertion
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bst.insert(40)  # Duplicate entry

    # Display the tree using Inorder Traversal (sorted order)
    print("Inorder Traversal:")
    bst.display_tree()  

    # Search
    key_to_search = 40
    result = bst.search(key_to_search)
    if result:
        print(f"{key_to_search} found in the tree.")
    else:
        print(f"{key_to_search} not found in the tree.")

    # Deletion
    key_to_delete = 30
    bst.delete(key_to_delete)

    # Display the updated tree after deletion
    print("Inorder Traversal after Deletion:")
    bst.display_tree()  
