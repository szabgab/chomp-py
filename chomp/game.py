

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

def move(rows, this_move):
    m_row, m_col = this_move

    if len(rows) < m_row:
        raise Exception
    if rows[m_row-1] < m_col:
        raise Exception

    new_rows = []
    for row in range(1, len(rows)+1):
        if row < m_row:
            new_rows.append(rows[row - 1])
            continue
        if m_col == 1:
            break
        if rows[row - 1] >= m_col:
            new_rows.append(m_col-1)
        else:
            new_rows.append(rows[row - 1])
    return tuple(new_rows)

situations = {}
situations[ (1,) ] = 'L'


# find all the possible moves, if any of them leads to a Losing situation then this is a Winning situation
# Otherwise it is itself a Losing situation
def get_situation(rows):
    if rows in situations:
        return situations[rows]
    for this_move in get_moves(rows):
        new_rows = move(rows, this_move)
        if new_rows not in situations:
            situations[new_rows] = get_situation(new_rows)

        if situations[new_rows] == 'L':
            situations[rows] = 'W'
            return 'W'
    return 'L'

