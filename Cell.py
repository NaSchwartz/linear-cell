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
        print("invalid entry. Unrecognizable string, or incorrect size")
    if input("type \'q\' to quit:\t") == "q":
        break