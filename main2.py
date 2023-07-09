from PIL import Image
import numpy as np
import sys, random, argparse

# Defining grayscale levels
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`. "
gscale2 = "@%#*+=-:. "

def parse_from_cmd():
    #create parser
    descString = "NGL, I will generate the most beautiful ASCII art from the image u give :)"
    parser = argparse.ArgumentParser(description=descString)
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='morelevels', action='store_true')

def save_to_txt(imgString):
    txt = open("ascii-img.txt", 'w')
    for row in imgString:
        txt.write(row + "\n")
    txt.close()

def open_img(filename, cols, scale, scalelarge=True):
    """
    1. open the image
    2. cut it into tiles of suitable dimens
    """
    global gscale1, gscale2
    # open and convert to grayscale
    img = Image.open(filename).convert("L")
    # store img dimensions
    imgWidth, imgHeight = img.size[0], img.size[1]
    # compute tile width
    tileWidth = imgWidth/cols
    # compute tile height based on aspect ratio and scale
    tileHeight = tileWidth/scale
    # compute the number of rows of the final grid
    rows = int(imgHeight/tileHeight)
    
    imgString = []
    # cut tiles from image:
    for rowNumber in range(0, rows):
        # loop through each row
        # calc the y coordinates of the tiles
        y1 = int(rowNumber*tileHeight)
        y2 = int((rowNumber+1)*tileHeight)
        # correct y2 for tiles of last row (which could be reduced 
        # if num of rows are not a multiple of a row height)
        if rowNumber == rows-1: y2 = imgHeight

        for colNumber in range(0, cols):
            # loop through each column
            # calc the x coordinates of the tiles
            x1 = int(colNumber*tileWidth)
            x2 = int((colNumber+1)*tileWidth)
            # correct x2 for tiles of last column (which could be
            # reduced if num of cols are not a multiple of a col width)
            if colNumber == cols-1: x2 = imgWidth

            # crop the image and get avg brightness:
            imgTile = img.crop((x1, y1, x2, y2))
            brightness = get_avg_brightness(imgTile)

            if scalelarge:
                char = gscale1[int(brightness*69/255)]
            else:
                char = gscale2[int(brightness*9/255)]
            imgString[rowNumber] += char

        save_to_txt(imgString)

def get_avg_brightness(imageTile):
    """
    return avg brightness of the given image
    """
    img = np.array(imageTile)
    width, height = img.shape
    return np.average(img.reshape(width*height))

def main():
    open_img('img_to_ascii_img\srk.jpg', cols=100, scale=1)


if __name__ == "__main__":
    main()
 

