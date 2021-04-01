from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return self.data


class CircularDoublyLinkedList:
    def __init__(self, data=None, starting_data=None):
        nodes = [Node(item) for item in data]

        starting_index = data.index(starting_data)
        self.head = nodes[starting_index]

        for current_node, next_node in pairwise(nodes):
            current_node.next = next_node
            next_node.prev = current_node

        nodes[0].prev = nodes[-1]
        nodes[-1].next = nodes[0]

    def __repr__(self):
        node = self.head
        nodes = []

        while node.next != self.head:
            nodes.append(node.data)
            node = node.next

        nodes.append(node.data)

        return " -> ".join(nodes)


class MusicalScale:
    chromatic_notes = ["C", "C#/Db",     "D", "D#/Eb",
                       "E",     "F", "F#/Gb",     "G",
                       "G#/Ab", "A", "A#/Bb",     "B"]

    step_intervals = {
        "H": 1,
        "W": 2
    }

    scale_intervals = {
        "major": ["W", "W", "H", "W", "W", "W", "H"],
        "minor": ["W", "H", "W", "W", "H", "W", "W"],

        "dominant":   ["W", "W", "H", "W", "W", "H"],
        "diminished": ["W", "H", "H", "W"],
        "augmented":  ["W", "W", "W", "W"],
        "pentatonic": ["W", "W", "WH", "W", "WH"],

        "fourths": ["WWH"] * 12,
        "fifths":  ["WWWH"] * 12,

        "relative minor": ["W", "W", "H", "W", "W", "W", "H"],

        # Note: ionian is major, aeolian is minor
        "ionian":     ["W", "W", "H", "W", "W", "W", "H"],
        "dorian":     ["W", "H", "W", "W", "W", "H", "W"],
        "phrygian":   ["H", "W", "W", "W", "H", "W", "W"],
        "lydian":     ["W", "W", "W", "H", "W", "W", "H"],
        "mixolydian": ["W", "W", "H", "W", "W", "H", "W"],
        "aeolian":    ["W", "H", "W", "W", "H", "W", "W"],
        "locrian":    ["H", "W", "W", "H", "W", "W", "W"],
    }

    chord_intervals = {
        "triad": [1, 3, 5],
        "sus2": [1, 2, 5],
        "sus4": [1, 4, 5],
        "6th": [1, 3, 5, 6],
        "7th": [1, 3, 5, 7],
        "9th": [1, 3, 5, 7, 9],
        "11th": [1, 3, 5, 7, 9, 11],
        "13th": [1, 3, 5, 7, 9, 11, 13],
    }

    def __init__(self, notes, starting_note):
        self.scale = CircularDoublyLinkedList(notes, starting_note)
        self.starting_note = starting_note

    def __repr__(self):
        return self.scale.__repr__()

    @ classmethod
    def chromatic_scale(cls, starting_note):
        return cls(cls.chromatic_notes, starting_note)

    def letter2num(cls, interval_list):
        num_list = []

        for i, interval in enumerate(interval_list):
            num_semitones = 0

            for letter in interval:
                num_semitones += cls.step_intervals.get(letter)

            num_list.append(num_semitones)

        return num_list

    def generate_scale(self, scale_interval):
        interval_list = self.scale_intervals.get(scale_interval)
        interval_list = self.letter2num(interval_list)

        node = self.scale.head
        new_notes = [node.data]

        for num_steps in interval_list:
            for i in range(0, num_steps):
                node = node.next

            new_notes.append(node.data)

        new_nodes = CircularDoublyLinkedList(new_notes, self.starting_note)

        if scale_interval == "relative minor":
            relative_minor = new_nodes.head.prev.prev.prev
            relative_minor.data = relative_minor.data + "m"

            return relative_minor
        else:
            return new_nodes

    def generate_chord(self, scale_interval, chord_interval):
        scale = self.generate_scale(scale_interval)

        interval_list = self.chord_intervals.get(chord_interval)
        interval_list = [t - s for
                         s, t in zip(interval_list, interval_list[1:])]

        node = scale.head
        new_notes = [node.data]

        for num_steps in interval_list:
            for i in range(0, num_steps):
                node = node.next

            new_notes.append(node.data)

        new_nodes = CircularDoublyLinkedList(new_notes, self.starting_note)
        return new_nodes
