import chomp

def test_get_situation():
    assert chomp.game.get_situation([1]) == 'L'
    assert chomp.game.get_situation([1, 1]) == 'W'
#    assert chomp.game.get_situation([2, 1]) == 'L'


    #assert chomp.play([1], "Computer") == 'Computer loses'
    #assert chomp.play([1], "Human") == 'Human loses'
    #assert chomp.play([2], "Computer") == "Take row 1 col 2"

def test_get_moves():
    assert  set([(1, 1)]) == set(chomp.game.get_moves([1]))
    assert  set([(1, 1), (2, 1)]) == set(chomp.game.get_moves([1, 1]))
    assert  set([(1, 1), (2, 1), (1, 2)]) == set(chomp.game.get_moves([2, 1]))
    assert  set([(1, 1), (2, 1), (1, 2), (2, 2)]) == set(chomp.game.get_moves([2, 2]))

def test_move():
    assert  [1] == chomp.game.move([5], (1, 2))
    assert  [2, 1] == chomp.game.move([2, 2], (2, 2))
    assert  [4, 2, 2, 1] == chomp.game.move([4, 3, 3, 1], (2, 3))
    assert  [3, 1, 1] == chomp.game.move([3, 3, 3], (2, 2))

    assert  [] == chomp.game.move([5], (1, 1))
    assert  [] == chomp.game.move([3, 3, 3], (1, 1))
