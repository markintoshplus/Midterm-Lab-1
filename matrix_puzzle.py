from collections import deque
from typing import List, Optional
from matrix import Matrix
from matrix_node import MatrixNode
from brick import Brick

class MatrixPuzzle:
    def __init__(self, width: int, height: int, bricks: List[Brick]):
        self.width = width
        self.height = height
        self.bricks = bricks

    def solve(self) -> List[Matrix]:
        initial_matrix = Matrix(self.width, self.height)
        root = MatrixNode(initial_matrix, len(self.bricks))
        queue = deque([(root, 0)])  # (node, brick_index)
        solutions = []

        while queue:
            node, brick_index = queue.popleft()
            
            if brick_index == len(self.bricks):
                solutions.append(node.matrix)
                continue
            
            brick = self.bricks[brick_index]
            for start_y in range(self.height - brick.height + 1):
                for start_x in range(self.width - brick.width + 1):
                    if node.matrix.can_place_brick(start_x, start_y, brick):
                        new_matrix = node.matrix.copy()
                        new_matrix.place_brick(start_x, start_y, brick)
                        child = MatrixNode(new_matrix, node.remaining_bricks - 1)
                        node.children.append(child)
                        queue.append((child, brick_index + 1))

        unique_solutions = []

        for matrix in solutions:
            if not any(matrix.is_similar(unique_matrix) for unique_matrix in unique_solutions):
                unique_solutions.append(matrix)
        
        return unique_solutions
    
