

# def play(rows, next_player):
#     if rows == [1]:
#         return "{} loses".format(next_player)

#def play(rows):
#    if

def get_moves(rows):
    moves = []
    for row in range(1, len(rows)+1):
        for col in range(1, rows[row-1]+1):
            if row != 1 or col != 1:
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
    #print("get_situation({})".format(rows))
    if rows in situations:
        #print("Response is {}".format(situations[rows]))
        return situations[rows]

    for this_move in get_moves(rows):
        new_rows = move(rows, this_move)
        #print("Checking rows {} using move {} to get to {}".format(rows, this_move, new_rows,))
        if new_rows not in situations:
            situations[new_rows] = get_situation(new_rows)

        if situations[new_rows] == 'L':
            situations[rows] = 'W'
            break
    else:
        situations[rows] = 'L'

    #print("Response is {}".format(situations[rows]))
    return situations[rows]


def show_losing_situations(cols_n, rows_n):
    starting_rows = tuple([cols_n] * rows_n)
    situation = get_situation(starting_rows)
    print("This is a {} gane for the first mover".format(situation))
    print("You need to reach one of the following situations and then stick to these situations in order to win the game.")
    for rows in situations:
        if situations[rows] == 'L':
            print(rows)

if __name__ == '__main__':
    import sys
    show_losing_situations(int(sys.argv[1]), int(sys.argv[2]))
