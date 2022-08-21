from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
import random

root = Tk()


def main():
    root.title("Image water marker")
    root.geometry("400x200")

    open_btn = Button(root, text="Select image", command=select_image)
    open_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.mainloop()


def select_image():
    file_name = filedialog.askopenfilename(initialdir="/Pictures", title="Select image",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    image = Image.open(file_name)

    x = image.width
    y = image.height

    new_img = ImageDraw.Draw(image)

    my_font = ImageFont.truetype('PermanentMarker-Regular.ttf', 25)

    new_img.text((x - 150, y - 50), "Lasantha", font=my_font, fill=(255, 255, 255))

    serial_num = random.randint(1000, 9999)

    image.save(f"watermark_image {serial_num}.jpg")


main()
