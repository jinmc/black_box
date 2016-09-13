from random import random, sample

real_board =  [ [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False],
                [False, False, False, False, False, False, False, False] ]
printed_board = [ [False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, False, False, False],
                  [False, False, False, False, False, False, False, False] ]
dict = {   "1T":" ",
           "2T":" ",
           "3T":" ",
           "4T":" ",
           "5T":" ",
           "6T":" ",
           "7T":" ",
           "8T":" ",
           "1B":" ",
           "2B":" ",
           "3B":" ",
           "4B":" ",
           "5B":" ",
           "6B":" ",
           "7B":" ",
           "8B":" ",
           "1L":" ",
           "2L":" ",
           "3L":" ",
           "4L":" ",
           "5L":" ",
           "6L":" ",
           "7L":" ",
           "8L":" ",
           "1R":" ",
           "2R":" ",
           "3R":" ",
           "4R":" ",
           "5R":" ",
           "6R":" ",
           "7R":" ",
           "8R":" " }

def create_board():
    """creates the initial black box board."""

    return [ [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False],
             [False, False, False, False, False, False, False, False] ]

def random_location():
    """defines random location in the grid
    Location = (a, b) and use in main ex) Location1 = (0, 2) """
    Location1 = sample(range(8), 2)
    Location2 = sample(range(8), 2)
    Location3 = sample(range(8), 2)
    Location4 = sample(range(8), 2)
    while Location2 == Location1:
        Location2 = sample(range(8), 2)
    while Location3 == Location1 and Location3 != Location2:
        Location3 = sample(range(8), 2)
    while Location4 == Location1 and Location4 != Location2 and Location4 != Location3:
        Location4 = sample(range(8), 2)
    return tuple(Location1), tuple(Location2), tuple(Location3), tuple(Location4)

def new_game(Location1, Location2, Location3, Location4):
    """The Location should be like Location = (0, 3) then
    first row, fourth column"""
    global real_board
    real_board = create_board()
    
    real_board[Location1[0]][Location1[1]] = True
    real_board[Location2[0]][Location2[1]] = True
    real_board[Location3[0]][Location3[1]] = True
    real_board[Location4[0]][Location4[1]] = True
    return

def get_real_board():
    """helper function to test new game"""
    return real_board

def return_minus(boo):
    if boo == False:
        return "- "
    else:
        return "* "

def print_board():
    global printed_board
    print()
    print("      1 2 3 4 5 6 7 8       ")
    print("     ", dict['1T'], dict['2T'], dict['3T'], dict['4T'], dict['5T'], dict['6T'], dict['7T'], dict['8T'], "       ")
    print("     " + "-----------------" + "      ")
    for i in range(8):
        print(str(i + 1) + "  " + dict[str(i + 1) + 'L'] + "|" + " " + return_minus(printed_board[i][0]) + return_minus(printed_board[i][1]) + return_minus(printed_board[i][2]) + return_minus(printed_board[i][3])
              + return_minus(printed_board[i][4]) + return_minus(printed_board[i][5]) + return_minus(printed_board[i][6]) + return_minus(printed_board[i][7]) + "|" + dict[str(i + 1) + 'R'] + "  " + str(i + 1))
    print("     " + "-----------------" + "      ")
    print("     ", dict['1B'], dict['2B'], dict['3B'], dict['4B'], dict['5B'], dict['6B'], dict['7B'], dict['8B'], "       ")
    print("      1 2 3 4 5 6 7 8       ")
    print()

def print_real_board():
    global real_board
    print()
    print("      1 2 3 4 5 6 7 8       ")
    print()
    print("     " + "-----------------" + "      ")
    for i in range(8):
        print(str(i + 1) + "   " + "|" + " " + return_minus(real_board[i][0]) + return_minus(real_board[i][1]) + return_minus(real_board[i][2]) + return_minus(real_board[i][3])
              + return_minus(real_board[i][4]) + return_minus(real_board[i][5]) + return_minus(real_board[i][6]) + return_minus(real_board[i][7]) + "|" + "   " + str(i + 1))
    print("     " + "-----------------" + "      ")
    print()
    print("      1 2 3 4 5 6 7 8       ")
    print()

