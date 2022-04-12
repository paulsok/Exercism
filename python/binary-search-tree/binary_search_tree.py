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
            self.left.get_sorted(sorted_data)
        sorted_data.append(self.data)
        if self.right:
            self.right.get_sorted(sorted_data)
        return sorted_data


class BinarySearchTree:
    def __init__(self, tree_data):
        pass

    def data(self):
        pass

    def sorted_data(self):
        pass
