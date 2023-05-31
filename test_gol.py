

def test_display():
    
    game =[[1,0,0],[1.0,0],[1,0,0]]
    expected_output = "# - - \n# - - \n# - - \n"
    next_output = next_gen(game)
    assert next_output == expected_output, "Test case 1 failed"
    




# # Function to test the next_generation() function
# def test_game_of_life():
#     # Test case 1: Blinker
#     grid = [[0, 1, 0],
#             [0, 1, 0],
#             [0, 1, 0]]

#     expected_next_gen = [[0, 0, 0],
#                          [1, 1, 1],
#                          [0, 0, 0]]

#     next_gen = next_generation(grid)
#     assert next_gen == expected_next_gen, "Test case 1 failed"

#     # Test case 2: Block
#     grid = [[1, 1, 0],
#             [1, 1, 0],
#             [0, 0, 0]]

#     expected_next_gen = [[1, 1, 0],
#                          [1, 1, 0],
#                          [0, 0, 0]]

#     next_gen = next_generation(grid)
#     assert next_gen == expected_next_gen, "Test case 2 failed"

#     # Test case 3: Glider
#     grid = [[0, 0, 1],
#             [1, 0, 1],
#             [0, 1, 1]]

#     expected_next_gen = [[0, 1, 0],
#                          [0, 0, 1],
#                          [1, 1, 1]]

#     next_gen = next_generation(grid)
#     assert next_gen == expected_next_gen, "Test case 3 failed"

#     print("All test cases passed!")


