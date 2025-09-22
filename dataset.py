import tkinter as tk
from tkinter import *
from tkinter import ttk
import pandas as pd
from tkinter import messagebox
from PIL import Image, ImageTk

class Dataset:
    def __init__(self,root):
        # Function to load and display dataset
        def load_dataset():
            try:
                    # Read the dataset
                    file_path="Housing.csv"
                    data = pd.read_csv(file_path)
                    
                    # Clear any existing data in the treeview
                    for row in tree.get_children():
                        tree.delete(row)
                    
                    # Add column headers to the treeview
                    tree["columns"] = list(data.columns)
                    tree["show"] = "headings"  # Hide the first empty column
                    
                    for col in data.columns:
                        tree.heading(col, text=col)
                        tree.column(col, width=120, anchor="center")
                    
                    # Add rows to the treeview
                    for _, row in data.iterrows():
                        tree.insert("", "end", values=list(row))
                    
                    # Update status label
                    status_label.config(text=f"Dataset Loaded: {file_path.split('/')[-1]}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        # Create the main Tkinter window
        self.root=root
        self.root.title("Dataset Viewer")
        self.root.geometry("1920x900")

        # Add background image for aesthetics
        bg_image = Image.open("bg3.jpg")  # Replace with your background image
        bg_image = bg_image.resize((700, 800), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.place(x=0,y=0)

        # Main Frame (semi-transparent for aesthetics)
        main_frame = tk.Frame(self.root, bg="#33415C", bd=2, relief="ridge")
        main_frame.place(x=700, y=0, width=850, height=800)

        # Header Label
        header_label = tk.Label(
            main_frame,
            text="📊 Dataset Viewer",
            font=("Times New Roman", 40, "bold"),
            bg="#33415C",
            fg="#D9DCD6"
        )
        header_label.pack(pady=10)

        # Treeview to display dataset
        tree_frame = tk.Frame(main_frame, bg="#33415C", relief="ridge", bd=2)
        tree_frame.pack(fill="both", expand=True)

        tree = ttk.Treeview(tree_frame)
        tree.pack(fill="both", expand=True)

        # Add scrollbar to the treeview
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        # Button to load dataset
        load_button = tk.Button(
            main_frame,
            text="Load Dataset",
            font=("Times New Roman", 16, "bold"),
            bg="#81C3D7",
            fg="#002855",
            relief="ridge",
            bd=3,
            command=load_dataset
        )
        load_button.pack(pady=10)

        # Status Label
        status_label = tk.Label(
            main_frame,
            text="Let data guide you to your next home!",
            font=("Times New Roman", 14, "italic"),
            bg="#33415C",
            fg="#D9DCD6"
        )
        status_label.pack(pady=5)

        # Footer
        footer_label = tk.Label(
            main_frame,
            text="👩‍💻 Developed by A2D | 📧 Contact: a2d383961@gmail.com",
            font=("Times New Roman", 10),
            bg="#33415C",
            fg="#D9DCD6"
        )
        footer_label.pack(side="bottom", pady=10)

# Run the Tkinter application
if __name__=="__main__":
    root=Tk()
    obj=Dataset(root)
    root.mainloop()