import qrcode
from PIL import Image, ImageTk
import tkinter as tk

def generate_qr():
    link = entry_link.get()
    fill_color = entry_fill_color.get()
    back_color = entry_back_color.get()
    qr = qrcode.QRCode(version=1, box_size=3, border=3)
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save('user_qr.png')
    img.show()


root = tk.Tk()
root.title("QR Code Generator")


tk.Label(root, text="Website Link:").grid(row=0)
tk.Label(root, text="Fill Color:").grid(row=1)
tk.Label(root, text="Background Color:").grid(row=2)

entry_link = tk.Entry(root)
entry_fill_color = tk.Entry(root)
entry_back_color = tk.Entry(root)

entry_link.grid(row=0, column=1)
entry_fill_color.grid(row=1, column=1)
entry_back_color.grid(row=2, column=1)

button_generate = tk.Button(root, text="Generate QR Code", command=generate_qr)
button_generate.grid(row=3, columnspan=2)


root.mainloop()
