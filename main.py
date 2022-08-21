from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog


def main():
    root = Tk()
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
    print(x)
    print(y)

    new_img = ImageDraw.Draw(image)

    myFont = ImageFont.truetype('PermanentMarker-Regular.ttf', 20)

    new_img.text((x - 150, y - 50), "Lasantha", font=myFont, fill=(255, 0, 0))
    image.show()


main()
