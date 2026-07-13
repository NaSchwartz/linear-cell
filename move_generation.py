# math
from math import sqrt
from itertools import combinations
# symmetry
from symmetry import positive_rotation, negative_rotation
import symmetry
# testing + printing
from printing import print_grid, print_moves

#################################
# Multiple Cell Moves

def multis(num:str):
    # Consturction of positions of the ones list
    ones = []
    i = 0
    for ch in num:
        if ch == "1":
            ones.append(i)
        i += 1

    # Combinatorics :D
    for i in range(2,len(ones)+1,1):
        for comb in combinations(ones, i):
            temp = list(num)
            for j in comb:
                temp[j] = "0"
            
            yield ''.join(temp)

#################################
# Single Moves

def singles_generator(num:str):
    index = 0
    desc = ""
    for ch in num:
        if ch == "1":
            yield num[:index]+"0"+num[index+1:]
        else:
            desc += ch
        index += 1

#################################
# Horizontal Moves

# split number into rows, O(size) work
def split_into_rows(num:str, size):
    rows = [""]*size
    for i in range(size):
        rows[i] = num[i*size:i*size+size]
    return rows

def horizontal_generator(num:str, size): 
    # split the binary string into rows
    rows = split_into_rows(num, size)
    inc = 0
    for row in rows:
        if row.count("1") < 2:
            inc += 1
            continue
        else:
            # create the moves for each row
            for comb in multis(row):
                #print(comb)
                # smash the combinations back into the other rows
                copy_rows = rows.copy()
                copy_rows[inc] = comb
                yield "".join(copy_rows)
        
        inc += 1

#################################
# Vertical Moves

def vertical_generator(num:str, size:int):
    # rotate number
    num2 = positive_rotation(num, size)
    # apply horizontal moves
    for state in horizontal_generator(num2, size):
        # rotate back and yield return
        yield negative_rotation(state, size)

#################################
# Diagonal Moves

# Transform diagonals into rows
def apply_isomorphism(number:str, size:int) -> str:
    new_number = ""
    msize = 2*size-1
    counter = 0
    for i in range(size**2):
        if counter != 0 and counter % size == 0:
            new_number += "0" * size

        new_number += number[i]
        counter += 1

    new_number += "0" * (msize * (size-1))

    return new_number

# Transform transformed diagonals into diagonals
def undo_isomorphism(number:str, size:int) -> str:
    new_number = ""
    msize = 2*size-1
    i = 0
    loop_counter = 0
    while loop_counter < size:
        for j in range(size):
            new_number += number[i]
            i += 1
        loop_counter += 1
        i += size

    return new_number

def diagonal_generator(number:str, size:int):
    # transform number
    new_number = apply_isomorphism(number, size)
    # apply vertical moves
    for state in vertical_generator(new_number, 2*size-1):
        # transform back and yield return
        yield undo_isomorphism(state, size)

def anti_diagonal_generator(number:str, size:int):
    # transform number
    new_number = apply_isomorphism(positive_rotation(number,size), size)
    # apply vertical moves
    for state in vertical_generator(new_number, 2*size-1):
        # transform back and yield return
        yield negative_rotation(undo_isomorphism(state, size),size)