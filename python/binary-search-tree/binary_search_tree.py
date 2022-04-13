class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        msg = 'TreeNode(data={}, left={}, right={})'
        return msg.format(self.data, self.left, self.right)

    def insert(self, data):
        if data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = TreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = TreeNode(data)

    def sorted_re(self, sorted_data=[]):
        if self.left:
            self.left.sorted_re(sorted_data)
        sorted_data.append(self.data)
        if self.right:
            self.right.sorted_re(sorted_data)
        return sorted_data


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for data in tree_data[1:]:
            self.root.insert(data)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.root.sorted_re([])
