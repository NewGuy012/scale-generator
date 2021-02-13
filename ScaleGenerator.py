from CircularLinkedList import CircularLinkedList as CLL

chromatic_scale = CLL(("C",
                       "C#/Db",
                       "D",
                       "D#/Eb",
                       "E",
                       "F",
                       "F#/Gb",
                       "G",
                       "G#/Ab",
                       "A",
                       "A#/Bb",
                       "B"))
print("12 Tone, Equal Temperament")
print(chromatic_scale)
print("\n")

print("Scales in Key of C")
chromatic_scale.generate_scale("C", "major")
chromatic_scale.generate_scale("C", "minor")
chromatic_scale.generate_scale("C", "relative minor")
chromatic_scale.generate_scale("C", "ionian")
chromatic_scale.generate_scale("C", "dorian")
chromatic_scale.generate_scale("C", "phrygian")
chromatic_scale.generate_scale("C", "lydian")
chromatic_scale.generate_scale("C", "mixolydian")
chromatic_scale.generate_scale("C", "aeolian")
chromatic_scale.generate_scale("C", "locrian")
chromatic_scale.generate_scale("A", "minor")
chromatic_scale.generate_scale("C", "pentatonic")
chromatic_scale.generate_scale("C", "fifths")
chromatic_scale.generate_scale("C", "fourths")
print("\n")

print("Chords in Key of C")
chromatic_scale.generate_chord("C", "major", "triad")
chromatic_scale.generate_chord("C", "major", "7")
chromatic_scale.generate_chord("C", "dominant", "7")
chromatic_scale.generate_chord("C", "minor", "triad")
chromatic_scale.generate_chord("C", "diminished", "triad")
chromatic_scale.generate_chord("C", "augmented", "triad")
chromatic_scale.generate_chord("C", "dominant", "7")
print("\n")

print("Chords in Key of D")
chromatic_scale.generate_chord("D", "major", "triad")
chromatic_scale.generate_chord("D", "dominant", "7")
print("\n")
