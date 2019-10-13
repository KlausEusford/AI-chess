# !/usr/bin/env python2.7.12
# -*- coding:utf-8 -*-
import chess


def respond_to(fen):
    board = chess.Board(fen)
    # print(board)
    move = minimaxRoot(4, board, True)
    # board.push(move)
    # print(board)
    return str(move)


def minimaxRoot(depth, board, isMax):
    moves = board.legal_moves
    bestMove = None
    # 使用一个负数作为局面的评估
    bestValue = -9999

    for i in moves:
        newMove = i
        board.push(newMove)

        # 假设AI是黑棋，也就是黑棋走了一步以后，整个局面的分数上升
        boardValue = minimax(depth - 1, board, -10000, 10000, not isMax)
        board.pop()

        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = newMove
    return bestMove


def minimax(depth, board, alpha, beta, isMax):
    if depth == 0:
        return -evaluateBoard(board)

    moves = board.legal_moves


    if isMax:
        bestMove = -9999
        for i in moves:
            board.push(i)
            bestMove = max(bestMove, minimax(depth - 1, board, alpha, beta, not isMax))
            board.pop()

            alpha = max(alpha, bestMove)
            if beta <= alpha:
                return bestMove

        return bestMove
    else:
        bestMove = 9999
        for i in moves:
            board.push(i)
            bestMove = min(bestMove, minimax(depth - 1, board, alpha, beta, not isMax))
            board.pop()

            beta = min(beta, bestMove)
            if beta <= alpha:
                return bestMove

        return bestMove


# 下了一步棋之后，对于局面进行评估
def evaluateBoard(board):
    totalEvaluation = 0
    for square in chess.SQUARES:
        totalEvaluation += getPieceValue(board.piece_at(square), square)
    return totalEvaluation


# 调整棋子的权重
def reverseArray(list):
    re = list[:]
    re.reverse()
    return re


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
pawnEvalBlack = reverseArray(pawnEvalWhite)

knightEvalWhite = [
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
    [-4.0, -2.0, 0.0, 0.0, 0.0, 0.0, -2.0, -4.0],
    [-3.0, 0.0, 1.0, 1.5, 1.5, 1.0, 0.0, -3.0],
    [-3.0, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, -3.0],
    [-3.0, 0.0, 1.5, 2.0, 2.0, 1.5, 0.0, -3.0],
    [-3.0, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, -3.0],
    [-4.0, -2.0, 0.0, 0.5, 0.5, 0.0, -2.0, -4.0],
    [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
]
knightEvalBlack = reverseArray(knightEvalWhite)

bishopEvalWhite = [
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 1.0, 1.0, 0.5, 0.0, -1.0],
    [-1.0, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, -1.0],
    [-1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 0.0, -1.0],
    [-1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -1.0],
    [-1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.5, -1.0],
    [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]
bishopEvalBlack = reverseArray(bishopEvalWhite)

rookEvalWhite = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [-0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.5],
    [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0]
]
rookEvalBlack = reverseArray(rookEvalWhite)

evalQueenWhite = [
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-0.5, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, -0.5],
    [-1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0, -1.0],
    [-1.0, 0.0, 0.5, 0.0, 0.0, 0.0, 0.0, -1.0],
    [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]
evalQueenblack = reverseArray(evalQueenWhite)

kingEvalWhite = [

    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [-2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [-1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0],
    [2.0, 3.0, 1.0, 0.0, 0.0, 1.0, 3.0, 2.0]
]
kingEvalBlack = reverseArray(kingEvalWhite)


# 对于每一个棋子进行评估，黑色是负值，白色是正的
def getPieceValue(piece, square):
    if piece == None:
        return 0

    def getAbsoluteValue(piece, white, x, y):
        if piece.piece_type == 1:
            return 10 + (pawnEvalWhite[y][x] if white else pawnEvalBlack[y][x])
        elif piece.piece_type == 2:
            return 30 + (knightEvalWhite[y][x] if white else kingEvalBlack[y][x])
        elif piece.piece_type == 3:
            return 30 + (bishopEvalWhite[y][x] if white else bishopEvalBlack[y][x])
        elif piece.piece_type == 4:
            return 50 + (rookEvalWhite[y][x] if white else rookEvalBlack[y][x])
        elif piece.piece_type == 5:
            return 90 + (evalQueenWhite[y][x] if white else evalQueenblack[y][x])
        elif piece.piece_type == 6:
            return 900 + kingEvalWhite[y][x] if white else kingEvalBlack[y][x]
        else:
            return 0

    if piece.color == chess.WHITE:
        isWHITE = True
    else:
        isWHITE = False

    x = int(chess.square_file(square))
    y = int(chess.square_rank(square))
    absoluteValue = getAbsoluteValue(piece, isWHITE, x, y)
    return absoluteValue if isWHITE else -absoluteValue


if __name__ == "__main__":
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    v = respond_to(fen)
    print(v)
