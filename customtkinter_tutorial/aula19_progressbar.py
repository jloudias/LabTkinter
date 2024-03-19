import customtkinter as ctk

root = ctk.CTk()
root.title("Aula 19 - Progress Bar")
root.geometry("600x400")
root.resizable(False, False)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
FONT_TITLE = ("Roboto", 18, "bold")


def step_bar():
    pg_test.step()
    lbl_progress.configure(text=pg_test.get())


lbl_title = ctk.CTkLabel(
    root, text="My Progress Bar", font=FONT_TITLE, text_color="orange"
)
lbl_title.pack(pady=30)

pg_test = ctk.CTkProgressBar(
    root,
    width=300,
    height=10,
    #  corner_radius: int | None = None,
    #  border_width: int | None = None,
    #  bg_color: str | Tuple[str, str] = "transparent",
    #  fg_color: str | Tuple[str, str] | None = None,
    #  border_color: str | Tuple[str, str] | None = None,
    progress_color="orange",
    #  variable: Variable | None = None,
    #  orientation: str = "horizontal",
    mode="determinate",  # indeterminate mode progress to max and come back
    determinate_speed=5,
    #  indeterminate_speed: float = 1
)
pg_test.pack()
pg_test.set(0)

btn_start = ctk.CTkButton(
    root, text="Step", width=100, height=40, corner_radius=15, command=step_bar
)
btn_start.pack(pady=60)

lbl_progress = ctk.CTkLabel(root, text="")
lbl_progress.pack(pady=20)
root.mainloop()
