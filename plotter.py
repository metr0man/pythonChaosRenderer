import ast
import math
from PIL import Image

#vars
filename = "output.txt"
binColors = [(0,0,0),(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,0,255),(255,255,0),(255,255,255)]
binSize = 20

file = open(filename, 'r')
f = file.readlines()
file.close()

for x in range(len(f)):
    f[x] = ast.literal_eval(f[x][:-1])

bins = []
binNums = []
for x in range(len(f)):
    foundBin = False
    for y in range(len(bins)):
        if bins[y][0] < f[x][2] < bins[y][1] and bins[y][2] < f[x][3] < bins[y][3]:
            foundBin = True
            binNums[y] += 1
    if foundBin == False:
        bins.append([f[x][2]-binSize/2,f[x][2]+binSize/2,f[x][3]-binSize/2,f[x][3]+binSize/2])
        binNums.append(1)        
            
print(str(len(bins))+" bins")
      
for x in range(len(bins)):
    print("bin: "+str(bins[x])+" has "+str(binNums[x]))

#setup image
imageSize = int(math.sqrt(len(f)))
bitmap = Image.new("RGB", (imageSize, imageSize), "white")
pix = bitmap.load()

for x in range(imageSize):
    for y in range(imageSize):
        startPos = f[x*imageSize+y][:1]
        endPos = f[x*imageSize+y][2:]
        #find bin
        for z in range(len(bins)):
            if bins[z][0] < endPos[0] < bins[z][1] and bins[z][2] < endPos[1] < bins[z][3]:
                pointBin = z
        pix[x,y] = binColors[pointBin]

#bitmap.show()
bitmap.save('plot.png','png')

