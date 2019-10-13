#!/usr/bin/python
import chess
import agent_naive # this is black
import agent  # this is white

def main():
    board = chess.Board()
    turn = 0 # white is 0 , black is 1
    while(not board.is_game_over()):
        if turn == 0:
            move = agent_naive.respond_to(board.fen())
            board.push(chess.Move.from_uci(move))
            print("---------------------------The white move:-------------------")
            print(board)
            turn = 1
        else :
            move = agent.respond_to(board.fen())
            board.push(chess.Move.from_uci(move))
            print("---------------------------The black move:-------------------")
            print(board)
            turn = 0
    # if the status is drawn, it will not be shown.
    fen = board.fen()
    sections = fen.split()
    if int(sections[4]) >= 50:
        print("A draw have been made! ")
        print("Game is over!")
        exit(0)
    if turn == 0:
        print("The black side wins the game!")
    else :
        print("The white side wins the game!")
    print("Game is over!")
main()
