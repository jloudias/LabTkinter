import customtkinter as ctk
from PIL import Image

app = ctk.CTk()
app.geometry("500x400")
app.title("Login")


def submit_form():
    print(f"Username: {txt_login.get()}")
    print(f"Password: {txt_password.get()}")


ctk.set_appearance_mode("dark")
img = Image.open("images/play.gif")

lbl_title = ctk.CTkLabel(
    master=app,
    text="Enter your credentials.",
    font=("Roboto", 20),
    text_color="#FFCC70",
)
lbl_title.place(relx=0.5, rely=0.2, anchor="center")

txt_login = ctk.CTkEntry(
    master=app, placeholder_text="Username...", width=300, text_color="#FFCC70"
)
txt_login.place(relx=0.5, rely=0.4, anchor="center")

txt_password = ctk.CTkEntry(
    master=app,
    placeholder_text="Password...",
    width=300,
    text_color="#FFCC70",
    show="*",
)
txt_password.place(relx=0.5, rely=0.5, anchor="center")

btn_user = ctk.CTkButton(
    master=app,
    text="Submit",
    corner_radius=32,
    hover_color="gray",
    fg_color="white",
    text_color="black",
    border_color="#FFCC70",
    border_width=2,
    command=submit_form,
    # image=ctk.CTkImage(dark_image=img, light_image=img),
)
btn_user.place(relx=0.5, rely=0.8, anchor="center")

app.mainloop()
