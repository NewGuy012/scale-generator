from CircularDoublyLinkedList import MusicalScale, generate_musical_scale


def main():
    # keys_list = ["C", "D"]
    # scales_list = ["major", "minor", "dominant", "diminished", "augmented",
    #                "pentatonic", "fourths", "fifths", "relative minor"]
    # chords_list = ["triad", "sus2", "sus4", "7th",
    #                "9th", "11th", "13th", "diatonic"]
    keys_list = ["C", "D", "A", "F", "(A#/Bb)"]
    scales_list = ["major"]
    chords_list = ["triad"]

    generate_musical_scale(
        keys=keys_list, scales=scales_list, chords=chords_list)


if __name__ == "__main__":
    main()
