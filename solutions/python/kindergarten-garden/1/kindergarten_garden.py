plantas={
    "G":"Grass",
    "C":"Clover",
    "R":"Radishes",
    "V":"Violets"
}
class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.zurcos=[[item[pos:pos+2] for pos in range(0,len(item),2)] for item in diagram.split("\n")]
        self.students=sorted(students)
    
    def plants(self,student):
        if student in self.students:
            idx=self.students.index(student)
        else:
            idx=0
        print(idx)
        iniciales_planta=[item[idx] for item in self.zurcos]
        return [plantas[letra] for inicial in iniciales_planta for letra in inicial]