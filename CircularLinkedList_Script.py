from CircularLinkedList import CircularLinkedList as CLL
import copy

C_chromatic = CLL(["C",
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
                   "B"])
print(C_chromatic)
C_major = C_chromatic.major_scale()
print(C_major)

D_chromatic = copy.deepcopy(C_chromatic)
D_chromatic.head = D_chromatic.head.next.next

print(D_chromatic)
D_major = D_chromatic.major_scale()
print(D_major)
