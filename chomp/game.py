

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
    return new_rows


def get_situation(rows):
    if rows == [1]:
        return 'L'
    return 'W'