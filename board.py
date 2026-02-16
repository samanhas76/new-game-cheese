# Chess Board Management in Python

class ChessBoard:
    def __init__(self):
        # Initialize an 8x8 chess board
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()

    def setup_board(self):
        # Set up the pieces on the board
        self.board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  # Black pieces
        self.board[1] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']  # Black pawns
        self.board[6] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']  # White pawns
        self.board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']  # White pieces

    def display(self):
        # Print the board to the console
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))

    def move_piece(self, start, end):
        # Move a piece from start to end
        piece = self.board[start[0]][start[1]]
        self.board[end[0]][end[1]] = piece
        self.board[start[0]][start[1]] = None

# Example usage
if __name__ == '__main__':
    chess_board = ChessBoard()
    chess_board.display()
    # Move a pawn from (6, 4) to (4, 4)
    chess_board.move_piece((6, 4), (4, 4))
    chess_board.display()