from pieces import *


class Board():
    # FEN
    # rank1/rank2/rank3/rank4/rank5/rank6/rank7/rank8 P EP HM FM
    #
    # rank[N] - pieces in Nth rank, lower black, upper white, 1-8 empty
    # P: w/b - who moves next
    # C: KQkq - castling option, upper white, lower black, K/Q king/queen side
    # EP: -/e5 - en passant possibility (always set) or - if not applicable
    # HM: 0 - number of half moves since last capture or pawn advance
    # FM: The number of the full move. It starts at 1, and is incremented after Black's move.
    startFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    def __init__(self):
        self.nextPlayer = 'w'
        self.whiteOO = True
        self.whiteOOO = True
        self.blackOO = True
        self.blackOOO = True
        self.ep = '-'
        self.halfMoves = 0
        self.fullMoves = 1
        self.board = [None] * 64
        # rank by rank, 0: a1, 1; b1...
        self.fromFen(Board.startFEN)

    def pieceAt(self, rank, file):
        idx = rank * 8 + file
        return self.board[idx]

    def fromFen(self, fen):
        x = fen.split(sep=' ')
        ranks, self.nextPlayer, castling, self.ep, self.halfMoves, self.fullMoves = x
        ranks = ranks.split('/')
        self.whiteOO = 'K' in castling
        self.whiteOOO = 'Q' in castling
        self.blackOO = 'k' in castling
        self.blackOOO = 'q' in castling

        # fen goes from top (rank8) to bottom (rank1)
        # move forward in rank: idx++
        # at the end of the rank, jump to prev rank start: idx -= 16
        idx = 56

        for rank in ranks:
            for piece in rank:
                # if int
                try:
                    empty = int(piece)
                    self.board[idx:idx+empty] = [None] * empty
                    idx += empty
                except:
                    self.board[idx] = piece
                    idx += 1

            idx -= 16

    def fen(self):
        ranks = []
        for rank in self._rranks():
            empty = 0
            s = ''
            for piece in rank:
                if piece is None:
                    empty += 1
                    continue
                if empty != 0:
                    s += str(empty)
                    empty = 0
                s += piece
            if empty != 0:
                s += str(empty)
            ranks.append(s)

        castling = ''
        if self.whiteOO:
            castling += 'K'
        if self.whiteOOO:
            castling += 'Q'
        if self.blackOO:
            castling += 'k'
        if self.blackOOO:
            castling += 'Q'
        if not castling:
            castling = '-'

        return f'{"/".join(ranks)} {self.nextPlayer} {castling} {self.ep} {self.halfMoves} {self.fullMoves}'

    def show(self):
        lineSep = '\n +---+---+---+---+---+---+---+---+\n'
        board = lineSep
        for rank in self._rranks():
            line = ''
            for piece in rank:
                if piece is None:
                    piece = ' '
                line = f'{line} | {piece}'
            board = f'{board}{line} | {lineSep}'
        print(board)

    # list of ranks from 8 to 1
    def _rranks(self):
        idx = 56
        for i in range(0, 8):
            yield self.board[idx:idx+8]
            idx -= 8

    # list of ranks from 1 to 8
    def ranks(self):
        idx = 8
        for i in range(0, 8):
            yield self.board[idx:idx + 8]
            idx += 8


b = Board()
b.show()
print(b.fen())
