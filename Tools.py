import generator, symmetry
from printing import print_grid
from bitarray import bitarray

#######################################
#           Move Generation           #
#######################################

# holy hell, turn those functions into actual generators. 
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


#######################################
#        Symetry Optimization         #
#######################################

# Check to see if a state is in the memory
def is_this_in_memo(num : str, memo):
    return memo[2*int(num,2)]

# Given a state (in str form) and it's p-pos result, store it into memory
def store_into_memory(state:str, is_p_pos:bool, memo):
    memo[(2*int(state,2))] = 1
    memo[(2*int(state,2))+1] = int(is_p_pos)

def store_rotations(state:str, size:int, is_p_pos:bool, memo):
    # Make list of all rotations
    states = [None] * 4
    for i in range(4):
        states[i] = state
        state = symmetry.positive_rotation(state, size)

    # Store rotations into memory
    for rot_state in states:
        store_into_memory(rot_state, is_p_pos, memo)

    # print("rotation time saved!")

#######################################
#            The Algorithm            #
#######################################

# Reduce a given state using isomorphisms       [DO THIS OPTIIZATION LAST!]
    # changes states into a single cannonical state
    # Ex: all C4 states -> ONE type of C4


# Determine if a board state is a p-pos, and store result into memory
def is_p_position(num:str, size:int, do_printing:bool, memo, first_memo_bypass:bool = False) -> bool:

    # Firstly, check memo if already known
    # Bypass this step if we need an optimal move for an N-posiiton already in the memory
    if not first_memo_bypass:
        
        if memo[2*int(num,2)]:
            # print("Time saved")
            return memo[(2*int(num,2))+1]
        first_memo_bypass = False

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
        result = not any(is_p_position(state, size, do_printing, memo, first_memo_bypass) for state in generate_moves(num, size))

        # Do printing if told to do so
        if do_printing:
            print_grid(num)
            if result:
                print("P-position")
            else:
                print("N-Position") 

        # Store the result into the memory
        store_into_memory(num, result, memo)
        # Store all equivalent states into memory also
        store_rotations(num, size, result, memo)
        return result

# Find the best move in the position (to reduce N-pos to P-pos)
def optimal_move(state:str, size:int, memo):
    bypass = False
    # First check if this is in the memory already
    if memo[2*int(state,2)]:
        bypass = True
        # if it's a known P-position, all done
        if memo[(2*int(state,2))+1]:
            print_grid(state)
            print("(Entered state)\n\nThis P-position is in the memory already!\n")
            return
        # if it's a known N-position, we need to find the best move

    # Otherwise call algorithm with first_memo_bypass to get optimal move
    if is_p_position(state, size, True, memo, bypass):
        print("(Entered state)\n\nYou are in a P-position! If it's you're turn in the above state, you're losing :(\n")
        return
    print("(Entered state)\n\nYou are in an N-Position! The two states above show the optimal move!\n")


#######################################
#            Memory Tools             #
#######################################

def create_memory(size:int):
    # Memory is a two bit bit array:
    # 1st bit is the "was this state analyzed" bool
    # 2nd bit it the "is this a P-position" bool
    # state n \mapsto position 2n and 2n+1
    total = 2 ** ((size**2)+1)
    memory = bitarray(total)
    return memory

def to_string(size:int, num:int):
    state = bin(num)[2:]
    return "0"*(max((size**2)-len(state),0)) + state

def print_p_pos(memo):
    i = 0
    while i < 2**((size**2)+1):
        if memo[i]:
            print(state)

# def print_p_pos_states():
#     for state in memo:
#         if memo[state]:
#             print_grid(state, False)

# def print_p_pos_cells(cell_cnt=0, visuals = False):
#     for state in memo:
#         if state.count("1")>=cell_cnt:
#             if memo[state]:
#                 if visuals:
#                     print_grid(state, False)
#                 else:
#                     print(state)

def print_p_pos_cells(size:int, memo, cell_cnt=0, visuals = False):
    i = 0
    while i < 2**((size**2)):
        if memo[2*i] and memo[(2*i)+1]:
            state = to_string(size, i)
            if state.count("1")>=cell_cnt:
                if visuals:
                    print_grid(state, False)
                else:
                    print(state)
        i += 1

# Set all bits to 0
def reset_memory(memo):
    for i in range(len(memo)):
        memo[i] = 0

# set bitarray to []
def wipe_memory(memo):
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

def analyze_all_states(size:int, memo):
    i = 0
    while i < 2**((size**2)):
        if not memo[2*i]:
            is_p_position(to_string(size, i), size, False, memo)
        i += 1

def export_p_positions_txt(size:int, filename:str, delimiter:str, memo):
    file = open(filename, 'w')
    i = 0
    while i < 2**((size**2)):
        if memo[2*i] and memo[(2*i)+1]:
            state = to_string(size, i)
            file.write(state + delimiter)
        i += 1
    file.close()

def list_searching_statistics(size:int, memo):
    p_pos_count = 0
    n_pos_count = 0
    total_states = 2**((size**2))
    i = 0
    while i < total_states:
        if memo[2*i]:
            if memo[2*i+1]:
                p_pos_count += 1
            else:
                n_pos_count += 1
        i += 1
    known_states = p_pos_count + n_pos_count
    print(f"Searching Statistics for an {size}x{size} board\n"
         +f"Total states: {total_states}\n"
         +f"States analyzed: {known_states}\n"
         +f"P-positions found: {p_pos_count}\n"
         +f"N-positions found: {n_pos_count}\n"
         +f"Trivial states skipped: {(size*size)+1}\n"
         +f"States left to analyze: {(total_states-known_states)-(size*size)-1}\n")
    # A crazy expression is used above because the states with 1 or 0 cells are skipped over.