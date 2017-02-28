#!/usr/bin/python

#My Python file for tictac toe game!!
#2 players
# enter input
# all rows, all columns and diagonals
# list contains either X or 0
from __future__ import print_function


list_1 = [' ',' ',' ']
list_2 = [' ',' ',' ']
list_3 = [' ',' ',' ']

matrix_input = [list_1,list_2,list_3]

assigneduser = 0

def fill_value(assigneduser, location):
    """
        INPUT:
        OUTPUT:
    """

    if (location == '1'):
        if list_1[0] == ' ':
            list_1[0] = str(assigneduser)
            return True;
        else:
            return False
    elif (location == '2'):
        if list_1[1] == ' ':
            list_1[1] = str(assigneduser)
            return True;
        else:
            return False
    elif (location == '3'):
        if list_1[2] == ' ':
            list_1[2] = str(assigneduser)
            return True;
        else:
            return False
    elif (location == '4'):
        if list_2[0] == ' ':
            list_2[0] = str(assigneduser)
            return True;
        else:
            return False
    elif (location == '5'):
        if list_2[1] == ' ':
            list_2[1] = str(assigneduser)
            return True;
        else:
            return False
    elif (location == '6'):
        if list_2[2] == ' ':
            list_2[2] = str(assigneduser)
            return True;
        else:
            return False
    elif (location == '7'):
        if list_3[0] == ' ':
            list_3[0] = str(assigneduser)
            return True;
        else:
            return False
    elif (location == '8'):
        if list_3[1] == ' ':
            list_3[1] = str(assigneduser)
            return True;
        else:
            return False
    elif (location == '9'):
        if list_3[2] == ' ':
            list_3[2] = str(assigneduser)
            return True;
        else:
            return False

def is_winner():

        if matrix_input[0][0] == matrix_input[0][1] and matrix_input[0][0] == matrix_input[0][2]:
            print ("1")
            return matrix_input[0][0],True;
        elif matrix_input[0][0] == matrix_input[1][0] and matrix_input[0][0] == matrix_input[2][0]:
            print ("2")
            return matrix_input[0][0],True;
        elif matrix_input[0][0] == matrix_input[1][1] and matrix_input[0][0] == matrix_input[2][2]:
            print ("3")
            return matrix_input[0][0],True;
        elif matrix_input[1][0] == matrix_input[1][1] and matrix_input[0][0] == matrix_input[2][1]:
            print ("4")
            return matrix_input[1][0],True;
        elif matrix_input[0][2] == matrix_input[1][2] and matrix_input[0][2] == matrix_input[2][2]:
            print ("5")
            return matrix_input[0][2],True;
        elif matrix_input[0][2] == matrix_input[1][1] and matrix_input[0][2] == matrix_input[2][0]:
            print ("6")
            return matrix_input[0][2],True;
        else:
            return ' ',False

def display_screen():
    print (matrix_input[0])
    print (matrix_input[1])
    print (matrix_input[2])
    return True

def player_input():
    while (True):
        print ("Enter location 1-9")
        var = raw_input("Please enter the location for player {}:" .format(assigneduser))
        if var >= '1' and var <= '9':
            return var
        else:
            print ("Incorrect location please enter 0-9")
    

def toggle_user(assigneduser):
    if (assigneduser == 1):
            assigneduser = 2
    elif (assigneduser == 2):
            assigneduser = 1;
    return assigneduser

def get_user_input():
    global assigneduser
    min_inputs = 0
    assigneduser = 1
    while (True):
        display_screen()
        if (fill_value(assigneduser,player_input())):
            if (min_inputs  >= 3):
                item, var = is_winner()
                print (item, var)
                if (var == True):
                    print ("User {} is a winner " .format(item))
                    display_screen()
                    break
                elif (min_inputs == 9):
                    display_screen()
                    print ("No one is a winner")
                    break
            else:
                min_inputs += 1
            assigneduser = toggle_user(assigneduser)
        else:
            print ("Cell is already filled please fill another cell")
            continue

def main():
    get_user_input()


if __name__ == "__main__":
    main()
