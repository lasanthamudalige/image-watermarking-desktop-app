from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
import random

root = Tk()


def main():
    root.title("Image water marker")
    root.geometry("400x200")

    # create a button in the window to open an image to watermark
    open_btn = Button(root, text="Select image", command=save_image)
    open_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()


def save_image():
    # open jpg file in any directory
    file_name = filedialog.askopenfilename(initialdir="/Pictures", title="Select image",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    # open the file with PIL image
    image = Image.open(file_name)

    x = image.width
    y = image.height

    # open the image to draw
    new_img = ImageDraw.Draw(image)

    # select the font to enter to the image
    my_font = ImageFont.truetype('PermanentMarker-Regular.ttf', 25)

    # add the word to the right bottom corner of the image
    new_img.text((x - 150, y - 50), "Lasantha",
                 font=my_font, fill=(255, 255, 255))

    serial_num = random.randint(1000, 9999)

    # save the image with the generated random number
    image.save(f"watermark_image {serial_num}.jpg")


if __name__ == "__main__":
    main()
