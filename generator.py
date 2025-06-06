# Grid size (Not needed from)
size = 4

from math import sqrt

def print_moves(move_list):
    for i in move_list:
        print(i)

def multis(num:str):
    

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
    rows = split_into_rows(num)
    for row in rows:
        if row.count("1") < 2:
            continue
        else:
            horiz += multis(row)
    return horiz


#################################
#           Vertical            #
#################################

def split_into_columns(num:str):
    verts = [""]*size
    pass

def verticals(num:str):
    vert = []
    verts = split_into_columns(num)
    for vert in verts:
        if row.count("1") < 2:
            continue
        else:
            vert += multis(row)
    return vert


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