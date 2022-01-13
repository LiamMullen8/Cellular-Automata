# Python code to implement Conway's Game Of Life
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

def randomGrid(N):    
    """returns a grid of NxN random 0, 1"""
    A = np.random.randint(2, size=(N,N))

    # Border of 0s
    A[0,:] = 0
    A[N-1,:] = 0
    A[:,0] = 0
    A[:,N-1] = 0
    return A
    
def glider_init(N):

    A = np.zeros((N,N))

    # Glider
    A[N//2, N//2] = 1
    A[N//2 - 1, N//2 - 1] = 1
    A[N//2 + 1, N//2] = 1
    A[N//2 + 1, N//2 - 1] = 1
    A[N//2 + 1, N//2 - 2] = 1
    
    return A

def count_neighbors(i, j):

    global N
    global grid
    
    # moore neighborhood
    return (grid[i, (j-1)%N] + grid[i, (j+1)%N] + \
            grid[(i-1)%N, j] + grid[(i+1)%N, j] + \
            grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + \
            grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])  
    

def update(frameNum, img, grid, N):
    
    newGrid = grid.copy()
    for i in range(1, N-1):
        for j in range(1, N-1):
            c = count_neighbors(i, j)

            # alive if odd # neighbors
            #if c==1:
             #   newGrid[i,j] = 1
            #elif c==0:
            #    newGrid[i,j] = 0
            #
            # newGrid[i,j] = c
            
            # GOL Rules
            if grid[i,j] == 0:
                if c == 3:
                    newGrid[i,j] = 1

            elif grid[i,j] == 1:
                if c == 2 or c == 3:
                    newGrid[i,j] = 1
                else:
                    newGrid[i,j] = 0
            
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,



# main() function
def main():
    
    global N
    global grid
    
    N = int(input("grid size: "))
    F = int(input("enter number of frames: "))

    # initialize grid
    if len(sys.argv) == 1 or sys.argv[1]=="random":
        grid = randomGrid(N)
    
    elif sys.argv[1]=="glider":
        grid = glider_init(N)
    
    print(grid)

    
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid,  interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), frames=F, blit=False, repeat=False, interval=250)
    ani.save("gol.mov", fps=60, extra_args=['-vcodec', 'libx264'])
    
    #plt.show()

# call main
if __name__ == '__main__':    
    main()
