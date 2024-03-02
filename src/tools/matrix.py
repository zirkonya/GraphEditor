class Matrix:
    def __init__(self):
        self.matrix = []
        self.rows = 0
        self.cols = 0

    def __str__(self):
        return str(self.matrix)

    def zeros(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for i in range(cols)] for j in range(rows)]
        return self

    def identity(self, size):
        self.rows = size
        self.cols = size
        self.matrix = [[1 if i == j else 0 for i in range(size)] for j in range(size)]
        return self

    def at(self, i, j):
        return self.matrix[i][j]

    def set_at(self, i, j, value):
        self.matrix[i][j] = value

    def from_list(self, matrix):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        for row in matrix:
            if len(row)!= self.rows:
                raise ValueError("Matrix must have same rows size")
        self.matrix = matrix
        return self

    def is_square(self):
        return self.rows == self.cols

    # Operations of matrix
    def __add__(self, other):
        if self.cols != other.cols and self.rows != other.rows:
            raise ValueError("Matrices must have same columns size")
        new_matrix = Matrix()
        new_matrix.rows = self.rows
        new_matrix.cols = self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_at(i, j, self.at(i, j) + other.at(i, j))
        return new_matrix

    def __sub__(self, other):
        if self.cols != other.cols and self.rows != other.rows:
            raise ValueError("Matrices must have same columns size")
        new_matrix = Matrix()
        new_matrix.rows = self.rows
        new_matrix.cols = self.cols
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.set_at(i, j, self.at(i, j) - other.at(i, j))
        return new_matrix

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrices must have same columns size")
        new_matrix = Matrix()
        new_matrix.rows = self.rows
        new_matrix.cols = other.cols
        for i in range(self.rows):
            for j in range(other.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.at(i, k) * other.at(k, j)
                new_matrix.set_at(i, j, sum)
        return new_matrix
