"""
Rachael Shockey
DAT-129 Spring 2021
Icon Manipulation Program

"""

def get_user_input():
    """gets input 10 characters at a time, validates user input, returns valid input"""
    icon_row = []
    valid_chars = ['#', ':']
    user_icon_input = input("Please type in 10 characters with no spaces, tabs,or commas: ")
    valid_input = False
    while valid_input == False:
        if len(user_icon_input) != 10:
            print("Try again. Your entries must be 10 characters exactly (no spaces).")
            print("")
            user_icon_input = input("Please type in 10 characters with no spaces, tabs,or commas: ")
        # control for user input > or < 10 characters
        elif len(user_icon_input) == 10:
            for char in user_icon_input:
                if char not in valid_chars:
                    print("Please only enter valid characters (# for filled pixels and\
: for blank pixels.")
                    print("")
                    user_icon_input = input("Please type in 10 characters with no spaces, tabs, or commas: ")            
                    # control for user input of characters other than ':' or '#'
                else:
                    valid_input == True
                    icon_row += [user_icon_input]
                    # convert user input of 10 characters to a list 
                    return icon_row

def display_user_icon(icon_display):
    """takes in a list as an argument, displays the list"""
    
    for row in icon_display:
        print(row)
        # prints each row of 10 on a new line

# def invert_icon(list):
#     """reverses the order of each mini-list of user input"""
    
#     invert_wanted = input("Do you want to invert your image (Y/N)? ")
    
#     while invert_wanted == "Y" or invert_wanted == "y":
#         for row in list:
#             row = row.reverse()
#         display_user_icon(list)

# def flip_chars(icon_display):
#     """flips the placement of the two display characters throughout the image"""
    
#     flip_wanted = input("Do you want to flip the characters in your image (Y/N)? ")
    
#     while flip_wanted == "Y" or flip_wanted == "y":
#         for row in icon_display:
#             for char in row:
#                 if char == ":":
#                     char == "#"
#                 if char == "#":
#                     char == ":"
#             display_user_icon(icon_display)
            
    
# def change_scale(icon_display):
#     # need 4 nested for loops to multiply each item in a list and each list itself
#     
#     for row in icon_display:
#     # vertical scaling
#         for vert_rep in range (0:10):
#         for char in row:
#         # horizontal scaling

def main():
    """calls all other functions and runs the program with introductory text"""
    
    # introduce the program
    print("This program will take in user input of 100 total characters (10 \
at a time) and display your input as a 10x10 image. The first 10 characters \
you enter will be the top row of the image, and the last 10 you enter will \
be the bottom row. A '#' character will display as a filled pixel, and a ':' \
will display as a blank pixel.")
    
    input("Press ENTER when you are ready to continue.")
   
    icon_lines = []
    # initialize an empty list to add smaller lists to
   
    while(len(icon_lines)) < 10:
        new_line = get_user_input()
        icon_lines += new_line
        # keep collecting user input until there have been 10 valid entries
        # added to the list of lists
    print("")
    print("Here is your icon:")
    print("")
   
    display_user_icon(icon_lines)
    # print the list of 10 lists to display the user's 10x10 image
    
    invert_icon(icon_lines)
    
    flip_chars(icon_lines)
    

# make the program go
if __name__ == '__main__':
    main()