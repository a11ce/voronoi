# converts a black and white image to a list of black points in the image

from PIL import Image
from pylab import *


img = array(Image.open('david.png'))

# x by y
print("Size is " + str(len(img[0]))+ "x"+ str(len(img)))
outfile = open("output.csv", "a")


for i in range(len(img)):
        for j in range(len(img[i])):
            if (img[i][j] == 255):
                outfile.write(str(i) + "," + str(j) + "\n")
