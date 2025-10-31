notas=[
    "A",
    "A#",
    "B",
    "C",
    "C#",
    "D",
    "D#",
    "E",
    "F",
    "F#",
    "G",
    "G#"
      ]
SHARP_KEYS = {
    "C", "D", "A", "E", "B", "F#",
    "a", "e", "b", "f#", "c#", "g#", "d#"
}

FLAT_KEYS = {
    "F", "Bb", "Eb", "Ab", "Db", "Gb",
    "d", "g", "c", "f", "bb", "eb"
}

class Scale:
    def __init__(self, tonic):

        self.bemol=False
        if tonic in SHARP_KEYS or sharp_to_b(tonic) in SHARP_KEYS:
            self.bemol=False
            print("Sostenido")
        elif tonic in FLAT_KEYS or sharp_to_b(tonic) in FLAT_KEYS:
            self.bemol=True
            print("Bemol")
            
        if len(tonic)==2:
            self.tonic=tonic[0].upper()+tonic[1]
        else:
            self.tonic=tonic.upper()

        if self.tonic not in notas:
            self.tonic=bemol_to_s(self.tonic)
            
        self.notes=self.interval("m")
        

    def chromatic(self):
        return self.notes

    def interval(self, intervals):
        tonic_pos=notas.index(self.tonic)

        

            
        #intervalo
        intervalos=[]
        for letter in intervals:
            if letter=="M":
                intervalos.append(2)
            elif letter=="m":
                intervalos.append(1)
            else:
                intervalos.append(3)

                
        notes=[]
        idx_intervalo=0
        acum=0
        print(intervalos)
        for pos in range(len(notas)):
            idx=(pos+tonic_pos+acum)%len(notas)
            
            if self.bemol:
                agregar=sharp_to_b(notas[idx])
            else:
                agregar=notas[idx]
                
            if agregar in notes:
                notes.append(agregar)
                break
            notes.append(agregar)
                
            acum+=intervalos[idx_intervalo]-1
            print(idx)
            idx_intervalo=(idx_intervalo+1)%len(intervalos)
        return notes
        
def sharp_to_b(sharp):
    if "#" in sharp:
        idx=notas.index(sharp)
        idx=(idx+1)%len(notas)
        return notas[idx]+"b"
    else:
        return sharp

def bemol_to_s(bemol):
    if "b" in bemol:
        idx=notas.index(bemol[0])
        idx=(idx-1)%len(notas)
        return notas[idx]
    else:
        return bemol