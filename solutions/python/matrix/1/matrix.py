class Matrix:
    def __init__(self, matrix_string):
        self.matrix=[fila.split() for fila in matrix_string.split("\n")]
        print(self.matrix)
    def row(self, index):
        return [int(item) for item in self.matrix[index-1]]

    def column(self, index):
        return [int(row[index-1]) for row in self.matrix]
