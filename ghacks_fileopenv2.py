import sys
from os.path import exists
import matplotlib.pyplot as plt

# CONSTANTS:
FIRSTARGV = 1
FIRSTARGV_LEN = 2

def file_input():
    """
    file_input, gets filename from command line argument (or prompts if not included)
    python ghacks_fileopenv0.py recordedv0.txt
    return: data in inputted file (recorded data)
    """
    # Check args, if there is an argument from the command line, get filename or exit
    if len(sys.argv) > FIRSTARGV:
        # Get filename
        filename = sys.argv[FIRSTARGV]
        if not exists(filename) and len(sys.argv) > FIRSTARGV_LEN:  # multiple arguments, but first argument is not a file
            print(f"Your first argument does not seem to be a file that exists.")
            arguments = True # checks whether there are more arguments to be checked
            while arguments:
                for i in range(len(sys.argv) - FIRSTARGV_LEN):  # check all arguments to see if they are a file
                    if exists(sys.argv[i + FIRSTARGV_LEN]):  # if another argument is file, use that
                        filename = sys.argv[i + FIRSTARGV_LEN]
                        print(f"But it seems that argument {i + FIRSTARGV_LEN} is a file that exists")
                        arguments = False
                    if arguments and i == (len(sys.argv) - FIRSTARGV_LEN - FIRSTARGV):   # when at last file and no file exist --> exit
                        print (f"Sorry, none of the arguments are a file that exists.")
                        exit()
        elif not exists(filename):  # no file exist so exit
            exit(f"Sorry your file does not exist")
        elif len(sys.argv) > (FIRSTARGV_LEN): # first argument is a file that exist, but there are too many arguments
            print(f"Too many arguments. But that's okay because it seems that your first argument is a file that exists....")
    else:  # No argument is entered in the cmd line so get input filename
        file_inputted = False
        while not file_inputted:
            filename = input(f"Oops no filename provided. Enter filename: ")
            if exists(filename):
                file_inputted = True
                print("ok")
            else: print("not ok")

    # Open, read and close file
    file = open(filename)
    data = file.read()
    file.close()
    return data

def main():
    """
    Main, gets filename from command line argument (or prompts if not included), reads file into dictionary, then executes contact list categorization
    :return: None
    """
    # Turn file into a list
    data = file_input().splitlines()  # create a list that separates items per line (\n)
    
    # Make dict from file, list of latitudes and longitudes in the order they were recorded
    data_dict = {}

    lat = []
    long = []
    x = []
    y = []
    z = []

    for i in range(0,len(data),4):  #bestposa data
        
        data[i] = data[i].split(",")  # split each comma separated data/field
        data_dict[float(data[i][6])-587680] = [float(data[i][11]),float(data[i][12]) ]
        
        lat.append(float(data[i][11]))
        long.append(float(data[i][12]))


    print(lat)
    print(long)

        #print(i)
    for i in range(2,len(data),4):  #bestxyz data
        
        data[i] = data[i].split(" ")  # split each space for separated data/field
        
        x.append(float(data[i][7]))
        y.append(float(data[i][8]))
        z.append(float(data[i][9]))
    
    #print(data_dict)

    fig, axs = plt.subplots(2)
    
    axs[0].plot(x,y)
    axs[1].plot(long, lat)
    #plt.scatter(x,y,z)
    plt.show()



main()

"""
updated-data.txt
"""

