import sys, printing, Tools, traceback

# print(int("10111",2))
# sys.exit()

while True:
    # change the grid size
    try:
        size = int(input("Enter the side length of the square grid:\t"))
        if size < 1:
            raise Exception("")
    except:
        print("\ninvalid entry. size must be a natural number\n")
        continue
    
    # Standard analyzing loop
    state = input(f"Please enter state to analyze (size: {size}):\t")
    try:
        Tools.optimal_move(state, size)
    except Exception as e:
        print("\ninvalid entry. Unrecognizable string, or incorrect size\n")
        traceback.print_exc()
        #sys.exit()
    
    # post-analyzation, fun visuals and useful records for the user
    while True:
        u_inp = input("Post-analyzation. Enter a number to select that option, all other entires will restart the main loop.\n"
        +"[ 1 ] See current memory\n"
        +"[ 2 ] Analyze ALL STATES for this grid size\n"
        +"[ 3 ] See all P-positions found so far\n"
        +"[ 4 ] Export all knonw P-positions to a text file\n"
        +"[ 5 ] Generate a randdom state for this size\n"
        +"[ 6 ] Exit program\n"
        +"\nChoice:\t")
        match (u_inp):
            case "1":
                print("Flase = N-Position, True = P-Position")
                print(Tools.memo)
                print()
            case "2":
                print()
                print("Please be patient, this may take some time...")
                Tools.analyze_all_states(size)
                print("Done!")
                print()
            case "3":
                cells_cnt = input("type the minimum number of cells to be in each state (default 0):\t")
                print()
                if not cells_cnt.strip():
                    cells_cnt = "0"
                # Either display binary encodings or the pictures.
                Tools.print_p_pos_cells(size, int(cells_cnt), input("type \'v\' to see visuals:\t")=="v")
                print()
            case "4":
                filename = input("Enter the name of your text file (inclucde \".txt\"):\t")
                print()
                Tools.export_p_positions_txt(size, filename, input("Enter the delimiter to use:\t"))
                print()
            case "5":
                state = Tools.random_state(size)
                printing.print_grid(state)
                print()
            case "6":
                sys.exit()
            case _:
                break