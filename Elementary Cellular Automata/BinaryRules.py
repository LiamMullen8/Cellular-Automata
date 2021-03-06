
import math
from PIL import Image, ImageDraw


def rep(start):    
    s=[]
    for i in range(1, len(start)-1):
        s.append(f"{Rule[int(start[i-1 : i+1 +1], 2)]}")
    return "0" + "".join(s) + "0" 


if __name__ == "__main__":

    start = "0" + input("enter binary: ") + "0"

    Rule = input("enter binary rule: ")
    Rule = Rule[::-1]

    h = int(input("enter number of generations: "))
    w = len(start)-2
  
    # creating new Image object
    img = Image.new("RGB", (w, h))
  
    # create rectangle image
    img1 = ImageDraw.Draw(img)  

    #update each row
    for j in range(1, h+1):
        for i in range(1, w+1):
            img1.rectangle([(i-1, j-1), (i, j)], fill=(255*int(start[i]), 0, 255))
        start = rep(start)
        
    img.show()
    img.save(f"Rule{int(Rule[::-1], 2)}.png")