def shoot(entry):       ## entry = 1L , etc...
    global dict
    global row
    global column
    global direction
    global real_board
    """i and j are 1 to 8 together, and they are not 0 to 7. it may be confusing."""
    if entry[1] == "L" or entry[1] == "l":
        direction = "R"
        row = int(entry[0])
        column = 0
        if row == 1 and real_board[1][0]:
            return str(row) + "L"
        elif row == 8 and real_board[6][0]:
            return str(row) + "L"
        elif 2 <= row <= 7 and real_board[row - 2][0]:
            return str(row) + "L"
        elif 2 <= row <= 7 and real_board[row][0]:
            return str(row) + "L"
        while True:
            move()
            check()
            if direction == 0:
                return
            if row == 0:
                return str(column) + "T"
            elif column == 0:
                return str(row) + "L"
            elif row == 9:
                return str(column) + "B"
            elif column == 9:
                return str(row) + "R"
                
    elif entry[1] == "R" or entry[1] == "r":
        direction = "L"
        row = int(entry[0])
        column = 9
        if row == 1 and real_board[1][7]:
            return str(row) + "R"
        elif row == 8 and real_board[6][7]:
            return str(row) + "R"
        elif 2 <= row <= 7 and real_board[row - 2][7]:
            return str(row) + "R"
        elif 2 <= row <= 7 and real_board[row][7]:
            return str(row) + "R"
        while True:
            move()
            check()
            if direction == 0:
                return
            if row == 0:
                return str(column) + "T"
            elif column == 0:
                return str(row) + "L"
            elif row == 9:
                return str(column) + "B"
            elif column == 9:
                return str(row) + "R"
        
    elif entry[1] == "T" or entry[1] == "t":
        direction = "D"
        row = 0
        column = int(entry[0])
        if column == 1 and real_board[0][1]:
            return str(column) + "T"
        elif column == 8 and real_board[0][6]:
            return str(column) + "T"
        elif 2 <= column <= 7 and real_board[0][column - 2]:
            return str(column) + "T"
        elif 2 <= column <= 7 and real_board[0][column]:
            return str(column) + "T"
        while True:
            move()
            check()
            if direction == 0:
                return
            if row == 0:
                return str(column) + "T"
            elif column == 0:
                return str(row) + "L"
            elif row == 9:
                return str(column) + "B"
            elif column == 9:
                return str(row) + "R"
        
    elif entry[1] == "B" or entry[1] == "b":
        direction = "U"
        row = 9
        column = int(entry[0])
        if column == 1 and real_board[7][1]:
            return str(column) + "B"
        elif column == 8 and real_board[7][6]:
            return str(column) + "B"
        elif 2 <= column <= 7 and real_board[7][column - 2]:
            return str(column) + "B"
        elif 2 <= column <= 7 and real_board[7][column]:
            return str(column) + "B"
        while True:
            move()
            check()
            if direction == 0:
                return
            if row == 0:
                return str(column) + "T"
            elif column == 0:
                return str(row) + "L"
            elif row == 9:
                return str(column) + "B"
            elif column == 9:
                return str(row) + "R"


def check():
    """ checking the direction if it does reflection, deflection,
    or hit"""
    global real_board
    global row
    global column
    global direction
    if direction == "R":
        if column == 8:
            column = 9
        elif row == 1:
            if real_board[row - 1][column] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row][column]:
                row = 0
        elif row == 8:
            if real_board[row - 1][column] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row - 2][column]:
                row = 9
        elif  2 <= row <= 7:
            if real_board[row - 1][column] or real_board[row - 1][column - 1]:
                direction = 0    #Hits
            elif real_board[row][column] and real_board[row - 2][column]:
                direction = "L"  #reflection
            elif real_board[row][column]:
                direction = "U"   
            elif real_board[row - 2][column]:
                direction = "D"
                
    elif direction == "L":
        if column == 1:
            column = 0
        elif row == 1:
            if real_board[row - 1][column - 2] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row][column - 2]:
                row = 0
        elif row == 8:
            if real_board[row - 1][column - 2] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row - 2][column - 2]:
                row = 9
        elif 2 <= row <= 7:
            if real_board[row - 1][column - 2] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row][column - 2] and real_board[row - 2][column - 2]:
                direction = "R"
            elif real_board[row][column - 2]:
                direction = "U"
            elif real_board[row - 2][column - 2]:
                direction = "D"
            
    elif direction == "U":
        if row == 1:
            row = 0
        elif column == 1:
            if real_board[row - 2][column - 1] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row - 2][column]:
                column = 0
        elif column == 8:
            if real_board[row - 2][column - 1] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row - 2][column - 2]:
                column = 9
        elif 2 <= column <= 7:
            if real_board[row - 2][column - 1] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row - 2][column - 2] and real_board[row - 2][column]:
                direction = "D"
            elif real_board[row - 2][column - 2]:
                direction = "R"
            elif real_board[row - 2][column]:
                direction = "L"

    elif direction == "D":
        if row == 8:
            row = 9
        elif column == 1:
            if real_board[row][column - 1] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row][column]:
                column = 0
        elif column == 8:
            if real_board[row][column - 1] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row][column - 2]:
                column = 9
        elif 2 <= column <= 7:            
            if real_board[row][column - 1] or real_board[row - 1][column - 1]:
                direction = 0
            elif real_board[row][column - 2] and real_board[row][column]:
                direction = "U"
            elif real_board[row][column - 2]:
                direction = "R"
            elif real_board[row][column]:
                direction = "L"
            
def move():
    """ direction is "L", "R", "U", "D" meaning left, right, up, down"""
    global row
    global column
    global direction
    
    if direction == "R":
        column = column + 1
    elif direction == "L":
        column = column - 1
    elif direction == "U":
        row = row - 1
    elif direction == "D":
        row = row + 1

