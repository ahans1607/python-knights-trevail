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
        if self._value == value


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)   