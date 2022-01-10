# Python code to implement Conway's Game Of Life
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def randomGrid(N):    
    """returns a grid of NxN random 0, 1"""
    return np.random.randint(2, size=(N,N))

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
    for i in range(N):
        for j in range(N):
            c = count_neighbors(i, j)
            
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
    grid = randomGrid(N)
    print(grid)

    
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid,  interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ), frames=F, blit=False, repeat=False, interval=250)
    ani.save("gol.mp4", fps=30, extra_args=['-vcodec', 'libx264'])
    
    plt.show()

# call main
if __name__ == '__main__':
    main()
