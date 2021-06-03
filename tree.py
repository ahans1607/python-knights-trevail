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
        # if self._parent is not newNode:
            # if self._parent:
            #     self._parent.remove_child(newNode)

        self._parent = newNode
        if newNode is not None:
            newNode.add_child(self)
        return


    