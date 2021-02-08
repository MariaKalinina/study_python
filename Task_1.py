class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        print(f"Matrix {self.matrix}:")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()

    def __add__(self, other):
        result = []
        for item in zip(self.matrix, other.matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)


matrix_1 = Matrix([[1, 12], [3, 5], [7, 9]])
matrix_2 = Matrix([[21, 2], [33, 4], [2, 45]])
matrix_1.__str__()
matrix_2.__str__()
print(matrix_1 + matrix_2)
