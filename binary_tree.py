

class BinaryNode(object):
    """Node of a BinaryTree"""

    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_left_child(self, left_child):
        self.left_child = left_child
        return self

    def set_right_child(self, right_child):
        self.right_child = right_child

    def insert_left(self, new_node):
        if self.left_child is not None:
            left_child = self.left_child
            self.set_left_child(new_node)
            new_node.set_left_child(left_child)
        else:
            self.set_left_child(new_node)

        return self

    def insert_right(self, new_node):
        if self.right_child is not None:
            right_child = self.right_child
            self.set_right_child(new_node)
            new_node.set_right_child(right_child)
        else:
            self.set_left_child(new_node)

        return self

    def breadth_first_traversal(self):

        if self.data is None:
            return

        breadth_queue = Queue.new(self)

        while breadth_queue.isEmpty == False:
            current_node = breadth_queue.dequeue()
            print current_node

            if current_node.get_left_child() is not None:
                breadth_queue.enqueue(self.get_left_child())

            if current_node.get_right_child() is not None:
                breadth_queue.enqueue(self.get_right_child())


    def depth_first_traversal_preorder(self):

        if self == None:
            return

        print(self)
        depth_first_traversal_preorder(self.get_left_child)
        depth_first_traversal_preorder(self.get_right_child)


    def depth_first_traversal_inorder(self):

        if self == None:
            return

        depth_first_traversal_preorder(self.get_left_child)
        print(self)
        depth_first_traversal_preorder(self.get_right_child)

    def depth_first_traversal_postorder(self):

        if self == None:
            return

        depth_first_traversal_preorder(self.get_left_child)
        depth_first_traversal_preorder(self.get_right_child)
        print(self)
