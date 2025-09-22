import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class Compare:
    def __init__(self,root):

        # Create the main window
        self.root = root
        self.root.title("Model Comparison")
        self.root.geometry("1920x900")
        self.root.configure(bg="#33415C")

        # Header Label
        header_label = tk.Label(
            self.root,
            text="🖼️Model Comparison",
            font=("Times New Roman", 40, "bold"),
            bg="#33415C",
            fg="#D9DCD6",
        )
        header_label.pack(pady=20)

        # Add 3 images in the first row
        #photo1
        image1 = Image.open("LR.jpg")  # Replace with your background image
        image1 = image1.resize((400, 300), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(image1)

        image1_label = tk.Label(self.root, image=self.photo1)
        image1_label.place(x=80, y=100)

        result1_label = tk.Label(
            self.root,
            text="Linear Regression",
            font=("Times New Roman", 20, "italic"),
            bg="#33415C",
            fg="#D9DCD6"
        )
        result1_label.place(x=160, y=420)

        #photo2
        image2 = Image.open("RF.jpg")  # Replace with your background image
        image2 = image2.resize((400, 300), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(image2)

        image2_label = tk.Label(self.root, image=self.photo2)
        image2_label.place(x=580, y=100)

        result2_label = tk.Label(
            self.root,
            text="Random Forest Regression",
            font=("Times New Roman", 20, "italic"),
            bg="#33415C",
            fg="#D9DCD6"
        )
        result2_label.place(x=630, y=420)

        #photo3
        image3 = Image.open("DT.jpg")  # Replace with your background image
        image3 = image3.resize((400, 300), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(image3)

        image3_label = tk.Label(self.root, image=self.photo3)
        image3_label.place(x=1080, y=100)

        result3_label = tk.Label(
            self.root,
            text="Decision Tree Regression",
            font=("Times New Roman", 20, "italic"),
            bg="#33415C",
            fg="#D9DCD6"
        )
        result3_label.place(x=1140, y=420)

        # Add 1 image in the second row
        image4 = Image.open("score comparison.png")  # Replace with your background image
        image4 = image4.resize((1000, 200), Image.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(image4)

        image4_label = tk.Label(self.root, image=self.photo4)
        image4_label.place(x=280, y=500)

        result4_label = tk.Label(
            self.root,
            text="Various Error Measurement Metrics",
            font=("Times New Roman", 20, "italic"),
            bg="#33415C",
            fg="#D9DCD6"
        )
        result4_label.place(x=590, y=720)

# Run the Tkinter main loop
if __name__=="__main__":
    root=Tk()
    obj=Compare(root)
    root.mainloop()
