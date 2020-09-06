from enum import IntEnum


class Player(IntEnum):
    WHITE = 0,
    BLACK = 1


class RankBB(IntEnum):
    RANK_1 = 0x00_00_00_00_00_00_00_ff,
    RANK_2 = 0x00_00_00_00_00_00_ff_00,
    RANK_3 = 0x00_00_00_00_00_ff_00_00,
    RANK_4 = 0x00_00_00_00_ff_00_00_00,
    RANK_5 = 0x00_00_00_ff_00_00_00_00,
    RANK_6 = 0x00_00_ff_00_00_00_00_00,
    RANK_7 = 0x00_ff_00_00_00_00_00_00,
    RANK_8 = 0xff_00_00_00_00_00_00_00

    @property
    def next(self):
        n = int(self.name[-1])+1
        if n <= 8:
            return RankBB[f'RANK_{n}']

    @property
    def prev(self):
        n = int(self.name[-1])-1
        if n >= 1:
            return RankBB[f'RANK_{n}']


class FileBB(IntEnum):
    FILE_A = 0x01_01_01_01_01_01_01_01,
    FILE_B = 0x02_02_02_02_02_02_02_02,
    FILE_C = 0x04_04_04_04_04_04_04_04,
    FILE_D = 0x08_08_08_08_08_08_08_08,
    FILE_E = 0x10_10_10_10_10_10_10_10,
    FILE_F = 0x20_20_20_20_20_20_20_20,
    FILE_G = 0x40_40_40_40_40_40_40_40,
    FILE_H = 0x80_80_80_80_80_80_80_80


class SquareBB(IntEnum):
    SQ_A1 = 1 << 0,
    SQ_B1 = 1 << 1,
    SQ_C1 = 1 << 2,
    SQ_D1 = 1 << 3,
    SQ_E1 = 1 << 4,
    SQ_F1 = 1 << 5,
    SQ_G1 = 1 << 6,
    SQ_H1 = 1 << 7,
    SQ_A2 = 1 << 8,
    SQ_B2 = 1 << 9,
    SQ_C2 = 1 << 10,
    SQ_D2 = 1 << 11,
    SQ_E2 = 1 << 12,
    SQ_F2 = 1 << 13,
    SQ_G2 = 1 << 14,
    SQ_H2 = 1 << 15,
    SQ_A3 = 1 << 16,
    SQ_B3 = 1 << 17,
    SQ_C3 = 1 << 18,
    SQ_D3 = 1 << 19,
    SQ_E3 = 1 << 20,
    SQ_F3 = 1 << 21,
    SQ_G3 = 1 << 22,
    SQ_H3 = 1 << 23,
    SQ_A4 = 1 << 24,
    SQ_B4 = 1 << 25,
    SQ_C4 = 1 << 26,
    SQ_D4 = 1 << 27,
    SQ_E4 = 1 << 28,
    SQ_F4 = 1 << 29,
    SQ_G4 = 1 << 30,
    SQ_H4 = 1 << 31,
    SQ_A5 = 1 << 32,
    SQ_B5 = 1 << 33,
    SQ_C5 = 1 << 34,
    SQ_D5 = 1 << 35,
    SQ_E5 = 1 << 36,
    SQ_F5 = 1 << 37,
    SQ_G5 = 1 << 38,
    SQ_H5 = 1 << 39,
    SQ_A6 = 1 << 40,
    SQ_B6 = 1 << 41,
    SQ_C6 = 1 << 42,
    SQ_D6 = 1 << 43,
    SQ_E6 = 1 << 44,
    SQ_F6 = 1 << 45,
    SQ_G6 = 1 << 46,
    SQ_H6 = 1 << 47,
    SQ_A7 = 1 << 48,
    SQ_B7 = 1 << 49,
    SQ_C7 = 1 << 50,
    SQ_D7 = 1 << 51,
    SQ_E7 = 1 << 52,
    SQ_F7 = 1 << 53,
    SQ_G7 = 1 << 54,
    SQ_H7 = 1 << 55,
    SQ_A8 = 1 << 56,
    SQ_B8 = 1 << 57,
    SQ_C8 = 1 << 58,
    SQ_D8 = 1 << 59,
    SQ_E8 = 1 << 60,
    SQ_F8 = 1 << 61,
    SQ_G8 = 1 << 62,
    SQ_H8 = 1 << 63

    @property
    def rankBB(self):
        return RankBB[f'RANK_{self.name[-1]}']

    @property
    def fileBB(self):
        return FileBB[f'FILE_{self.name[-2]}']


