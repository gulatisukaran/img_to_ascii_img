#  1. get an image<done>
#  2. read the rgb values of every set of 8 pixels
#  3. take average and map that to a char
#  4. store that as a list and then lastly convert the list into an image

from PIL import Image, ImageFont, ImageDraw
import numpy as np

def main():
    converted_ascii_from_img, width, height = get_image("E:\python prjcts\img2ascii\img_to_ascii_img\srk.jpg")
    draw_image(converted_ascii_from_img, width=width*8, height=height*8)
    

def get_image(file_path):
    # get the image from specified file path
    img = Image.open(file_path).convert("L")

    # extract width and height from the image
    width, height = img.size
    # get the converted (text) version of the image provided
    converted_ascii = convert_img_to_ascii(img)
    return converted_ascii, width, height

def convert_img_to_ascii(img):
    # Return the final string that represents the final image
    array = np.asarray(img)

    new_array = np.empty([array.shape[0], array.shape[1]], dtype=np.int32)
    # take the average RGB value of each pixel and store it inside {new_array}
    for i, j in np.ndindex(array.shape):
        new_array[i, j] = np.mean(array[i, j])

    # map the values of each pixel to image
    final_image_txt = ""
    for row in new_array:
        for col in row:
            if col == 0:
                final_image_txt += "   "
            elif col > 0 and col < 25 :
                final_image_txt += " . "
            elif col >=25 and col < 50 :
                final_image_txt += " : "
            elif col >= 50 and col < 75 :
                final_image_txt += " o "
            elif col >= 75 and col < 100 :
                final_image_txt += " i "
            elif col >= 100 and col < 125 :
                final_image_txt += " l "    
            elif col >= 125 and col < 150 :
                final_image_txt += " p " 
            elif col >= 150 and col < 175 :
                final_image_txt += " m " 
            elif col >= 175 and col < 200 :
                final_image_txt += " n " 
            elif col >= 200 and col < 225 :
                final_image_txt += " @ " 
            else :
                final_image_txt += " N "
        final_image_txt += "\n"
    print("generated text")
    return final_image_txt

def draw_image(txt, width, height):
    # write the complete text then draw on image
    rectangle = draw_rectangle(width, height)

    # fill in the text inside the rectangle
    draw_text_on_image(txt, rectangle)

def draw_text_on_image(text, rectangle):
    # get an image to draw on it, in our case a plane white rectangle image
    with rectangle.convert("RGBA") as base:

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("img_to_ascii_img\Courier_Prime\CourierPrime-Bold.ttf", 4)

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