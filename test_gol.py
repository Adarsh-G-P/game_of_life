import gol

import gol

def test_display_dead():
    board = [[0, 0, 0],[0,0,0],[0,0,0]]
    expected_output = '***\n***\n***'
    assert gol.display_board(board) == expected_output

