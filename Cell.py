# Ignore this

import sys
import Tools
# arrays where each entry takes up a single bit
# from bitarray import bitarray

#bits = bitarray('00101101') 
#print(bits)

#Tools.optimal_move("100111111")

#ol.(

while True:
    # Standard analyzing loop
    cells = input("Please enter state to analyze:\t")
    try:
        Tools.optimal_move(cells)
    except:
        print("\ninvalid entry. Unrecognizable string, or incorrect size\n")
    
    # post-analyzation, fun visuals and useful records for the user
    try:
        u_inp = input("type \'q\' to quit, \'m\' to see the memory, or \'p\' to see all p-positions found so far:\t")
        if u_inp == "q":
            break
        elif u_inp == "m":
            print()
            print(Tools.memo)
            print()
        elif u_inp == "p":
            cells_cnt =input("type the minimum number of cells to be in each state (default 0):\t")
            print()
            if not cells_cnt.strip():
                cells_cnt = "0"

            Tools.print_p_pos_cells(int(cells_cnt), input("type \'v\' to see visuals:\t")=="v")
    except:
        print("\ninvalid entry.\n")