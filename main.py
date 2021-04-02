from CircularDoublyLinkedList import MusicalScale


def generate_musical_scale(keys=["C"], scales=["major"], chords=["triad"]):
    # scales = ["major", "minor", "dominant", "diminished", "augmented",
    #           "pentatonic", "fourths", "fifths", "relative minor"]
    # chords = ["triad", "sus2", "sus4", "7th",
    #           "9th", "11th", "13th", "diatonic"]

    for key in keys:

        key_chromatic_scale = MusicalScale.chromatic_scale(key)
        output_str = f"{key} chromatic: {key_chromatic_scale}"
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
        print("\n")


if __name__ == "__main__":
    keys_list = ["C", "D"]
    scales_list = ["major", "minor", "dominant", "diminished", "augmented",
                   "pentatonic", "fourths", "fifths", "relative minor"]
    chords_list = ["triad", "sus2", "sus4", "7th",
                   "9th", "11th", "13th", "diatonic"]

    generate_musical_scale(
        keys=keys_list, scales=scales_list, chords=chords_list)
