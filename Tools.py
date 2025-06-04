# Grid size
size = 4

def print_grid(number : int = 0, N = size):
    # convert number to binary
    num = str(bin(number))[2:]
    # Add trailing zeros
    num = "0"*(N**2 - len(num)) + num

    cells = ["\u00B7", "\u25A1"]
    desc = ""
    counter = 0

    # Convert binary string to grid
    for i in range(len(num)-1,-1,-1):
        desc += cells[int(num[i])] + " "
        counter += 1
        if counter%N == 0 and counter !=N**2:
            desc+= "\n"
    print(num)
    print(desc)

def in_range(num):
    return 0 <= num <= size**2

# Generate all posible moves (print/return a list of states in binary)
    # singles, n-tuples, splits
    # horizontal, vertical, diaganol