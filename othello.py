# -*- coding:utf-8 -*-

class Board:
    # BLANK = 0
    # BLACK = 1
    # WHITE = -1

    def __init__(self):
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[3][3] = board[4][4] = 1
        board[3][4] = board[4][3] = -1

    def print_board(self):
        print(' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        for x in board:
            for y in board:
                if y == 0:
                    print('-', )
                elif y == 1:
                    print('●, ')
                elif y == -1:
                    print('○', )
            print('\n')

def main():
    board = Board()
    board.print_board

if __name__ == __main__:
    main()
