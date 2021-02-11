class CircularLinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
            node.next = self.head

    def __repr__(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        nodes = [starting_point]

        while node is not None and (node.next != starting_point):
            node = node.next
            nodes.append(node)

        node = node.next
        nodes.append(node)

        nodes = map(str, nodes)
        return " -> ".join(nodes)

    def major_scale(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        nodes = [starting_point]

        major_interval = ["W", "W", "H", "W", "W", "W", "H"]

        for interval in major_interval:
            if interval == "W":
                node = node.next.next
                nodes.append(node)
            elif interval == "H":
                node = node.next
                nodes.append(node)
            else:
                print("Error")

        nodes = map(str, nodes)
        return " -> ".join(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
