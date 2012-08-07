# solve.py
# taken from http://norvig.com/sudoku.html

import peers as p
import grid as g
import display as d

def solve(grid): return search(g.parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in p.squares): 
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n, s = min((len(values[s]), s) for s in p.squares if len(values[s]) > 1)
    return some(search(g.assign(values.copy(), s, d)) 
		for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

def solution(grid):
    vals = solve(grid)
    d.display(vals)
