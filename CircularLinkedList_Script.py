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
print(chromatic_scale)

chromatic_scale.generate_scale("C", "major")
chromatic_scale.generate_scale("A", "minor")
chromatic_scale.generate_scale("C", "pentatonic")
chromatic_scale.generate_scale("C", "fifths")
chromatic_scale.generate_scale("C", "fourths")
chromatic_scale.generate_scale("C", "relative minor")
