class CircularLinkedList:
    def __init__(self, node_str=None):
        self.head = None
        self.node_dict = {}

        if node_str is not None:
            node = Node(data=node_str[0])
            self.head = node
            self.node_dict[node_str[0]] = node

            for elem in node_str[1:]:
                node.next = Node(data=elem)
                node.next.previous = node
                node = node.next
                self.node_dict[elem] = node

            node.next = self.head

    def __repr__(self):
        starting_node = self.head
        node = starting_node
        nodes = [node]

        while node is not None and (node.next != starting_node):
            node = node.next
            nodes.append(node)

        node = node.next
        nodes.append(node)

        nodes = map(str, nodes)
        return " -> ".join(nodes)

    def generate_scale(self, starting_note=None, scale_type=None):
        if starting_note is None:
            starting_node = self.head
        else:
            starting_node = self.node_dict[starting_note]

        node = starting_node
        nodes = [starting_node]

        scale_interval = {
            "major": ["W", "W", "H", "W", "W", "W", "H"],
            "minor": ["W", "H", "W", "W", "H", "W", "W"],
            "pentatonic": ["W", "W", "WH", "W", "WH"],
            "fourths": ["WWH"] * 12,
            "fifths": ["WWWH"] * 12,
            "relative minor": ["WWWWH"],
            "major chord": ["WW", "WH"],
            "minor chord": ["WH", "WW"]
        }
        scale_interval = scale_interval.get(scale_type)

        node_interval = {
            "H": 1,
            "W": 2,
            "WH": 3,
            "WW": 4,
            "WWH": 5,
            "WWWH": 7,
            "WWWWH": 9,
        }

        for interval in scale_interval:
            num_steps = node_interval.get(interval)

            for i in range(0, num_steps):
                node = node.next
            nodes.append(node)

        nodes = map(str, nodes)
        nodes_str = " -> ".join(nodes)
        output_str = starting_note \
            + " " \
            + scale_type \
            + ": " \
            + nodes_str
        print(output_str)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data
