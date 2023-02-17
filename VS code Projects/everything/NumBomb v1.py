import random
import numpy as np
#size of grid
# w = random.randint(1,10)
# h = random.randint(1,10)
w = 20
h = 20
print(w, h)

# grid
space = '0'
world = [[space] * w for i in range(h)]
npworld2 = np.array(world) 

# random number
npworld2[random.randint(1,9)][random.randint(1,9)] = str(random.randint(1,11))

# initialize world
for x in npworld2:
    print(' '.join(x))

def bomb(xcoord, ycoord, npworld):
    int(xcoord)
    int(ycoord)
    npworld = npworld.astype(int)
    # expanding on x axis 
    for i in range(1,w-xcoord):
        if xcoord+i < w:   
            npworld[ycoord][xcoord+i] += i
        if xcoord-i >= 0:
            npworld[ycoord][xcoord-i] += i

    # expanding on y axis
    for j in range(1,h-ycoord):
        if ycoord+j < h: 
            npworld[ycoord+j][xcoord] += j
        if ycoord-j >= 0:
            npworld[ycoord-j][xcoord] += j

    # expanding diagonally
    if w > h:
        for o in range(1,h-ycoord):
            if ycoord+o < h: 
                npworld[ycoord+o][xcoord+o] += 2*o 
                npworld[ycoord+o][xcoord-o] += 2*o
            if ycoord - o >= 0:
                npworld[ycoord-o][xcoord-o] += 2*o
                npworld[ycoord-o][xcoord+o] += 2*o
    elif w < h:
        for p in range(1, w-xcoord):
            if xcoord + p < w:
                npworld[ycoord+p][xcoord+p] += 2*p
                npworld[ycoord-p][xcoord+p] += 2*p
            if xcoord - p >= 0:
                npworld[ycoord+p][xcoord-p] += 2*p
                npworld[ycoord-p][xcoord-p] += 2*p
    elif w == h:
        for k in range(1, w-xcoord):
            if xcoord + k < w and ycoord + k < h:
                npworld[ycoord+k][xcoord+k] += 2*k
            if xcoord + k < w and ycoord - k >= 0:
                npworld[ycoord-k][xcoord+k] += 2*k
            if xcoord - k >= 0 and ycoord + k < h:
                npworld[ycoord+k][xcoord-k] += 2*k
            if xcoord - k >= 0 and ycoord - k >= 0:
                npworld[ycoord-k][xcoord-k] += 2*k
    return npworld
x = int(input("x-coordinate for the bomb:"))
y = int(input("y-coordinate for the bomb:"))
npworld2 = bomb(x, y, npworld2)
print(np.matrix(npworld2))

#print(npworld)

npworld2 = npworld2.astype(str)
for k in npworld2:
    print(' '.join(k))
    


