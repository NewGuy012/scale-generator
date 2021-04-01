from CircularDoublyLinkedList import MusicalScale


def main():
    keys = ["C"]
    scales = ["major", "minor", "dominant", "diminished", "augmented",
              "pentatonic", "fourths", "fifths", "relative minor"]
    # chords = ["triad", "sus2", "sus4", "7th", "9th", "11th", "13th"]
    chords = ["triad"]

    for key in keys:

        key_chromatic_scale = MusicalScale.chromatic_scale(key)
        print(f'{key} chromatic : {key_chromatic_scale}')
        print("\n")

        for scale in scales:
            key_scale = key_chromatic_scale.generate_scale(scale)
            print(f'{key} {scale} : {key_scale}')

            if scale in ["major", "minor", "dominant", "diminished", "augmented"]:
                for chord in chords:

                    key_chord = key_chromatic_scale.generate_chord(
                        scale, chord)
                    print(f'{key} {scale} {chord} : {key_chord}')

                print("\n")

        print("\n")


if __name__ == "__main__":
    main()
