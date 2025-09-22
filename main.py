import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from predict import Predict
from dataset import Dataset
from visualization import Visualize
from comparison import Compare

class Main:
    def __init__(self,root):
        # Create the main Tkinter window
        self.root = root
        self.root.title("House Price Prediction")
        self.root.geometry("1920x900")

        # Add background image
        bg_image = Image.open("bg1.jpg")  # Replace with your background image
        bg_image = bg_image.resize((800, 800), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(root, image=self.bg_photo)
        bg_label.place(x=0, y=0)

        # Main Frame (semi-transparent for aesthetics)
        main_frame = tk.Frame(root, bg="#16425B", bd=0, relief="ridge")
        main_frame.place(x=800, y=0, width=740, height=795)

        # Header
        header_label = tk.Label(
            main_frame,
            text="🏡 House Price Prediction",
            font=("Times New Roman", 40, "bold"),
            bg="#16425B",
            fg="#D9DCD6"
        )
        header_label.pack(pady=20)

        #button1
        image1 = Image.open("bg7.jpg")  # Replace with your background image
        image1 = image1.resize((220, 220), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(image1)

        b1=Button(root,image=self.photo1,command=self.predict,cursor="hand2")
        b1.place(x=900,y=140,width=230,height=230)
        b1_1=tk.Button(root,text="Predict",command=self.predict,cursor="hand2",font=("times new roman",18,"bold"),bg="black",fg="white")
        b1_1.place(x=900,y=360,width=230,height=40)

        #button2
        image2 = Image.open("bg8.jpg")  # Replace with your background image
        image2 = image2.resize((220, 220), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(image2)

        b2=Button(root,image=self.photo2,command=self.dataset,cursor="hand2")
        b2.place(x=1200,y=140,width=230,height=230)
        b2_1=tk.Button(root,text="Dataset",command=self.dataset,cursor="hand2",font=("times new roman",18,"bold"),bg="black",fg="white")
        b2_1.place(x=1200,y=360,width=230,height=40)

        #button3
        image3 = Image.open("bg6.jpg")  # Replace with your background image
        image3 = image3.resize((220, 220), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(image3)

        b3=Button(root,image=self.photo3,command=self.visualize,cursor="hand2")
        b3.place(x=900,y=440,width=230,height=230)
        b3_1=tk.Button(root,text="Visualize",command=self.visualize,cursor="hand2",font=("times new roman",18,"bold"),bg="black",fg="white")
        b3_1.place(x=900,y=660,width=230,height=40)

        #button4
        image4 = Image.open("bg9.jpg")  # Replace with your background image
        image4 = image4.resize((220, 220), Image.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(image4)

        b4=Button(root,image=self.photo4,command=self.compare,cursor="hand2")
        b4.place(x=1200,y=440,width=230,height=230)
        b4_1=tk.Button(root,text="Compare",command=self.compare,cursor="hand2",font=("times new roman",18,"bold"),bg="black",fg="white")
        b4_1.place(x=1200,y=660,width=230,height=40)

        result_label = tk.Label(
                self.root,
                text="Your home's true value predicted for you!",
                font=("Times New Roman", 20, "italic"),
                bg="#16425B",
                fg="#D9DCD6"
        )
        result_label.place(x=940,y=730)

        # Footer
        footer_label = tk.Label(
            main_frame,
            text="👩‍💻 Developed by A2D | 📧 Contact: a2d383961@gmail.com",
            font=("Times New Roman", 10),
            bg="#16425B",
            fg="#D9DCD6"
        )
        footer_label.pack(side="bottom", pady=10)
    
    def predict(self):
        self.new_window=Toplevel(self.root)
        self.app=Predict(self.new_window)

    def dataset(self):
        self.new_window=Toplevel(self.root)
        self.app=Dataset(self.new_window)

    def visualize(self):
        self.new_window=Toplevel(self.root)
        self.app=Visualize(self.new_window)

    def compare(self):
        self.new_window=Toplevel(self.root)
        self.app=Compare(self.new_window)

# Run the Tkinter application
if __name__=="__main__":
    root=Tk()
    obj=Main(root)
    root.mainloop()