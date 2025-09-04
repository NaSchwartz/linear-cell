import generator, symmetry
from printing import print_grid, set_size

# Grid size
size = set_size()

#######################################
#           Move Generation           #
#######################################

def generate_moves(num : str):
    moves = set()
    # singles
    moves.update(generator.singles_list(num))
    # horizontals
    moves.update(generator.horizontals(num))
    # verticals
    moves.update(generator.verticals(num))
    # diaganols - not yet installed
    moves.update(generator.diaganols(num))
    # diaganols - not yet installed
    moves.update(generator.anti_diaganols(num))
    return moves

# print(generate_moves("1100110000000000")) # should have 9 things (not counting anti diags)

memo = {}


#######################################
#        Symetry Optimization         #
#######################################


def is_this_in_memo(num : str):
    return memo.get(num)

def symmetry_check(num : str):
    rotations = symmetry.normal_forms(num)
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

def is_p_position(num:str):
    
    # First and foremost, check memory for symmetrical states
    symm = symmetry_check(num)
    if symm != None:
        print("time saved")
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
        result = not any(is_p_position(state) for state in generate_moves(num))

        # Before we return, we should store the result into the memory
        memo[num] = result
        return result

# for testing purposes only
def np_pos(num:str):
    print_grid(num)
    if is_p_position(num):
        print("P-position\n")
        return True
    else:
        print("N-position\n")
        return False

# main function to be used
def optimal_move(p_pos:str):
    for state in generate_moves(p_pos):
        print(generate_moves(state))
        if np_pos(state):
            print("Done!")
            return
    print("You are in a P-position! :( So much wasted time and computation!")



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