# non-attacking queens. Write a program to find positions for n queens on chessboard of size s,
# such that no queen can attack any other queen.

def Queen(q: int, s: int):
    board = [[0 for j in range(0,s)] for i in range(0,s)]
    print(board)
    for j in board:
        board[j]







def main():
    q = 4
    s = 3
    Queen(q,s)


if __name__ == '__main__':
    main()