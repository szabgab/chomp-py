import chomp

def test_chomp():
    assert chomp.game.get_situation([1]) == 'L'
    assert chomp.game.get_situation([1, 1]) == 'W'
    #assert chomp.play([1], "Computer") == 'Computer loses'
    #assert chomp.play([1], "Human") == 'Human loses'
    #assert chomp.play([2], "Computer") == "Take row 1 col 2"