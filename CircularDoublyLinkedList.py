from more_itertools import pairwise


class Node:
    """
    A class used to represent a Node in a Doubly Linked List.
    """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return self.data


class CircularDoublyLinkedList:
    """A class used to represent a Circular Doubly Linked List"""

    def __init__(self, data=None, starting_data=None):
        """
        Parameters
        ----------
        data : list of str
            A list of data to initialize the linked list
        starting_data : str
            The starting node data
        """
        nodes = [Node(item) for item in data]

        starting_index = [idx for idx, elem in enumerate(data)
                          if starting_data == elem][0]
        self.head = nodes[starting_index]

        for current_node, next_node in pairwise(nodes):
            current_node.next = next_node
            next_node.prev = current_node

        nodes[0].prev = nodes[-1]
        nodes[-1].next = nodes[0]

    def __repr__(self):
        node = self.head
        nodes = [node.data]

        while node.next != self.head:
            node = node.next
            nodes.append(node.data)

        return " -> ".join(nodes)


class MusicalScale:
    chromatic_notes = ["C", "(C#/Db)", "D", "(D#/Eb)", "E", "F",
                       "(F#/Gb)", "G", "(G#/Ab)", "A", "(A#/Bb)", "B"]

    sharp_keys = ["C", "G", "D", "A", "E", "B", "(F#/Gb)"]

    step_intervals = {
        "H": 1,
        "W": 2
    }

    scale_intervals = {
        "major":      ["W", "W", "H", "W", "W", "W", "H"],
        "minor":      ["W", "H", "W", "W", "H", "W", "W"],
        "dominant":   ["W", "W", "H", "W", "W", "H", "W"],
        "diminished": ["W", "H", "W", "H", "W", "W", "W"],
        "augmented":  ["W", "W", "W", "W", "H", "W", "H"],
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
        "diatonic": list(range(1, 8)),
    }

    def __init__(self, notes, starting_note):
        self.scale = CircularDoublyLinkedList(notes, starting_note)
        self.starting_note = starting_note

    def __repr__(self):
        return self.scale.__repr__()

    @ classmethod
    def chromatic_scale(cls, starting_note):
        """Class method docstrings go here."""
        return cls(cls.chromatic_notes, starting_note)

    def letter2num(self, interval_list):
        """Class method docstrings go here."""
        num_list = []

        for i, interval in enumerate(interval_list):
            num_semitones = 0

            for letter in interval:
                num_semitones += self.step_intervals.get(letter)

            num_list.append(num_semitones)

        return num_list

    def generate_scale(self, scale_interval):
        """Class method docstrings go here."""
        interval_list = self.scale_intervals.get(scale_interval)
        interval_list = self.letter2num(interval_list)
        interval_list.pop()

        node = self.scale.head
        new_notes = [node.data]

        for num_steps in interval_list:
            for i in range(0, num_steps):
                node = node.next

            new_notes.append(node.data)

        new_nodes = CircularDoublyLinkedList(new_notes, self.starting_note)

        if scale_interval == "relative minor":
            relative_minor = new_nodes.head.prev.prev

            return relative_minor
        else:
            return new_nodes

    def generate_chord(self, scale_interval, chord_interval):
        """Class method docstrings go here."""
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

        if chord_interval == "diatonic":
            if scale_interval == "major":
                major_chords = ["", "m", "m", "", "", "m", "o"]
                node = new_nodes.head

                for suffix in major_chords:
                    node.data = node.data + suffix
                    node = node.next

            elif scale_interval == "minor":
                minor_chords = ["m", "o", "", "m", "m", "", ""]

                node = new_nodes.head

                for suffix in minor_chords:
                    node.data = node.data + suffix
                    node = node.next

        return new_nodes

    def generate_signature(self, key):
        C_chromatic_scale = MusicalScale.chromatic_scale("C")
        scale_fifths = C_chromatic_scale.generate_scale("fifths")

        current_node = scale_fifths.head
        num_sharps = 0
        num_flats = 0

        while key != current_node.data:
            if key in MusicalScale.sharp_keys:
                num_sharps += 1
                current_node = current_node.next
            else:
                num_flats += 1
                current_node = current_node.prev

        return num_sharps, num_flats


def generate_musical_scale(keys=["C"], scales=["major"], chords=["triad"]):
    """This is the summary line

    This is the further elaboration of the docstring. Within this section,
    you can elaborate further on details as appropriate for the situation.
    Notice that the summary and the elaboration is separated by a blank new
    line.
    """

    for key in keys:
        key_chromatic_scale = MusicalScale.chromatic_scale(key)
        # output_str = f"{key} chromatic: {key_chromatic_scale}"
        # print(output_str)

        num_sharps, num_flats = key_chromatic_scale.generate_signature(key)
        output_str = f"{key} signature: {num_sharps}#/{num_flats}b"
        print(output_str)

        for scale in scales:
            key_scale = key_chromatic_scale.generate_scale(scale)

            if scale in ["pentatonic", "fourths", "fifths", "relative minor"]:
                output_str = f"{key} {scale} scale: {key_scale}"
                print(output_str)
            else:
                output_str = f"{key} {scale} {'scale':>5}: {key_scale}"
                print(output_str)

            if scale in ["major", "minor"]:
                for chord in chords:
                    key_chord = key_chromatic_scale.generate_chord(
                        scale, chord)
                    output_str = f"{key} {scale} {chord:>5}: {key_chord}"
                    print(output_str)

            if scale in ["dominant", "diminished", "augmented"]:
                for chord in chords:
                    if chord != "diatonic":
                        key_chord = key_chromatic_scale.generate_chord(
                            scale, chord)
                        output_str = f"{key} {scale} {chord:>5}: {key_chord}"
                        print(output_str)
            print("\n")
