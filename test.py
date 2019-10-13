#!/usr/bin/env python
# -*- coding:utf-8 -*-
import chess
import copy

board = chess.Board()
# piece = board.piece_at(chess.square('c', '3'))
# squares = chess.SquareSet(chess.BB_A8 | chess.BB_RANK_1)
# for x in chess.SQUARES:
# print(chess.square_file(x))
# print(chess.square_rank(x))
#     print(board.piece_at(x))
#     print(board.piece_at(x).piece_type)
# print(x)
# print(squares)

# c=ord('a')
# print(c)
pawnEvalWhite = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0],
    [1.0, 1.0, 2.0, 3.0, 3.0, 2.0, 1.0, 1.0],
    [0.5, 0.5, 1.0, 2.5, 2.5, 1.0, 0.5, 0.5],
    [0.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0],
    [0.5, -0.5, -1.0, 0.0, 0.0, -1.0, -0.5, 0.5],
    [0.5, 1.0, 1.0, -2.0, -2.0, 1.0, 1.0, 0.5],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]
def reverseArray(array):
    c=array[:]
    c.reverse()
    c[:].reverse()
    return c
black=reverseArray(pawnEvalWhite)
# x = 5 + pawnEvalWhite[2][1] if True else pawnEvalWhite[1][1]
print(pawnEvalWhite[1])
print(black[1])
# print(black)