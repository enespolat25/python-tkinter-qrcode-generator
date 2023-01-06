# Import module
from tkinter import *
import qrcode
from PIL import Image, ImageTk

root = Tk()
root.title('QR Kod Oluşturucu')

root.geometry("500x620")


def show():
    """
    qr_renk.config( text = renkler[clicked.get()] )
    arka_plan.config( text = renkler[clicked2.get()] )
    """
    veri_baslik.config(text="Karekod içeriği")
    veri.config(text=e1.get())

    qrrenk = renkler[clicked.get()]
    arkaplan = text = renkler[clicked2.get()]

    qr = qrcode. QRCode(version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=50, border=1)
    qr.add_data(e1.get())
    qr.make(fit=True)
    img = qr.make_image(fill_color=qrrenk, back_color=arkaplan)
    img.save("advanced.png")

    # Create a photoimage object of the image in the path
    image1 = Image.open("advanced.png")
    # Resize the image using resize() method
    resize_image = image1.resize((350, 350))

    test = ImageTk.PhotoImage(resize_image)

    label1 = Label(image=test)
    label1.image = test
    label1.grid(row=7, column=1)


options = [
    "Kırmızı",
    "Siyah",
    "Yeşil",
    "Beyaz",
    "Mor",
    "Sarı",
    "Turuncu"
]

options2 = [
    "Kırmızı",
    "Siyah",
    "Yeşil",
    "Beyaz",
    "Mor",
    "Sarı",
    "Turuncu"
]

renkler = {
    "Kırmızı": "red",
    "Siyah": "black",
    "Yeşil": "green",
    "Beyaz": "white",
    "Mor": "purple",
    "Sarı": "yellow",
    "Turuncu": "orange"

}

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Beyaz")

# datatype of menu text
clicked2 = StringVar()

clicked2.set("Siyah")

# Create Label
label = Label(root, text="Karekod İçeriği")
label.grid(row=0, column=0)
e1 = Entry(root, bg="gray")
e1.grid(row=0, column=1)

# Create Label
label1 = Label(root, text="Arkaplan Rengi")
label1.grid(row=1, column=0)

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.grid(row=1, column=1)


# Create Label
label2 = Label(root, text="Karekod Rengi")
label2.grid(row=2, column=0)
drop2 = OptionMenu(root, clicked2, *options2)
drop2.grid(row=2, column=1)

# Create button, it will change label text
button = Button(root, text="Kare Kod Oluştur",
                command=show).grid(row=3, column=1)

# Create Label
qr_renk = Label(root, text=" ")
qr_renk.grid(row=4, column=1)

arka_plan = Label(root, text=" ")
arka_plan.grid(row=5, column=1)

veri_baslik = Label(root, text=" ")
veri_baslik.grid(row=8, column=0)

veri = Label(root, text=" ")
veri.grid(row=8, column=1)

# Execute tkinter
root.mainloop()
