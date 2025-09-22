import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import numpy as np
from joblib import load

class Predict:
        def __init__(self,root):

            # Load your trained model (replace with your actual model path)
            model = load("House Price.joblib")
            preprocessing_pipeline = load("My_Pipeline.joblib")

            # Function to predict house price
            def predict_price():
                try:
                    # Get user inputs
                    area = int(entry_area.get())
                    bedrooms = int(entry_bedrooms.get())
                    bathrooms = int(entry_bathrooms.get())
                    stories = int(entry_stories.get())
                    mainroad = 1 if var_mainroad.get() == "Yes" else 0
                    guestroom = 1 if var_guestroom.get() == "Yes" else 0
                    basement = 1 if var_basement.get() == "Yes" else 0
                    hotwaterheating = 1 if var_hotwaterheating.get() == "Yes" else 0
                    airconditioning = 1 if var_airconditioning.get() == "Yes" else 0
                    parking = int(entry_parking.get())
                    preferred_area = 1 if var_preferred_area.get() == "Yes" else 0
                    furnishing_status = furnishing_status_var.get()

                    # Convert categorical `furnishing_status` to numeric values
                    if furnishing_status == "Furnished":
                        furnishing_status = 2
                    elif furnishing_status == "Semi-Furnished":
                        furnishing_status = 1
                    else:
                        furnishing_status = 0

                    # Prepare input array for prediction
                    input_data = np.array([[area, bedrooms, bathrooms, stories, mainroad, guestroom,
                                            basement, hotwaterheating, airconditioning, parking,
                                            preferred_area, furnishing_status]])
                    input_data_preprocessed = preprocessing_pipeline.transform(input_data)
                    
                    # Predict the price
                    price = model.predict(input_data_preprocessed)[0]
                    
                    # Show the result in the result label
                    result_label.config(text=f"Predicted Price: Rs. {price:,.2f}/-")
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please enter valid numbers for all numeric fields.")

            # Create the main Tkinter window
            self.root = root
            self.root.title("House Price Prediction")
            self.root.geometry("1920x900")

            # Add background image
            bg_image = Image.open("bg2.jpg")  # Replace with your background image
            bg_image = bg_image.resize((800, 800), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0)

            # Main Frame (semi-transparent for aesthetics)
            main_frame = tk.Frame(self.root, bg="#16425B", bd=0, relief="ridge")
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

            # Input Section
            input_frame = tk.Frame(main_frame, bg="#D9DCD6", padx=15, pady=15, relief="ridge", bd=2)
            input_frame.pack(pady=50, fill="x", padx=15)

            # Row 1: Area and Bedrooms
            tk.Label(input_frame, text="Area (in sqft):", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=0, column=0, padx=10, pady=5, sticky="w")
            entry_area = ttk.Entry(input_frame, width=20)
            entry_area.grid(row=0, column=1, padx=10, pady=5)

            tk.Label(input_frame, text="Bedrooms:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=0, column=2, padx=10, pady=5, sticky="w")
            entry_bedrooms = tk.StringVar(value=1)
            ttk.Combobox(input_frame, textvariable=entry_bedrooms, values=[1,2,3,4,5,6], state="readonly", width=18).grid(row=0, column=3, padx=10, pady=5)

            # Row 2: Bathrooms and Stories
            tk.Label(input_frame, text="Bathrooms:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=1, column=0, padx=10, pady=5, sticky="w")
            entry_bathrooms = tk.StringVar(value=1)
            ttk.Combobox(input_frame, textvariable=entry_bathrooms, values=[1,2,3,4], state="readonly", width=18).grid(row=1, column=1, padx=10, pady=5)

            tk.Label(input_frame, text="Stories:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=1, column=2, padx=10, pady=5, sticky="w")
            entry_stories = tk.StringVar(value=1)
            ttk.Combobox(input_frame, textvariable=entry_stories, values=[1,2,3,4], state="readonly", width=18).grid(row=1, column=3, padx=10, pady=5)

            # Row 3: Mainroad and Guestroom
            tk.Label(input_frame, text="Main Road Access:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=2, column=0, padx=10, pady=5, sticky="w")
            var_mainroad = tk.StringVar(value="Yes")
            ttk.Combobox(input_frame, textvariable=var_mainroad, values=["Yes", "No"], state="readonly", width=18).grid(row=2, column=1, padx=10, pady=5)

            tk.Label(input_frame, text="Guest Room:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=2, column=2, padx=10, pady=5, sticky="w")
            var_guestroom = tk.StringVar(value="Yes")
            ttk.Combobox(input_frame, textvariable=var_guestroom, values=["Yes", "No"], state="readonly", width=18).grid(row=2, column=3, padx=10, pady=5)

            # Row 4: Basement and Hot Water Heating
            tk.Label(input_frame, text="Basement:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=3, column=0, padx=10, pady=5, sticky="w")
            var_basement = tk.StringVar(value="Yes")
            ttk.Combobox(input_frame, textvariable=var_basement, values=["Yes", "No"], state="readonly", width=18).grid(row=3, column=1, padx=10, pady=5)

            tk.Label(input_frame, text="Hot Water Heating:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=3, column=2, padx=10, pady=5, sticky="w")
            var_hotwaterheating = tk.StringVar(value="Yes")
            ttk.Combobox(input_frame, textvariable=var_hotwaterheating, values=["Yes", "No"], state="readonly", width=18).grid(row=3, column=3, padx=10, pady=5)

            # Row 5: Air Conditioning and Parking
            tk.Label(input_frame, text="Air Conditioning:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=4, column=0, padx=10, pady=5, sticky="w")
            var_airconditioning = tk.StringVar(value="Yes")
            ttk.Combobox(input_frame, textvariable=var_airconditioning, values=["Yes", "No"], state="readonly", width=18).grid(row=4, column=1, padx=10, pady=5)

            tk.Label(input_frame, text="Parking Spaces:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=4, column=2, padx=10, pady=5, sticky="w")
            entry_parking = tk.StringVar(value=0)
            ttk.Combobox(input_frame, textvariable=entry_parking, values=[0,1,2,3], state="readonly", width=18).grid(row=4, column=3, padx=10, pady=5)

            # Row 6: Preferred Area and Furnishing Status
            tk.Label(input_frame, text="Preferred Area:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=5, column=0, padx=10, pady=5, sticky="w")
            var_preferred_area = tk.StringVar(value="Yes")
            ttk.Combobox(input_frame, textvariable=var_preferred_area, values=["Yes", "No"], state="readonly", width=18).grid(row=5, column=1, padx=10, pady=5)

            tk.Label(input_frame, text="Furnishing Status:", font=("Times New Roman", 16), bg="#D9DCD6").grid(row=5, column=2, padx=10, pady=5, sticky="w")
            furnishing_status_var = tk.StringVar(value="Furnished")
            ttk.Combobox(input_frame, textvariable=furnishing_status_var, values=["Furnished", "Semi-Furnished", "Unfurnished"], state="readonly", width=18).grid(row=5, column=3, padx=10, pady=5)

            # Result Section
            result_frame = tk.Frame(main_frame, bg="#16425B", padx=10, pady=10)
            result_frame.pack(fill="x", padx=20)

            result_label = tk.Label(
                result_frame,
                text="Predict your dream home's price with a click!",
                font=("Times New Roman", 20, "italic"),
                bg="#16425B",
                fg="#D9DCD6"
            )
            result_label.pack()

            # Predict Button
            predict_button = tk.Button(
                main_frame,
                text="Predict Price",
                font=("Times New Roman", 16, "bold"),
                bg="#81C3D7",
                fg="#002855",
                relief="ridge",
                bd=3,
                command=predict_price
            )
            predict_button.pack(pady=20)

            # Footer
            footer_label = tk.Label(
                main_frame,
                text="👩‍💻 Developed by A2D | 📧 Contact: a2d383961@gmail.com",
                font=("Times New Roman", 10),
                bg="#16425B",
                fg="#D9DCD6"
            )
            footer_label.pack(side="bottom", pady=10)

    # Run the Tkinter application
if __name__=="__main__":
    root=Tk()
    obj=Predict(root)
    root.mainloop()