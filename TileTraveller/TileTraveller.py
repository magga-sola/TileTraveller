#Functions for moving (N, S, W, E)
#Keep track of where the user is after each input
#3x3 square, starts at 1x1, the goal is to reach 3x1, print Victory!
#Not a valid direction if the user can not move that way

def move_north(y):
    return y
def move_south(y):
    return y
def move_west(x):
    return x
def move_east(x):
    return x

def position(x,y):
    if x == 3 and y == 1:
        victory == True
        return victory
    return(x,y)

# def wall_block(x, y):
#     if x == 2:
#         if y == 3:
#             east == True
#         elif y == 2:
#             west == True
#             south == True
#         elif y == 1:
#             north == True
#         else:



x = 1
y = 1

direction = input("Direction: ")
while 1 <= x <= 3 and 1 <= y <= 3:
    if direction.lower() == "n":
        y = move_north(y)
    elif direction.lower() == "s":
        y = move_south(y)
    elif direction.lower() == "w":
        x = move_west(x)
    elif direction.lower() == "e":
        x = move_east(x)
    else:
        print("Not a valid direction!")