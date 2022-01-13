import bpy
from math import *
import random
from random import randint
from mathutils import Vector

class Cell:
    
    def __init__(self, location, size):
        
        bpy.ops.mesh.primitive_cube_add(size=size, location=location)
                                  
        self.obj = bpy.context.object
        
        if size == 0.001:
            self.size = 0
        else:
            self.size = 1
            
        
    def isAlive(self):
        return self.size != 0
    
    def loc():
        return self.obj.location
    
    def kill(self):
        self.size = 0
#        self.obj.dimensions = Vector((0,0,0))
        return f"Cell@{self.obj.location} killed"

    def birth(self):
        self.size = 1
#        self.obj.dimensions = Vector((1,1,1))
        return f"Cell@{self.obj.location} birth"


class Grid:
    def __init__(self, size):
        self.size = size
        self.cubes = []
        
        
    # initialize 3D grid of Cells
    def initCells(self):
        for k in range(self.size):
            h=[]
            for j in range(self.size):
                w=[]
                for i in range(self.size):
                    
                    cube = Cell(location=(k,j,i), size=random.choice([0.001,1]))
                    
                    w.append(cube)
                h.append(w)
            self.cubes.append(h)
        return
    
    
    def updateGrid(self):
        
        newGrid = []
        
        #for each cell
        for k in range(self.size):
            h=[]
            for j in range(self.size):
                w=[]
                for i in range(self.size):                
                    cell = self.cubes[k][j][i] 
                    
                    # count neighbors, get new state accordingly (dimensions)
                    n = 0

                    for z in range(k-1, k+1+1):
                        for y in range(j-1,j+1+1):
                            for x in range(i-1,i+1+1):
                                if z != x != y:
                                    if self.cubes[z%self.size][y%self.size][x%self.size].isAlive():
                                        n+=1
                                                            
                    # if alive
                    if cell.isAlive():
                        print(cell.obj.name, f"n = {n} ", "ALIVE")
                        
                        if (n == 3 or n == 5 or n == 7):
                            cell.birth()
                            w.append(Vector((1,1,1)))
                            
                        else:     
                            cell.kill()
                            w.append(Vector((0,0,0)))
                    
                    # if dead       
                    else:
                        print(cell.obj.name,f"n = {n} ", "DEAD")   
                                         
                        if n == 3 or 5<=n<=13:                       
                            cell.birth()
                            w.append(Vector((1,1,1)))
                            
                        else:
                            cell.kill()
                            w.append(Vector((0,0,0)))
                            
                h.append(w)
            newGrid.append(h)

        # apply new dimensions to grid
        for k in range(self.size):
            for j in range(self.size):
                for i in range(self.size):    
                    self.cubes[k][j][i].obj.dimensions = newGrid[j][k][i]

        bpy.context.view_layer.update() 
        del newGrid
        
        return


if __name__ == "__main__":
    
    scene = bpy.context.scene

    # instantiate 3D Grid and cells
    G = Grid(5)
    G.initCells()
    

    # initial frame
    for ob in scene.objects:
        ob.keyframe_insert(data_path="scale", frame=10)

    for i in range(20, 1000, 10):

        G.updateGrid()
        for ob in scene.objects:
            ob.keyframe_insert(data_path="scale", frame=i)
    
    
