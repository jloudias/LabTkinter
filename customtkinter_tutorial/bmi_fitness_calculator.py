import tkinter as tk
import customtkinter as ctk

# from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Mondial BMI Calculator")
root.iconbitmap("icons/globe.ico")
root.geometry("500x600")
root.resizable(False, False)


def clear_all():
    ent_weight.delete(0, "end")
    ent_height.delete(0, "end")
    lbl_result.configure(text="")


def calculate_bmi():
    category = ""
    our_weight = int(ent_weight.get())
    our_height = int(ent_height.get()) * int(ent_height.get())

    bmi = (our_weight / our_height) * 10000
    bmi_rounded = round(bmi, 1)

    if bmi_rounded < 18.5:
        category = "Underweight"
    elif bmi_rounded <= 24.9:
        category = "Normal"
    elif bmi_rounded <= 29.9:
        category = "Overweight"
    elif bmi_rounded <= 34.9:
        category = "Obese"
    else:
        category = "Extreme Obese"

    lbl_result.configure(
        text=f"Your BMI is {str(bmi_rounded)}.\n\nYour category is {category.upper()}."
    )
    ent_weight.focus()


meter_frame = tk.Frame(root, width=450, height=120, background="black")
meter_frame.pack(fill="both", side="top", padx=(15, 5), pady=10)

# Define an image
# meter_img = ctk.CTkImage(Image.open("images/bmi.png"), size=(420, 200))
# meter_lbl = ctk.CTkLabel(
#     master=meter_frame,
#     image=meter_img,
#     text="",
# ).pack()

# Define the BMI table
lbl_under = ctk.CTkLabel(
    master=meter_frame,
    width=95,
    height=90,
    fg_color="blue",
    text="UNDER\nWEIGHT\n< 18.5",
    text_color="white",
    font=("Roboto", 14, "bold"),
).pack(side="left")

lbl_normal = ctk.CTkLabel(
    master=meter_frame,
    width=95,
    height=90,
    fg_color="green",
    text="NORMAL\n18.5 - 24.9",
    text_color="white",
    font=("Roboto", 14, "bold"),
).pack(side="left")

lbl_over = ctk.CTkLabel(
    master=meter_frame,
    width=95,
    height=90,
    fg_color="#E3CF57",
    text="OVER\nWEIGHT\n25.0 - 29.9",
    text_color="white",
    font=("Roboto", 14, "bold"),
).pack(side="left")

lbl_obese = ctk.CTkLabel(
    master=meter_frame,
    width=95,
    height=90,
    fg_color="orange",
    text="OBESE\n30.0 - 34.9",
    text_color="white",
    font=("Roboto", 14, "bold"),
).pack(side="left")

lbl_extreme = ctk.CTkLabel(
    master=meter_frame,
    width=95,
    height=90,
    fg_color="red",
    text="EXTREME\nOBESE\n>36.0",
    text_color="white",
    font=("Roboto", 14, "bold"),
).pack(side="left")

ent_weight = ctk.CTkEntry(
    master=root,
    width=250,
    height=30,
    border_width=1,
    corner_radius=20,
    border_color="white",
    placeholder_text="Your weight in kilos",
)
ent_weight.pack(pady=(60, 20))

ent_height = ctk.CTkEntry(
    master=root,
    width=250,
    height=30,
    border_width=1,
    corner_radius=20,
    border_color="white",
    placeholder_text="Your height in centimeters",
)
ent_height.pack(pady=20)

btn_calculate = ctk.CTkButton(
    root, text="Calculate BMI", width=200, height=40, command=calculate_bmi
).pack(pady=(30, 20))

btn_clear = ctk.CTkButton(
    root, text="Clear All", width=200, height=40, command=clear_all
).pack(pady=20)

lbl_result = ctk.CTkLabel(
    root, text="", font=("Roboto", 16, "normal"), text_color="orange", width=250
)
lbl_result.pack(pady=40)

root.mainloop()
