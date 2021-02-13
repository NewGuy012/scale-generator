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
        return "Chromatic scale: " + " -> ".join(nodes) + "\n"

    def generate_scale(self, starting_note=None, scale_type=None):
        starting_node = self.node_dict[starting_note]
        self.head = starting_node

        node = starting_node
        nodes = [starting_node]

        scale_interval = {
            "major": ["W", "W", "H", "W", "W", "W", "H"],
            "minor": ["W", "H", "W", "W", "H", "W", "W"],
            # all the modal scales
            "ionian": ["W", "W", "H", "W", "W", "W", "H"],
            "dorian": ["W", "H", "W", "W", "W", "H", "W"],
            "phrygian": ["H", "W", "W", "W", "H", "W", "W"],
            "lydian": ["W", "W", "W", "H", "W", "W", "H"],
            "mixolydian": ["W", "W", "H", "W", "W", "H", "W"],
            "aeolian": ["W", "H", "W", "W", "H", "W", "W"],
            "locrian": ["H", "W", "W", "H", "W", "W", "W"],
            # note, ionian is major, aeolian is minor
            "pentatonic": ["W", "W", "WH", "W", "WH"],
            "fourths": ["WWH"] * 12,
            "fifths": ["WWWH"] * 12,
            "relative minor": ["WWWWH"],
        }
        scale_interval = scale_interval.get(scale_type)

        node_interval = {
            "H": 1,
            "W": 2
        }

        for interval in scale_interval:
            num_steps = 0

            for c in interval:
                num_steps += node_interval.get(c)

            for i in range(0, num_steps):
                node = node.next

            nodes.append(node)

        nodes = map(str, nodes)
        nodes_str = " -> ".join(nodes)
        output_str = starting_note \
            + " " \
            + scale_type.title() \
            + " scale: " \
            + nodes_str
        print(output_str)

    def generate_chord(self, starting_note=None, chord_scale=None, chord_type=None):
        starting_node = self.node_dict[starting_note]
        self.head = starting_node
        node = starting_node
        nodes = [starting_node]

        scale_interval = {
            "major": ["W", "W", "H", "W", "W", "W", "H"],
            "minor": ["W", "H", "W", "W", "H", "W", "W"],
            "dominant": ["W", "W", "H", "W", "W", "H"],
            "diminished": ["W", "H", "H", "W"],
            "augmented": ["W", "W", "W", "W"],
        }
        scale_interval = scale_interval.get(chord_scale)

        node_interval = {
            "H": 1,
            "W": 2
        }

        for interval in scale_interval:
            num_steps = 0

            for c in interval:
                num_steps += node_interval.get(c)

            for i in range(0, num_steps):
                node = node.next

            nodes.append(node)

        chord_construction = {
            "triad": [x - 1 for x in [1, 3, 5]],
            "sus2": [x - 1 for x in [1, 2, 5]],
            "sus4": [x - 1 for x in [1, 4, 5]],
            "6": [x - 1 for x in [1, 3, 5, 6]],
            "7": [x - 1 for x in [1, 3, 5, 7]],
            "9": [x - 1 for x in [1, 3, 5, 7, 9]],
            "11": [x - 1 for x in [1, 3, 5, 7, 9, 11]],
            "13": [x - 1 for x in [1, 3, 5, 7, 9, 11, 13]]
        }

        nodes = [nodes[i] for i in chord_construction.get(chord_type)]
        nodes = map(str, nodes)
        nodes_str = " -> ".join(nodes)
        output_str = starting_note \
            + " " \
            + chord_scale \
            + " " \
            + chord_type \
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