class Square(IntEnum):
    SQ_A1 = 0,
    SQ_B1 = 1,
    SQ_C1 = 2,
    SQ_D1 = 3,
    SQ_E1 = 4,
    SQ_F1 = 5,
    SQ_G1 = 6,
    SQ_H1 = 7,
    SQ_A2 = 8,
    SQ_B2 = 9,
    SQ_C2 = 10,
    SQ_D2 = 11,
    SQ_E2 = 12,
    SQ_F2 = 13,
    SQ_G2 = 14,
    SQ_H2 = 15,
    SQ_A3 = 16,
    SQ_B3 = 17,
    SQ_C3 = 18,
    SQ_D3 = 19,
    SQ_E3 = 20,
    SQ_F3 = 21,
    SQ_G3 = 22,
    SQ_H3 = 23,
    SQ_A4 = 24,
    SQ_B4 = 25,
    SQ_C4 = 26,
    SQ_D4 = 27,
    SQ_E4 = 28,
    SQ_F4 = 29,
    SQ_G4 = 30,
    SQ_H4 = 31,
    SQ_A5 = 32,
    SQ_B5 = 33,
    SQ_C5 = 34,
    SQ_D5 = 35,
    SQ_E5 = 36,
    SQ_F5 = 37,
    SQ_G5 = 38,
    SQ_H5 = 39,
    SQ_A6 = 40,
    SQ_B6 = 41,
    SQ_C6 = 42,
    SQ_D6 = 43,
    SQ_E6 = 44,
    SQ_F6 = 45,
    SQ_G6 = 46,
    SQ_H6 = 47,
    SQ_A7 = 48,
    SQ_B7 = 49,
    SQ_C7 = 50,
    SQ_D7 = 51,
    SQ_E7 = 52,
    SQ_F7 = 53,
    SQ_G7 = 54,
    SQ_H7 = 55,
    SQ_A8 = 56,
    SQ_B8 = 57,
    SQ_C8 = 58,
    SQ_D8 = 59,
    SQ_E8 = 60,
    SQ_F8 = 61,
    SQ_G8 = 62,
    SQ_H8 = 63

    @property
    def rank(self):
        return Rank[f'RANK_{self.name[-1]}']

    @property
    def file(self):
        return File[f'FILE_{self.name[-2]}']


class Rank(IntEnum):
    RANK_1 = 0,
    RANK_2 = 1,
    RANK_3 = 2,
    RANK_4 = 3,
    RANK_5 = 4,
    RANK_6 = 5,
    RANK_7 = 6,
    RANK_8 = 7


class File(IntEnum):
    FILE_A = 0,
    FILE_B = 1,
    FILE_C = 2,
    FILE_D = 3,
    FILE_E = 4,
    FILE_F = 5,
    FILE_G = 6,
    FILE_H = 7


# --- BLACK PAWN MOVES ---
blackPawnMoves = [0] * 64
# move to prev rank
for r in Rank:
    for f in File:
        rbb = RankBB[r.name]
        fbb = FileBB[f.name]
        prbb = rbb.prev
        if prbb is not None:
            sq = r * len(File) + f
            blackPawnMoves[sq] = prbb & fbb

# exclude rank 8 - no way pawn gets there
for sq in range(Square.SQ_A8, Square.SQ_H8 + 1):
    blackPawnMoves[sq] = 0

# include move to rank 5 from rank 7
sq = Square.SQ_A7
for f in FileBB:
    blackPawnMoves[sq] |= RankBB.RANK_5 & f
    sq += 1

# --- WHITE PAWN MOVES ---
whitePawnMoves = [0] * 64
# move to next rank
for r in Rank:
    for f in File:
        rbb = RankBB[r.name]
        fbb = FileBB[f.name]
        nrbb = rbb.next
        if nrbb is not None:
            sq = r * len(File) + f
            whitePawnMoves[sq] = nrbb & fbb

# exclude rank 1 - no way pawn gets there
for sq in range(Square.SQ_A1, Square.SQ_H1 + 1):
    whitePawnMoves[sq] = 0

# include move to rank 4 from rank 2
sq = Square.SQ_A2
for f in FileBB:
    whitePawnMoves[sq] |= RankBB.RANK_4 & f
    sq += 1

# --- ROOKS MOVES ---
rookMove = [0] * 64
for sq in Square:
    rbb = RankBB[f'RANK_{sq.name[-1]}']
    fbb = FileBB[f'FILE_{sq.name[-2]}']
    sbb = SquareBB[sq.name]
    rookMove[sq] = (rbb | fbb) ^ sbb

# --- KNIGHS MOVES ---
knightMove = [0] * 64
for sqFrom in Square:
    rbb = RankBB[f'RANK_{sqFrom.name[-1]}']
    fbb = FileBB[f'FILE_{sqFrom.name[-2]}']
    sqFromBB = SquareBB[sqFrom.name]
    for n in [6, 10, 15, 17]:
        if sqFrom + n < 64:
            sqTo = Square(sqFrom + n)
            sqToBB = SquareBB[sqTo.name]
            # max distance of 2 files or ranks!
            if max(abs(sqTo.rank - sqFrom.rank), abs(sqTo.file - sqFrom.file)) <= 2:
                knightMove[sqFrom] |= sqToBB
        if sqFrom - n >= 0:
            sqTo = Square(sqFrom - n)
            sqToBB = SquareBB[sqTo.name]
            if max(abs(sqTo.rank - sqFrom.rank), abs(sqTo.file - sqFrom.file)) <= 2:
                knightMove[sqFrom] |= sqToBB

# --- BISHOP MOVES ----
bishopMoves = [0] * 64
for sqFrom in Square:
    pass

def printBB(bb, sq=None):
    print('   a b c d e f g h')
    for rank in range(Rank.RANK_8, -1, -1):
        s = f'{rank+1} '
        for file in range(len(File)):
            i = rank * 8 + file
            m = 1 << i
            v = bb & m
            if sq is not None and i == sq:
                s += '|p'
            elif v:
                s += '|.'
            else:
                s += '| '
        print(f'{s}|')
    print()


for sq in Square:
    bb = knightMove[sq]
    printBB(bb, sq)
