class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    def add_child(self, newNode):
        if newNode not in self._children:
            self._children.append(newNode)
            newNode.parent = self
        return

    def remove_child(self, newNode):
        if newNode in self._children:
            self._children.remove(newNode)
            newNode.parent = None
        return

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, newNode):
        if self._parent is newNode:
            return

        if self._parent is not None:
            self._parent.remove_child(self)
            
        self._parent = newNode
        if newNode is not None:
            newNode.add_child(self)
        return

    def depth_search(self, value):
        if self._value == value:
            return self
        elif len(self._children) != 0:
            for i in range(len(self._children)):
                node = self._children[i].depth_search(value)
                if node != None and node.value == value:
                    return node
        else:
            return None


    def breadth_search(self, value, q=[]):
        if self._value == value:
            return self
        elif len(self._children) != 0 or len(q) != 0:
            for i in range(len(self._children)):
                q.append(self._children[i])
            curr = q.pop(0)
            node = curr.breadth_search(value, q)
            if node != None and node.value == value:
                return node
        else:
            return None




# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)   