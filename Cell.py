import sys, os, traceback, printing, Tools

# print(int("10111",2))
# sys.exit()

def standard_analyzing_loop(memory):
    # Standard analyzing loop
        state = input(f"Please enter state to analyze (size: {size}):\t")
        try:
            Tools.optimal_move(state, size, memory)
        except Exception as e:
            print("\ninvalid entry. Unrecognizable string, or incorrect size\n")
            traceback.print_exc()
            sys.exit()

################################
# Main

if __name__ == "__main__":
    memory = None

    while True:
        # change the grid size
        try:
            size = int(input("Enter the side length of the square grid:\t"))
            if size < 1:
                raise Exception("")
        except:
            print("\ninvalid entry. size must be a natural number\n")
            continue
        
        # create memory and Cell.py memory """pointer"""
        memory = Tools.create_memory(size)

        # User enters a state, analyze it
        standard_analyzing_loop(memory)
        
        # post-analyzation, fun visuals and useful records for the user
        while True:
            u_inp = input("Post-analyzation. Enter a number to select that option, all other entires will restart the main loop.\n"
            +"[ 0 ] List searching statistics\n"
            +"[ 1 ] Analyze a new state\n"
            +"[ 2 ] See current memory\n"
            +"[ 3 ] Analyze ALL REMAINING STATES for this grid size\n"
            +"[ 4 ] See all P-positions found so far\n"
            +"[ 5 ] Export all knonw P-positions to a text file\n"
            +"[ 6 ] Generate a randdom state for this size\n"
            +"[ 7 ] Reset memory (clear all bits)\n"
            +"[ 8 ] Exit program\n"
            +"\nChoice:\t")
            #####os.system("clear")
            match (u_inp):
                case "0":
                    Tools.list_searching_statistics(size, memory)
                    print()
                case "1":
                    standard_analyzing_loop(memory)
                case "2":
                    print("0 = N-Position, 1 = P-Position")
                    print(memory)
                    print()
                case "3":
                    print()
                    print("Please be patient, this may take some time...")
                    try:
                        Tools.analyze_all_states(size, memory)
                    except:
                        print("\nWARNING Something went wrong (you probably interupted the process)\n")
                        traceback.print_exc()

                    print("Done!")
                    print()
                case "4":
                    cells_cnt = input("type the minimum number of cells to be in each state (default 0):\t")
                    print()
                    if not cells_cnt.strip():
                        cells_cnt = "0"
                    # Either display binary encodings or the pictures.
                    Tools.print_p_pos_cells(size, memory, int(cells_cnt), input("type \'v\' to see visuals:\t")=="v")
                    print()
                case "5":
                    filename = input("Enter the name of your text file (inclucde \".txt\"):\t")
                    print()
                    Tools.export_p_positions_txt(size, filename, input("Enter the delimiter to use:\t"), memory)
                    print()
                case "6":
                    state = Tools.random_state(size)
                    printing.print_grid(state)
                    print()
                case "7":
                    Tools.reset_memory(memory)
                case "8":
                    sys.exit()
                case _:
                    break
        
    Tools.wipe_memory(memory)