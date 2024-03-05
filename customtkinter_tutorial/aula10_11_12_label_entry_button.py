import customtkinter as ctk

root = ctk.CTk()
root.geometry("600x480")
root.title("Labels and Entry")


def submit():
    lbl_hide.configure(text=f"Hello, {ent_username.get()}. Are you experienced?")
    lbl_hide.pack(pady="20")


lbl_title = ctk.CTkLabel(
    master=root,
    width=300,
    height=50,
    corner_radius=15,
    bg_color="transparent",
    fg_color="navy",
    text_color="white",
    # text_color_disabled = None,
    text="Using Labels and Entrys",
    font=("Roboto", 22, "bold"),
    # image: CTkImage | None = None,
    # compound: str = "center",
    anchor="center",
    # wraplength: int = 0,
)
lbl_title.pack(pady=20)

ent_username = ctk.CTkEntry(
    master=root,
    # corner_radius=15,
    border_width=None,
    bg_color="transparent",
    fg_color=None,
    border_color=None,
    text_color=None,
    # placeholder_text_color = None,
    # textvariable = None,
    placeholder_text="Your name",
    font=None,
    state="normal",
    width=300,
    height=30,
)
ent_username.pack(pady=20)

btn_submit = ctk.CTkButton(
    master=root,
    text="Submit",
    command=submit,
    # width: int = 140,
    # height: int = 28,
    # corner_radius: int | None = None,
    # border_width=1,
    # border_spacing: int = 2,
    # bg_color: str | Tuple[str, str] = "transparent",
    # fg_color: str | Tuple[str, str] | None = None,
    # hover_color: str | Tuple[str, str] | None = None,
    # border_color="navy",
    # text_color: str | Tuple[str, str] | None = None,
    # text_color_disabled: str | Tuple[str, str] | None = None,
    # background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
    # round_width_to_even_numbers: bool = True,
    # round_height_to_even_numbers: bool = True,
    # font: tuple | CTkFont | None = None,
    # textvariable: Variable | None = None,
    # image: CTkImage | Any | None = None,
    # state: str = "normal",
    # hover: bool = True,
    # compound: str = "left",
    # anchor: str = "center"
)
btn_submit.pack(pady=20)


lbl_hide = ctk.CTkLabel(root, text="", text_color="#008040", font=("Arial", 20, "bold"))
lbl_hide.pack(pady="20")

root.mainloop()
