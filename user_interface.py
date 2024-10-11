from typing import List, Tuple
from brick import Brick

class UserInterface:
    @staticmethod
    def get_user_input() -> Tuple[int, int, List[Brick]]:
        width = int(input("Enter matrix width: "))
        height = int(input("Enter matrix height: "))
        num_bricks = int(input("Enter number of bricks: "))
        
        bricks = []
        for i in range(num_bricks):
            print(f"\nEnter dimensions for brick {i+1}:")
            brick_width = int(input(f"Enter width for brick {i+1}: "))
            brick_height = int(input(f"Enter height for brick {i+1}: "))
            bricks.append(Brick(brick_width, brick_height))
        
        return width, height, bricks
