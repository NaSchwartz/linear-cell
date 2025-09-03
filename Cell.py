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
    cells = input("Please enter state to analyze:\t")
    try:
        Tools.optimal_move(cells)
    except:
        print("\ninvalid entry. Unrecognizable string, or incorrect size\n")
    
    u_inp = input("type \'q\' to quit or type \'m\' to see the memory:\t")
    if u_inp == "q":
        break
    elif u_inp == "m":
        print()
        print(Tools.memo)
        print()