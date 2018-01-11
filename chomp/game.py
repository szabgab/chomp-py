

# def play(rows, next_player):
#     if rows == [1]:
#         return "{} loses".format(next_player)

#def play(rows):
#    if

def get_moves(rows):
    moves = []
    for row in range(1, len(rows)+1):
        for col in range(1, rows[row-1]+1):
            moves.append((row, col))
    return moves


def get_situation(rows):
    if rows == [1]:
        return 'L'
    return 'W'