import gol

import gol

def test_display_dead():
    board = [[0, 0, 0],[0,0,0],[0,0,0]]
    expected_output = '***\n***\n***'
    assert gol.display_board(board) == expected_output

def test_display_alive():
    board = [[1,1,1],[1,1,1],[1,1,1]]
    expected_output = '###\n###\n###'
    assert gol.display_board(board) == expected_output