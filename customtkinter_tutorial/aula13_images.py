import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("600x480")
root.title("Using Images")

# root.grid_columnconfigure(0, weight=1)

lbl_title = ctk.CTkLabel(
    root,
    text="We Are Family!",
    width=550,
    height=60,
    font=("Roboto", 24, "bold"),
    text_color="orange",
).grid(row=0, column=0, columnspan=3, pady=20, padx=20)

image_sat = ctk.CTkImage(
    # light_image=Image.open("images/satia1.jpg"),
    dark_image=Image.open("images/satia1.jpg"),
    size=(100, 100),
)
image_ju = ctk.CTkImage(
    # light_image=Image.open("images/satia1.jpg"),
    dark_image=Image.open("images/ju.jpg"),
    size=(100, 100),
)
image_ss = ctk.CTkImage(
    # light_image=Image.open("images/satia1.jpg"),
    dark_image=Image.open("images/ss.jpg"),
    size=(100, 100),
)

lbl_sat = ctk.CTkLabel(
    master=root,
    image=image_sat,
    text="",
    corner_radius=30,
)
lbl_ju = ctk.CTkLabel(master=root, image=image_ju, text="")
lbl_ss = ctk.CTkLabel(master=root, image=image_ss, text="")

lbl_ju.grid(row=1, column=0, pady=15, padx=15)
lbl_sat.grid(row=1, column=1, pady=15, padx=15)
lbl_ss.grid(row=1, column=2, pady=15, padx=15)


root.mainloop()
