

class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:

    def __init__(self) -> None:
        self.root = Node()

    def add(self, value: int) -> None:
        if not self.root.value:
            self.root.value = value
            return
        nextNode = self.root
        while True:
            if value <= nextNode.value:
                if not nextNode.left:
                    nextNode.left = Node(value)
                nextNode = nextNode.left   
                break                     
            else:
                if not nextNode.right:
                    nextNode.right = Node(value)
                nextNode = nextNode.right
                break


tree = Tree()
tree.add(1)
tree.add(2)
tree.add(0)
