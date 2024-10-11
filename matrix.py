from brick import Brick

class Matrix:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def can_place_brick(self, start_x: int, start_y: int, brick: Brick) -> bool:
        if start_x + brick.width > self.width or start_y + brick.height > self.height:
            return False
        return all(self.grid[y][x] == 0 
                   for y in range(start_y, start_y + brick.height) 
                   for x in range(start_x, start_x + brick.width))

    def place_brick(self, start_x: int, start_y: int, brick: Brick) -> None:
        for y in range(start_y, start_y + brick.height):
            for x in range(start_x, start_x + brick.width):
                self.grid[y][x] = 1

    def copy(self) -> 'Matrix':
        new_matrix = Matrix(self.width, self.height)
        new_matrix.grid = [row[:] for row in self.grid]
        return new_matrix

    def __str__(self) -> str:
        return '\n'.join(' '.join(['#' if cell == 1 else '.' for cell in row]) for row in self.grid)
