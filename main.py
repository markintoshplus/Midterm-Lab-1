from user_interface import UserInterface
from matrix_puzzle import MatrixPuzzle

def main():
    ui = UserInterface()
    
    while True:
        width, height, bricks = ui.get_user_input()
        
        puzzle = MatrixPuzzle(width, height, bricks)
        solutions = puzzle.solve()
        
        if solutions:
            print(f"\n{len(solutions)} solution(s) found:")
            for i, solution in enumerate(solutions, 1):
                print(f"\nSolution {i}:")
                print(solution)
        else:
            print("\nNo valid solutions found for the given inputs.")
        
        play_again = input("\nDo you want to solve another puzzle? (yes/no): ").lower()
        if play_again != 'yes' and play_again != 'y':
            print("Thank you for using the Matrix Puzzle Solver. Goodbye!")
            break

if __name__ == "__main__":
    main()
