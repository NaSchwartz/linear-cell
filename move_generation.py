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

# split number into rows, O(max{m,n}) work
def split_into_rows(num:str, m,n):
    rows = [""]*m
    for i in range(m):
        rows[i] = num[i*n:i*n+n]
    return rows

def horizontal_generator(num:str, m,n): 
    # split the binary string into rows
    rows = split_into_rows(num, m,n)
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

def vertical_generator(num:str, m:int, n:int):
    # rotate number
    num2,m,n = positive_rotation(num, m,n)
    # apply horizontal moves
    #print(num,num2)
    for state in horizontal_generator(num2, m,n):
        # rotate back and yield return
        yield negative_rotation(state, m,n)[0]

#################################
# Diagonal Moves

# Transform diagonals into columns
def apply_isomorphism(number:str, m:int, n:int) -> (str,int,int):
    new_number = ""
    msize = n + m-1
    counter = 0
    for i in range(m*n):
        if counter != 0 and counter % n == 0:
            new_number += "0" * m

        new_number += number[i]
        counter += 1

    return (new_number, m, n+m-1)

# Transform transformed diagonals into diagonals
def undo_isomorphism(number:str, m:int, n:int) -> (str,int,int):
    #print(number,m,n)
    new_number = ""
    msize = n + m-1
    i = 0
    loop_counter = 0
    while loop_counter < m:
        for j in range(n-m+1):
            #print(i, loop_counter)
            new_number += number[i]
            i += 1
        loop_counter += 1
        i += m

    return (new_number, m, n-m+1)

#num = "10011111"
#m,n = (2,4)
#print_grid(num,m,n)
#num,m,n = apply_isomorphism(num,m,n)
#print_grid(num,m,n)
#num,m,n = undo_isomorphism(num,m,n)
#print_grid(num,m,n)

def diagonal_generator(number:str, m:int, n:int):
    # transform number
    new_number,m,n = apply_isomorphism(number, m,n)
    # apply vertical moves
    for state in vertical_generator(new_number, m, n):
        # transform back and yield return
        yield undo_isomorphism(state, m,n)[0]

def anti_diagonal_generator(number:str, m:int, n:int):
    # transform number
    number,m,n = positive_rotation(number,m,n)
    new_number,m,n = apply_isomorphism(number,m,n)
    # apply vertical moves
    canonnical = (m,n)
    for state in vertical_generator(new_number, m,n):
        #Reset m,n because n looses two after each run in the vertical generator somehow 
        m,n = canonnical
        # transform back and yield return
        #print(f"pre:{state}, dim: {m,n}")
        state,m,n = undo_isomorphism(state, m,n)
        #print(f"undo:{state}, dim: {m,n}")
        yield negative_rotation(state, m, n)[0]

#for i in anti_diagonal_generator("111110101",3,3):
#    2 == 2

#print(undo_isomorphism("101000100000011",3,5))