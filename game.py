# Chess Game Flow and Turn Management

class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = 'white'
        self.game_over = False

    def create_board(self):
        # Create an 8x8 chess board with initial positions
        pass  # Implementation left as an exercise

    def switch_turn(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def make_move(self, move):
        # Logic to make a move
        pass  # Implementation left as an exercise

    def is_checkmate(self):
        # Checkmate logic
        pass  # Implementation left as an exercise

    def play(self):
        while not self.game_over:
            print(f"{self.current_turn}'s turn")
            move = input("Enter your move: ")
            self.make_move(move)
            if self.is_checkmate():
                print(f"Checkmate! {self.current_turn} wins!")
                self.game_over = True
            self.switch_turn()

# To play the game:
if __name__ == '__main__':
    game = ChessGame()
    game.play()