## grid.py
## taken from http://norvig.com/sudoku.html

import peers as p

def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, p.digits) for s in p.squares)
    ## s ~ squares (ie. A1)
    ## d ~ string of digits (ie. '1234')
    for s, d in grid_values(grid).items():
        if d in p.digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    return values

def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in p.digits or c in '0.']
    assert len(chars) == 81
    # Assign each square to either a value (1,2,...,9 or 0,.)
    return dict(zip(p.squares, chars)) 

#  Constraint Propagation
#       (1) If a square has only one possible value, then eliminate that value from the square's peers. 
#       (2) If a unit has only one possible place for a value, then put the value there.

def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
	    return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in p.peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in p.units[s]:
	    dplaces = [s for s in u if d in values[s]]
	    if len(dplaces) == 0:
	        return False ## Contradiction: no place for this value
	    elif len(dplaces) == 1:
             if not assign(values, dplaces[0], d):
                 return False
    return values
    
