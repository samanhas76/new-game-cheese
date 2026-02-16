class ChessPiece:
    def __init__(self, color, position):
        self.color = color  # 'white' or 'black'
        self.position = position  # e.g., (0, 0)

    def move(self, new_position):
        # Logic to validate the move can be added here
        self.position = new_position

class Pawn(ChessPiece):
    def move(self, new_position):
        # Pawn specific move logic (e.g., forward 1 square)
        super().move(new_position)

class Rook(ChessPiece):
    def move(self, new_position):
        # Rook specific move logic (e.g., vertical or horizontal)
        super().move(new_position)

# Additional classes for Knight, Bishop, Queen, King can be defined similarly.