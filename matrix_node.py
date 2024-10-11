from matrix import Matrix

class MatrixNode:
    def __init__(self, matrix: Matrix, remaining_bricks: int):
        self.matrix = matrix
        self.remaining_bricks = remaining_bricks
        self.children = []
