# Grid size (Not needed from)
size = 4

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

def pyramid(height:int):
    flag = False
    inc = 0
    alist = [0]*(height+height-1)
    for i in range(height+height-1):
        if i == height:
            flag = True
            inc += 1
        if flag:
            alist[i] = i - inc
            inc += 2
        else:
            alist[i] = i + 1
    return alist

def corner(length:int):
    alist = [0]*(length+length-1)
    j = 0
    for i in range(length+length-1):
        if i < length:
            alist[i] = length-1-i
        else:
            alist[i] = length*(j+1)
            j += 1
    return alist

def in_range(num:int):
    return 0 <= num <= size**2


def split_into_diags(num:str):
    # Indexing useful stuff
    diags = [""]*(size+size-1)
    ranges = pyramid(size)
    corn = corner(size)
    #print(corner(4))
    #print(ranges)
    
    # Putting it all together
    for i in range(len(diags)):
        increment = 0
        for j in range(ranges[i]):
            diags[i]+=num[corn[i]+increment]
            increment += size + 1
    return diags

#WIP
def diaganols(num:str):
    total = []
    # split the binary string into rows
    diags = split_into_diags(num)
    inc = 0
    for diag in diags:
        if diag.count("1") < 2:
            inc += 1
            continue
        else:
            # create the moves for each row
            for comb in multis(diag):
                #print(comb)
                # smash the combinations back into the other rows
                pass
        
        inc += 1

    return total

print(split_into_diags("011S10011001F110"))