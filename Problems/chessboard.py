# List cs contains the N widths of the N columns of the chessboard
# List rs contains the N heights of the N rows of the chessboard
# Remember, board coloring starts with top left cell => WHITE
# and then alternates with BLACK as in a usual chessboard.
def white_black_areas(cs, rs):
    # return a 2-element tuple, (total_white_area, total_black_area)
    whole = sum(cs) * sum(rs)
    even_row = rs[0::2]
    odd_row = rs[1::2]
    even_column = cs[0::2]
    odd_column = cs[1::2]
    res = sum(even_row) * sum(odd_column) + sum(odd_row) * sum(even_column)
    return whole - res, res
print(white_black_areas([3,1,2,7,1],[1,8,4,5,2]))