import generator, symmetry
from printing import print_grid

#######################################
#           Move Generation           #
#######################################

def generate_moves(num : str, size : int):
    moves = set()
    # singles
    moves.update(generator.singles_list(num))
    # horizontals
    moves.update(generator.horizontals(num, size))
    # verticals
    moves.update(generator.verticals(num, size))
    # diaganols - not yet installed
    moves.update(generator.diaganols(num, size))
    # diaganols - not yet installed
    moves.update(generator.anti_diaganols(num, size))
    return moves

# print(generate_moves("1100110000000000")) # should have 9 things (not counting anti diags)

memo = {}


#######################################
#        Symetry Optimization         #
#######################################


def is_this_in_memo(num : str):
    return memo.get(num)

def symmetry_check(num : str, size : int):
    rotations = symmetry.normal_forms(num, size)
    for i in rotations:
        output = is_this_in_memo(i)
        if output != None:
            return (output, i)
    return None

#print(symmetry.normal_forms("0001"))
#print(symmetry_check("0001"))
#print(symmetry_check("0110"))

#######################################
#            Common States            #
#######################################

# Enter known N/P-positions into memory
def enter_commons(): 
    # False = N-pos     True = P-pos
    memo.update({"1011": False})
#enter_commons()


# Reduce a given state using isomorphisms       [DO THIS OPTIIZATION LAST!]
    # changes states into a single cannonical state
    # Ex: all C4 states -> ONE type of C4

def is_p_position(num:str, size:int):
    
    # First and foremost, check memory for symmetrical states
    symm = symmetry_check(num, size)
    if symm != None:
        #print("time saved")
        memo[symm[1]] = symm[0] 
        return symm[0]

    # Firstly, check memo if already known
    #temp = memo.get(num)
    #if temp != None:
    #    print("time saved")
    #    return temp

    # base case: P-position
    if num == "0"*size**2:
        return True
    # base case: N-position
    elif num.count("1") == 1:
        return False
    else:
        # if all moves are N-positions, it's a P-position
        # if 1 move is a P-position, it's an N-position
        # Disclaimer: AI helped me with the next line because PAIN
        result = not any(is_p_position(state, size) for state in generate_moves(num, size))

        # Before we return, we should store the result into the memory
        memo[num] = result
        return result

# for testing purposes only
def np_pos(num:str, size:int):
    print_grid(num)
    if is_p_position(num, size):
        print("P-position\n")
        return True
    else:
        print("N-position\n")
        return False

# main function to be used
def optimal_move(state:str, size:int):
    # First check if this is in the memory already
    if state in memo:
        if memo[state]:
            print("\nThis P-position is in the memory already!\n")
        else:
            print("\nThis N-position is in the memory already!\n")
        return

    # Otherwise do the depth first search
    for state in generate_moves(state, size):
        #print(generate_moves(state))
        if np_pos(state, size):
            print("You are in an N-Position! The move directy above is a P-position")
            return
    print("You are in a P-position! If it's you're turn, you're losing :(")



#print_grid("111010001")
#generator.split_into_diags("101010110")
#np_pos("1111")

#optimal_move("111111111")
#print(memo)


#######################################
#            Memory Tools             #
#######################################

def print_p_pos():
    for state in memo:
        if memo[state]:
            print(state)

def print_p_pos_states():
    for state in memo:
        if memo[state]:
            print_grid(state, False)

def print_p_pos_cells(cell_cnt=0, visuals = False):
    for state in memo:
        if state.count("1")>=cell_cnt:
            if memo[state]:
                if visuals:
                    print_grid(state, False)
                else:
                    print(state)

def clear_memory():
    memo.clear()

#######################################
#            Miscellaneous            #
#######################################

import random

def random_state(size):
    state = ""
    for i in range(size**2):
        state += str(random.randint(0, 1))
    return state