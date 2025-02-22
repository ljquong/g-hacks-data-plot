import sys
from os.path import exists
#from colorama import Fore

# CONSTANTS:
FIRSTARGV = 1
FIRSTARGV_LEN = 2

def main():
    """
    Main, gets filename from command line argument (or prompts if not included), reads file into dictionary, then executes contact list categorization
    :return: None
    """
   # filename = "Dataset" 

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

    # Turn file into a list
    data = data.splitlines()  # create a list that separates items per line (\n)
    for i in range(len(data)):  # for every item in list
        data[i] = data[i].split(",")  # split each comma separated name
   # data = (sorted(data))
    # Make dict from file
    names_dict = {}
    for contact in data: # for each contact list
        print(contact)
        key = contact[0]  # key is first name of contact list
        contact.pop(0)  # remove key from contact list
        names_dict[key] = contact  # add contact list to the person/key
    
    # Part 1

main()


import matplotlib.pyplot as plt
x= [1,2,3,4]
y= [2 ,6 ,4 ,10]

plt.plot(x,y)
plt.show()