def toggle(row, column):
    global printed_board
    
    if printed_board[row][column] == False:
        printed_board[row][column] = True
    elif printed_board[row][column] == True:
        printed_board[row][column] = False
    return

def get_printed_board():
    """helper function to test. returns printed board"""
    return printed_board
    
def score():
    """returns the current score. Don't end the game"""
    global dict
    global printed_board
    global real_board
    score = 0
    for key, value in dict.items():
        if value != ' ':
            score += 1
    for i in range(len(printed_board[0])):
        for j in range(len(printed_board)):
            if printed_board[i][j] == True and real_board[i][j] == False:
                score += 10
            elif printed_board[i][j] == False and real_board[i][j] == True:
                score += 10
    return score 

def main():
    global printed_board
    global real_board
    global dict
    dict['1T'] = ' '
    dict['2T'] = ' '
    dict['3T'] = ' '
    dict['4T'] = ' '
    dict['5T'] = ' '
    dict['6T'] = ' '
    dict['7T'] = ' '
    dict['8T'] = ' '
    dict['1L'] = ' '
    dict['2L'] = ' '
    dict['3L'] = ' '
    dict['4L'] = ' '
    dict['5L'] = ' '
    dict['6L'] = ' '
    dict['7L'] = ' '
    dict['8L'] = ' '
    dict['1R'] = ' '
    dict['2R'] = ' '
    dict['3R'] = ' '
    dict['4R'] = ' '
    dict['5R'] = ' '
    dict['6R'] = ' '
    dict['7R'] = ' '
    dict['8R'] = ' '
    dict['1B'] = ' '
    dict['2B'] = ' '
    dict['3B'] = ' '
    dict['4B'] = ' '
    dict['5B'] = ' '
    dict['6B'] = ' '
    dict['7B'] = ' '
    dict['8B'] = ' '
    printed_board = create_board()
    real_board = create_board()
    rand = random_location()
    new_game(rand[0], rand[1], rand[2], rand[3])
    ch = "a"
    while True:
        print_board()
        command = input("input s to shoot, input m to mark, input u to unmark, input sc to see the score, input f to finish. : ")
        if command == "s" or command == "S":
            input_entry = input("input your entry (ex: 1R) : " )
            if len(input_entry) != 2 or input_entry[0] not in "12345678" or input_entry[1] not in "lLrRtTbB":
                print("invalid input!")
            elif shoot(input_entry) == None:
                dict[input_entry.upper()] = "H"
            elif shoot(input_entry) == input_entry.upper():
                dict[input_entry.upper()] = "R"
            elif shoot(input_entry)[0] == input_entry[0] and shoot(input_entry)[1] in "lL" and input_entry[1] in "rR":
                dict[input_entry.upper()] = "M"
                dict[shoot(input_entry)] = "M"
            elif shoot(input_entry)[0] == input_entry[0] and shoot(input_entry)[1] in "rR" and input_entry[1] in "lL":
                dict[input_entry.upper()] = "M"
                dict[shoot(input_entry)] = "M"
            elif shoot(input_entry)[0] == input_entry[0] and shoot(input_entry)[1] in "tT" and input_entry[1] in "bB":
                dict[input_entry.upper()] = "M"
                dict[shoot(input_entry)] = "M"
            elif shoot(input_entry)[0] == input_entry[0] and shoot(input_entry)[1] in "Bb" and input_entry[1] in "tT":
                dict[input_entry.upper()] = "M"
                dict[shoot(input_entry)] = "M"
            elif shoot(input_entry) != input_entry:
                dict[input_entry.upper()] = ch
                dict[shoot(input_entry)] = ch
                ch = chr(ord(ch) + 1)

        elif command == "m" or command == "M" or command == "u" or command == "U":
            input_rowcolumn = input("input row and column : ")    ## example, 44
            input_rowcolumn = input_rowcolumn.replace(" ", "")
            if len(input_rowcolumn) == 2 and isinstance(int(input_rowcolumn), int):
                toggle(int(input_rowcolumn[0]) - 1, int(input_rowcolumn[1]) - 1)
            else:
                print("invalid input!")
            
        elif command == "sc" or command == "SC":
            print("score : "+ str(score()))         
        elif command == "f" or command == "F":
            print("Thank you!")
            print("Your score is : " + str(score()))
            print("This is the real board : ")
            print_real_board()
            again = input("Do you want to play again? (y/n) " )
            if again == "n" or again == "N":
                print("Good bye!")
                break
            elif again == "y" or again == "Y":
                real_board = create_board()
                rand = random_location()
                new_game(rand[0], rand[1], rand[2], rand[3])
                for key, value in dict.items():
                    dict[key] = " "
                printed_board = create_board()
                ch = 'a'
                continue
        else:
            print("invalid input!")

if __name__ == "__main__":
    main()  # or whatever your starting method is

