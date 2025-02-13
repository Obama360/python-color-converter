from PIL import Image
import numpy as np

#open image
img = Image.open("test.jpg", 'r').resize((50,65),Image.Resampling.LANCZOS)

#convert image to np array
data = np.array(img)

#get height and width of image for indexing
height, width = img.size

#define color palette (this color palette is for skribbl.io)
colors = [(254,255,255),(0,0,0), (193,192,196), (77,75,77), (241,17,11), (116,11,7), (254,114,1), (195,56,0), (254,227,0), (231,162,0), (2,201,5), (1,84,16), (0,178,255), (0,85,158), (39,30,205), (15,7,98), (163,0,183), (85,0,104), (211,123,168), (164,85,116), (158,82,45), (98,48,13)]
print("{} colors loaded".format(len(colors)))

difs = []
difr = 0

#translate image
for y in range (height):
    for x in range (width):
        for color in colors:
            for rgb in range(3):
                diffi = data[x][y][rgb] - color[rgb]
                if diffi < 0:
                    diffi = diffi *-1
                difr = difr + diffi
            difs.append(difr)
            difr = 0
        raas = np.array(difs)
        data[x][y] = colors[np.argmin(raas)]
        difs = []

#show result image
Image.fromarray(data).show()