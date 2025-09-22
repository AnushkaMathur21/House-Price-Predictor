import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

class Visualize:
    def __init__(self,root):

        # Create the main Tkinter window
        self.root=root
        self.root.title("Visualization")
        self.root.geometry("1920x900")
        self.root.configure(bg="#16425B")

        # Header Label
        header_label = tk.Label(
            self.root,
            text="📊 Visualization",
            font=("Times New Roman", 40, "bold"),
            bg="#16425B",
            fg="#D9DCD6",
        )
        header_label.pack(pady=15)

        def open_file():
            os.startfile("histogram.jpg")

        def open_file2():
            os.startfile("heatmap.jpg")

        bg_image = Image.open("bg5.jpg")  
        bg_image = bg_image.resize((1550, 750), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=90)

        open_button = tk.Button(
            self.root,
            text="View Histogram",
            font=("Times New Roman", 20, "bold"),
            bg="#16425B",
            fg="white",
            command=open_file
        )
        open_button.place(x=300, y=100)


        open_button2 = tk.Button(
            self.root,
            text="View Heatmap",
            font=("Times New Roman", 20, "bold"),
            bg="#16425B",
            fg="white",
            command=open_file2
        )
        open_button2.place(x=1100, y=100)

# Run the Tkinter application
if __name__=="__main__":
    root=Tk()
    obj=Visualize(root)
    root.mainloop()