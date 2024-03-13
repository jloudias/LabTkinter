import tkinter as tk
import customtkinter as ctk


root = ctk.CTk()
root.geometry("600x400")
root.minsize(width=600, height=400)
root.resizable(False, False)
root.title("Sliders")

ctk.set_appearance_mode("dark")
LABEL_FONT = ("Roboto", 22, "bold")


top_title = ctk.CTkLabel(
    master=root,
    text="Lesson 15 - Mastering Sliders",
    font=LABEL_FONT,
    text_color="orange",
)
top_title.pack(pady=20)

lbl_value = ctk.CTkLabel(master=root, text="", font=("Arial", 16), text_color="red")


def show_slider_value(value):
    # if value <= 10:
    #     slider.configure(fg_color="red", progress_color="red")
    # else:
    #     slider.configure(fg_color="orange", progress_color="orange")

    lbl_value.configure(text=f"Slider value is: {int(value)}")
    lbl_value.pack(pady=30)


slider = ctk.CTkSlider(
    master=root,
    width=400,
    # height: int | None = None,
    # corner_radius: int | None = None,
    # button_corner_radius: int | None = None,
    # border_width: int | None = None,
    # button_length: int | None = None,
    # bg_color: str | Tuple[str, str] = "transparent",
    # fg_color="orange",
    # border_color: str | Tuple[str, str] = "transparent",
    # progress_color="orange",
    # button_color: str | Tuple[str, str] | None = None,
    button_hover_color="cadetblue",
    from_=0,
    to=100,
    # state: str = "normal",
    # number_of_steps: int | None = None,
    # hover: bool = True,
    command=show_slider_value,
    # variable: Variable | None = None,
    # orientation: str = "horizontal",
)
slider.pack(pady=30)


root.mainloop()
