# Grid size
size = 3

import generator, symmetry

# Base 10 version
def print_grid(number : int = 0, N = size):
    # convert number to binary
    num = str(bin(number))[2:]
    # Add trailing zeros
    num = "0"*(N**2 - len(num)) + num

    cells = ["\u00B7", "\u25A1"]
    desc = ""
    counter = 0

    # Convert binary string to grid
    for i in range(len(num)-1,-1,-1):
        desc += cells[int(num[i])] + " "
        counter += 1
        if counter%N == 0 and counter !=N**2:
            desc+= "\n"
    print(num)
    print(desc)
#Binary version
def print_grid(num : str, N = size):
    cells = ["\u00B7", "\u25A1"]
    desc = ""
    counter = 0

    for i in range(len(num)-1,-1,-1):
        desc += cells[int(num[i])] + " "
        counter += 1
        if counter%N == 0 and counter !=N**2:
            desc+= "\n"
    print(num)
    print(desc)


def generare_moves(num : str) -> str :
    moves = set()
    # singles
    moves |= generator.singles_list(num)
    # horizontals
    moves |= generator.horizontal(num)
    # verticals
    moves |= generator.vertical(num)
    # diaganols
    moves |= generator.diaganols(num)
    return moves

memo = {}

# Enter known P-positions into memory           [DO THIS OPTIIZATION LATER]
    # the null position, D2, C3, C4, etc
    # When doing so, use next two functions

# Reduce a given state using symmetry           [DO THIS OPTIIZATION LATER]
    # changes states into a single cannonical state
    # flipping, rotating, and translating

# Reduce a given state using isomorphisms       [DO THIS OPTIIZATION LAST!]
    # changes states into a single cannonical state
    # Ex: all C4 states -> ONE type of C4

# Given a state number, recursively check for N/P positions
    # P if all moves in a state lead to N
    # N if one move in a state leads to P

print_grid("111010001")
generator.split_into_diags("101010110")