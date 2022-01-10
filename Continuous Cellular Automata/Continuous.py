import math
from PIL import Image, ImageDraw
import sys
import random

def rep(start):
    s=[0]
    t=[(start[i-1], start[i], start[i+1]) for i in range(1, len(start)-1)]

    for R in t:

        # average the 3 cells, add delta to that, take only fractional part of result
        if t.index(R) == 0:
            w = ((float(R[1]) + float(R[2])) / 2) + PARAM                  # # Check boundaries
        elif t.index(R) == len(t)-1:
            w = ((float(R[0]) + float(R[1])) / 2) + PARAM                  # #
        else:
            w = ((float(R[0]) + float(R[1]) + float(R[2])) / 3) + PARAM 
            
        f,i = math.modf(w)
        s.append(f)
        
    s.append(0)
    return s


if __name__ == "__main__":

    # get user binary input, add border 0s
    if len(sys.argv) == 1:
        start = "0" + input("enter binary: ") + "0"
        
    elif sys.argv[1] == "source":
        i = int(input("enter size: "))
        start = "0" + "0"*(i//2 -1) + "1" + "0"*(i//2) + "0"
        
    elif sys.argv[1] == "random":
        i = int(input("enter size: "))
        start = "0"
        for _ in range(i):
            start += f"{random.randint(0,1)}"
        start += "0"  
        
    start = [int(c) for c in start]
    print(start)
    PARAM = float(input("Enter delta for avg of each cell: "))

    h = int(input("enter number of generations: "))
    w = len(start)-2
  
    # creating new Image object
    img = Image.new("RGB", (w, h))
  
    # create rectangle image
    img1 = ImageDraw.Draw(img)  

    #update each row
    for j in range(1, h+1):
        for i in range(1, w+1):
            img1.rectangle([(i-1, j-1), (i, j)], fill=(int(255*start[i]), 0, 255))
        start = rep(start)
        print(f"{(j/h) *100}%")
        
    img.show()

    if len(sys.argv) == 1:
        img.save(f"delta{PARAM}.png")
    else:
        img.save(f"delta{PARAM}-{sys.argv[1]}.png")
