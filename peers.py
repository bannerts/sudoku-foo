# peers.py
# taken from http://norvig.com/sudoku.html

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)    # all squares

# unitlist ~ returns a list of all units (as lists)
#   [ ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'],
#     ['A2', 'B2', 'C2', 'D2', 'E2', 'F1', 'G2', 'H2', 'I2'],
#     ..
#     ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'],
#     ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'],
#     ..
#     ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3'],
#     ['A4', 'A5', 'A6', 'B4', 'B5', 'B6', 'C4', 'C5', 'C6']
#     .. 
unitlist = ([cross(rows, c) for c in cols] + 
            [cross(r, cols) for r in rows] + 
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

# units ~ maps each square (ie 'F6') to its units (using a dictionary)
#   each square is mapped to 3 units
#   {'A1': [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'],
#           ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'],
#           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
#    'B1': ..
#    ...}
units = dict((s, [u for u in unitlist if s in u]) 
             for s in squares)

# peers ~ maps each square to its peers (as a set) using a dictionary
#  {'A1': set(['A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 
#              'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1',
#              'B2', 'C2', 'B3', 'C3']),
#   'B1': .. 
#    ...}
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

