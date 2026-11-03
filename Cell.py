import sys, os, time, threading, traceback
import printing, Tools

# print(int("10111",2))
# sys.exit()

def standard_analyzing_loop(memory):
    # Standard analyzing loop
        state = input(f"Please enter a(n) {m} by {n} state to find the optimal move for:\t")
        try:
            Tools.optimal_move(state, m,n, memory)
        except Exception as e:
            print("\nInvalid entry. Unrecognizable string, or incorrect dimensions\n")
            traceback.print_exc()
            sys.exit()

################################
# Main

if __name__ == "__main__":
    memory = None

    while True:
        # change the grid dimensions
        try:
            m = int(input("Enter the number of rows in the grid:\t"))
            if m < 1:
                raise Exception("")
            n = int(input("Enter the number of columns in the grid:\t"))
            if n < 1:
                raise Exception("")
        except:
            print("\nInvalid entry. dimensions must be natural numbers\n")
            continue
        
        # create memory and Cell.py memory """pointer"""
        memory = Tools.create_memory(m,n)

        # User enters a state, analyze it
        standard_analyzing_loop(memory)
        
        # post-analyzation, fun visuals and useful records for the user
        while True:
            u_inp = input("Post-analyzation. Enter a number to select that option, all other entires will restart the main loop.\n"
            +"[ 0 ] List searching statistics\n"
            +"[ 1 ] Check if a state is an N/P-position\n"
            +"[ 2 ] Find the optimal move for a state\n"
            +"[ 3 ] See current memory\n"
            +"[ 4 ] Analyze ALL REMAINING STATES for this grid type\n"
            +"[ 5 ] See all P-positions found so far\n"
            +"[ 6 ] Export all knonw P-positions to a text file\n"
            +"[ 7 ] Generate a randdom state for these grid dimensions\n"
            +"[ 8 ] Reset memory (clear all bits)\n"
            +"[ 9 ] Exit program\n"
            +"\nChoice:\t")
            os.system("clear")
            match (u_inp):
                case "0":
                    Tools.list_searching_statistics(m,n, memory)
                    print()
                case "1":
                    try:
                        state = input("Enter your state:\t")
                        printing.print_grid(state,m,n)
                        if memory[(2*int(state,2))]:
                            print("This state is a P-Position") if memory[(2*int(state,2))+1] else print("This state is an N-Position")
                        else:
                            print("This state has not been analyzed yet")
                        print()
                    except:
                        print("\nAn error occured: unrecognizable string entered.\n")
                        traceback.print_exc()
                case "2":
                    standard_analyzing_loop(memory)
                case "3":
                    print("0 = N-Position, 1 = P-Position")
                    print(memory)
                    print()
                case "4":
                    print()
                    print("Please be patient, this may take some time...")
                    start = time.perf_counter()
                    try:
                        Tools.analyze_all_states(m,n, memory)
                        end = time.perf_counter()
                        print(f"Elapsed time: {end - start:.5f}seconds\n")
                    except:
                        print("\nWARNING Something went wrong (you probably interupted the process)\n")
                        traceback.print_exc()
                    print("Done!")
                    print()
                case "5":
                    cells_cnt = input("type the minimum number of cells to be in each state (default 0):\t")
                    print()
                    if not cells_cnt.strip():
                        cells_cnt = "0"
                    # Either display binary encodings or the pictures.
                    Tools.print_p_pos_cells(m,n, memory, int(cells_cnt), input("type \'v\' to see visuals:\t")=="v")
                    print()
                case "6":
                    filename = input("Enter the name of your text file (inclucde \".txt\"):\t")
                    print()
                    Tools.export_p_positions_txt(m,n, filename, input("Enter the delimiter to use:\t"), memory)
                    print()
                case "7":
                    state = Tools.random_state(m,n)
                    printing.print_grid(state,m,n)
                    print()
                case "8":
                    Tools.reset_memory(memory)
                case "9":
                    sys.exit()
        
    Tools.wipe_memory(memory)