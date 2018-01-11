import chomp

def test_chomp():
    assert chomp.game.get_situation([1]) == 'L'
    assert chomp.game.get_situation([1, 1]) == 'W'
#    assert chomp.game.get_situation([2, 1]) == 'L'

    #assert chomp.play([1], "Computer") == 'Computer loses'
    #assert chomp.play([1], "Human") == 'Human loses'
    #assert chomp.play([2], "Computer") == "Take row 1 col 2"

    assert  set([(1, 1)]) == set(chomp.game.get_moves([1]))
    assert  set([(1, 1), (2, 1)]) == set(chomp.game.get_moves([1, 1]))
    assert  set([(1, 1), (2, 1), (1, 2)]) == set(chomp.game.get_moves([2, 1]))
    assert  set([(1, 1), (2, 1), (1, 2), (2, 2)]) == set(chomp.game.get_moves([2, 2]))
