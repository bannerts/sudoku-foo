# display.py
# taken from http://norvig.com/sudoku.html

import peers as p
# import grid as g

def display(values):
    "Display these values as a 2-D grid."
    width = 1 + max(len(values[s]) for s in p.squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in p.rows:
        print ''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in p.cols)
        if r in 'CF': print line
    print
