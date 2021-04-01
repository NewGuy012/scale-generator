from CircularDoublyLinkedList import MusicalScale


def main():
    keys = ["C"]
    scales = ["major", "minor", "dominant", "diminished", "augmented",
              "pentatonic", "fourths", "fifths", "relative minor"]
    chords = ["triad", "sus2", "sus4", "7th", "9th", "11th", "13th"]

    for key in keys:

        key_chromatic_scale = MusicalScale.chromatic_scale(key)
        output_str = f'{key} chromatic: {key_chromatic_scale}'
        print(output_str)

        for scale in scales:
            key_scale = key_chromatic_scale.generate_scale(scale)
            output_str = f'{key} {scale} scale: {key_scale}'
            print(output_str)

            if scale in ["major", "minor", "dominant", "diminished", "augmented"]:
                for chord in chords:
                    key_chord = key_chromatic_scale.generate_chord(
                        scale, chord)
                    output_str = f'{key} {scale} {chord:>5}: {key_chord}'
                    print(output_str)
            print("\n")
        print("\n")


if __name__ == "__main__":
    main()
