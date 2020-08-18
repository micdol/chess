class Move():
    def __init__(self):
        # destination and origin square (0-63)
        self.toSquare = 0
        self.fromSquare = 0
        # False or PieceType if promotion
        self.promotion = False
        self.enPassant = False
        self.castling = False