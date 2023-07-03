class Node:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


class Tree:
    def __init__(self):
        self.root = None

    def search_and_create_node(self, node, source, left, right):
        if node:
            if node.val == source:
                if left:
                    node.left = Node(None, None, left)
                if right:
                    node.right = Node(None, None, right)
                return True
            else:
                if self.search_and_create_node(
                    node.left, source, left, right
                ) or self.search_and_create_node(node.right, source, left, right):
                    return


class TreeTraversal:
    def __init__(self):
        self.preorder = []
        self.inorder = []
        self.postorder = []
        self.iterative_preorder = []
        self.iterative_inorder = []
        self.iterative_postorder = []

    def pre_order_traversal(self, node):
        if not node:
            return
        self.preorder.append(node.val)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if not node:
            return
        self.in_order_traversal(node.left)
        self.inorder.append(node.val)
        self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if not node:
            return
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        self.postorder.append(node.val)

    def iterative_preorder_traversal(self, root):
        stack = []
        node = root
        while node or len(stack) > 0:
            while node:
                self.iterative_preorder.append(node.val)
                if node.right:
                    stack.append(node.right)
                node = node.left
            if not node and len(stack) > 0:
                node = stack.pop()

    def iterative_inorder_traversal(self, root):
        stack = []
        node = root
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                self.iterative_inorder.append(node.val)
                node = node.right

    def iterative_postorder_traversal(self, root):
        stack = []
        node = root
        prev_node = None
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]
            if node.right and node.right.val != prev_node.val:
                node = node.right
                prev_node = node
            else:
                prev_node = stack.pop()
                self.iterative_postorder.append(prev_node.val)
                node = None


def main():
    tree = Tree()
    tree.root = Node(None, None, 10)
    tree.search_and_create_node(tree.root, 10, 9, 17)
    tree.search_and_create_node(tree.root, 9, 5, 12)
    tree.search_and_create_node(tree.root, 17, 15, 22)
    tree.search_and_create_node(tree.root, 5, 3, 1)
    tree.search_and_create_node(tree.root, 22, 16, 23)
    tree.search_and_create_node(tree.root, 3, 19, None)
    tree.search_and_create_node(tree.root, 19, 11, None)

    traversal = TreeTraversal()
    traversal.pre_order_traversal(tree.root)
    traversal.in_order_traversal(tree.root)
    traversal.post_order_traversal(tree.root)

    print(f"Pre-order: {traversal.preorder}")
    print(f"In-order: {traversal.inorder}")
    print(f"Post-order: {traversal.postorder}")

    traversal.iterative_preorder_traversal(tree.root)
    traversal.iterative_inorder_traversal(tree.root)
    traversal.iterative_postorder_traversal(tree.root)
    print(f"Iterative pre-order: {traversal.iterative_preorder}")
    print(f"Iterative in-order: {traversal.iterative_inorder}")
    print(f"Iterative post-order: {traversal.iterative_postorder}")


if __name__ == "__main__":
    main()
