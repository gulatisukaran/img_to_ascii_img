#  1. get an image<done>
#  2. read the rgb values of every set of 8 pixels
#  3. take average and map that to a char
#  4. store that as a list and then lastly convert the list into an image

from PIL import Image, ImageFont, ImageDraw
import numpy as np

def main():
    text, width, height = get_image("E:\python prjcts\img2ascii\img_to_ascii_img\srk.jpg")
    draw_image(text, width=width, height=height)
    


def get_image(file_path):
    # get the image from specified file path
    img = Image.open(file_path)
    pixel_map = img.load()
  
    # Extracting the width and height 
    # of the image:
    width, height = img.size
    
    pixels =[226, 137, 125, 226, 137, 125, 223, 137, 133, 223, 136, 128, 226, 138, 120, 226, 129, 116, 228, 138, 123, 227, 134, 124, 227, 140, 127, 225, 136, 119, 228, 135, 126, 225, 134, 121, 223, 130, 108, 226, 139, 119, 223, 135, 120, 221, 129, 114, 221, 134, 108, 221, 131, 113, 222, 138, 121, 222, 139, 114, 223, 127, 109, 223, 132, 105, 224, 129, 102, 221, 134, 109, 218, 131, 110, 221, 133, 113, 223, 130, 108, 225, 125, 98, 221, 130, 121, 221, 129, 111, 220, 127, 121, 223, 131, 109, 225, 127, 103, 223] 

    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)
    text = "sdfasdjkfhasjkdhfasl2364yr9 70ewqyrjsdnf,m.asdhrq;34uuiqewyhrsjkdnbfkmlasdfbasldjkf\nhjsdkfhkskfdjhsdjkfhjksdhfewioufhrkzdnfv,msdfnlsfrhjwefhroiwerfhyoishf\nhjskfjkncsxvijewyhruieshjkfn,msdnf,mnsenrijwehyroiewhroi  skjnfkjshruihewhoiwehfi\n"
    return text, width, height

def draw_image(txt, width, height):
    # write the complete text then draw on image
    rectangle = draw_rectangle(width, height)

    # fill in the text    
    draw_text_on_image(txt, rectangle)

def draw_text_on_image(text, rectangle):

    # get an image to draw on it, in our case a plane white rectangle image
    with rectangle.convert("RGBA") as base:

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("arial.ttf", 12)
        # get a drawing context
        d = ImageDraw.Draw(txt)
        # draw text, full opacity
        d.text((10, 60), f"{text}", font=fnt, fill=(0, 0, 0, 255))

        out = Image.alpha_composite(base, txt)

        out.show()

def draw_rectangle(width, height):
    # Create a new image with a white background
    # and return it
    image = Image.new('RGB', (width, height), 'white')
    return image


if __name__ == "__main__":
    main()