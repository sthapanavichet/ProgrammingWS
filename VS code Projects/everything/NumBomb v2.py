import random
import numpy as np

#main function
def bomb(xcoord, ycoord, world): 
# convert array to int array
    world = world.astype(int)
    int(xcoord), int(ycoord)
    Maxx = 0 
    Maxy = 0
    # expanding on the x axis from origin
    for i in range(1, w):
        if xcoord+i < w and xcoord-i >= 0 and ycoord+i < h and ycoord-i >= 0:
            world[ycoord][xcoord+i] += i
            world[ycoord][xcoord-i] += i
            Maxx += 1
            world[ycoord+i][xcoord] += i
            world[ycoord-i][xcoord] += i
            Maxy += 1
    Numlist = [1]
    length = 0
    # Numlist2 = np.array(Numlist)
    for i in range(1, Maxx):
        Numlist.append(1+i)
        Numlist.insert(0, 1+i)
        length += 2
    #expanding in the pos y direction
    for i in range(1, h):
        Maxx -= 1
        if ycoord-i >= 0:
            for o in range(1, w):
                if xcoord+o <= xcoord + Maxx and xcoord-o >= xcoord - Maxx:
                    world[ycoord-i][xcoord+o] = Numlist[int(length/2) - o - i + 1]
                    world[ycoord-i][xcoord-o] = Numlist[int(length/2) + o + i - 1]
        #expanding in the neg y direction
        if ycoord+i <= h:
            for o in range(1, w):
                if xcoord+o <= xcoord + Maxx and xcoord-o >= xcoord - Maxx:
                    world[ycoord+i][xcoord+o] = Numlist[int(length/2) - o - i + 1]
                    world[ycoord+i][xcoord-o] = Numlist[int(length/2) + o + i - 1]
    world = world.astype(str)
    return world

# Border and displaying world
def display(world):
    verticalNum = 0
    for row in world:
        print(" ".join(["{:<2}".format(nums) for nums in row]), end=" ")
        verticalNum += 1
        print(" | {}".format(verticalNum))
    
    _line = [["_"] * (w)]
    for items in _line:
        print("__".join(items))
    horizontalNum = np.arange(1, w+1)
    for num in horizontalNum:
        print(" ".join(["{:<2}".format(num)]), end=" ")
    print(" ")

#replacing 0 with x and starting point with O
def replacezero(xcoord, ycoord, world):
    world = world.astype(str)
    world[ycoord][xcoord] = "O"
    world = np.char.replace(world, "0", "X")
    return world

#showing bomb

#start 

#difficulty
difficulty = input("Please select the difficulty (Hard/Medium/Easy): ")
if(difficulty == "Easy" or difficulty == "easy"):
    width = random.randint(15,25)
    height = random.randint(15,25)
    numBomb = 0
elif(difficulty == "Medium" or difficulty == "medium"):
    width = random.randint(25,35)
    height = random.randint(25,35)
    numBomb = 0
elif(difficulty == "Hard" or difficulty == "hard"):
    width = random.randint(35,45)
    height = random.randint(35,45)
    numBomb = 0

#size of grid
w = width
h = height
print(w, h)

# grid
space = '0'
grid = [[space] * w for i in range(h)]
world = np.array(grid)

# random number
randx = random.randint(0,w) - 1
randy = random.randint(0,h) - 1
randvalue = random.randint(1,11)
world[randy][randx] = str(randvalue)

# initialize world
display(world)

#Users input
x = int(input("Enter x-coordinate: ")) - 1
y = int(input("Enter y-coordinate: ")) - 1
world = bomb(x, y, world)
world = replacezero(x, y, world)
display(world)

#win and lose conditions
if world[randy][randx] == randvalue:
    print("\nYou Win!")
else:
    print("\nTry Again")