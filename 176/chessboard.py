WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for i in range(size):
        pattern = WHITE + BLACK
        if i % 2:
            pattern = pattern[::-1]
        print(pattern * int(size / 2))
