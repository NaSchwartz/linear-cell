# Grid size (Not needed from)
size = 3

from math import sqrt
from itertools import combinations
from symmetry import positive_rotation, negative_rotation

def print_moves(move_list):
    for i in move_list:
        print(i)

def multis(num:str):
    # Consturction of positions of the ones list
    ones = []
    i = 0
    for ch in num:
        if ch == "1":
            ones.append(i)
        i += 1
    
    # Set of unique unordered elements 
    moves = set()

    # Combinatorics :D
    for i in range(2,len(ones)+1,1):
        for comb in combinations(ones, i):
            temp = list(num)
            for j in comb:
                temp[j] = "0"
            
            moves.add(''.join(temp))
    return sorted(moves)

#################################
#           Singles             #
#################################

def singles(num:str):
    index = 0
    desc = ""
    for ch in num:
        if ch == "1":
            print(num[:index]+"0"+num[index+1:])
        else:
            desc += ch
        index += 1
    
def singles_list(num:str):
    moves = []
    index = 0
    desc = ""
    for ch in num:
        if ch == "1":
            moves.append(num[:index]+"0"+num[index+1:])
        else:
            desc += ch
        index += 1
    return moves


#################################
#           Horizontal          #
#################################

def split_into_rows(num:str):
    rows = [""]*size
    for i in range(size):
        rows[i] = num[i*size:i*size+size]
    return rows

def horizontals(num:str):
    horiz = []
    # split the binary string into rows
    rows = split_into_rows(num)
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
                horiz.append("".join(copy_rows))
        
        inc += 1

    return horiz

#print(split_into_rows("111111111"))
#print(horizontals("111111111"))
#print(multis("111"))


#################################
#           Vertical            #
#################################

def verticals(num:str):
    num2 = positive_rotation(num)
    temp = horizontals(num2)
    vert = []
    for grid in temp:
        vert.append(negative_rotation(grid))
    return vert

#print(horizontals("001001001"))
#print(verticals("001001001"))
#print(multis("111"))


#################################
#           Diaganol            #
#################################

def split_into_diags(num:str):
    diags = [""]*size
    pass

def diaganols(num:str):
    diags = []
    diags = split_into_diags(num)
    for diag in diags:
        if row.count("1") < 2:
            continue
        else:
            diags += multis(diag)
    return diags