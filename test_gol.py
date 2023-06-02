import gol

def test_display_dead():
    board = [[0, 0, 0],[0,0,0],[0,0,0]]
    expected_output = '***\n***\n***'
    assert gol.display_board(board) == expected_output

def test_display_alive():
    board = [[1,1,1],[1,1,1],[1,1,1]]
    expected_output = '###\n###\n###'
    assert gol.display_board(board) == expected_output

def test_next_live_or_dead():
    sample_board = [[0,1,0],[0,0,1],[1,1,1]]
    expected_board = [[0,0,0],[1,0,1],[0,1,1]]
    assert gol.next_generation(sample_board) == expected_board

def test_nieghbours_live_dead():
    board = [[0,1,0],[0,1,0],[0,1,0]]
    assert gol.count_live_dead_neighbors(board,1,1) == 2