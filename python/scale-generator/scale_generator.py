class Scale:
    def __init__(self, tonic):
        self.signature = 'sharp' if tonic in ['C', "D", "E", "G", "A", "B", 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a'] else 'flat'
        self.tonic = tonic.upper() if len(tonic) == 1 else tonic[0].upper() + tonic[1]

    def chromatic(self):
        if self.signature == 'sharp':
            note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        else:
            note = ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]
        index = note.index(self.tonic)
        return note[index:] + note[:index]

    def interval(self, intervals):
        notes = []
        if self.signature == 'sharp':
            note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        else:
            note = ["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]
        index = note.index(self.tonic)
        for i in intervals:
            notes.append(note[index])
            if i == 'm':
                index += 1
            elif i == 'M':
                index += 2
            else:
                index += 3
            if index >= 12:
                index -= 12
        return notes + [self.tonic]
