class School:
    def __init__(self):
        self.lista=[]
        self.add=[]

    def add_student(self, name, grade):
        if name not in [item[0] for item in self.lista]:
            self.lista.append([name,grade])
            self.add.append(True)
            return True
        self.add.append(False)
        return False

    def roster(self):
        out=sorted(self.lista,key=lambda x:(x[1],x[0]))
        return [item[0] for item in out]

    def grade(self, grade_number):
        return sorted([item[0] for item in self.lista if item[1]==grade_number])

    def added(self):
        return self.add
