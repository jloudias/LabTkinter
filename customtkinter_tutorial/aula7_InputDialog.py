import customtkinter as ctk
import tkinter as tk
from CTkMessagebox import CTkMessagebox

root = ctk.CTk()
root.title("Aula 7 - Caixas de Diálogo")
root.geometry("700x400")
root.resizable(False, False)


def open_dialog():
    dialog = ctk.CTkInputDialog(
        # fg_color: str | Tuple[str, str] | None = None,
        # text_color: str | Tuple[str, str] | None = None,
        # button_fg_color: str | Tuple[str, str] | None = None,
        # button_hover_color: str | Tuple[str, str] | None = None,
        # button_text_color: str | Tuple[str, str] | None = None,
        # entry_fg_color: str | Tuple[str, str] | None = None,
        # entry_border_color="orange",
        # entry_text_color: str | Tuple[str, str] | None = None,
        title="Input Dialog Example",
        # font=() tuple | CTkFont | None = None,
        text="Enter the full user name",
    )

    v_user = f"\n  Hello, {dialog.get_input()}.  \n"
    lbl_welcome.configure(text=v_user)
    lbl_welcome.pack(side="top", pady=10, padx=10)


v_user = ctk.StringVar(root)

lbl_welcome = ctk.CTkLabel(
    master=root,
    # width: int = 0,
    # height: int = 28,
    corner_radius=10,
    # bg_color: str | Tuple[str, str] = "transparent",
    fg_color="teal",
    text_color="white",
    # text_color_disabled: str | Tuple[str, str] | None = None,
    text=None,
    font=("Roboto", 28, "normal"),
    # image: CTkImage | None = None, compound: str = "center",
    # anchor: str = "center",
    # wraplength: int = 0,
)


# tkinter menu review
def do_nothing():
    CTkMessagebox(
        title="Information",
        message="This feature is not available.\n\nCome back later.",
    )


menu_bar = tk.Menu(root)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Exit", command=do_nothing)
menu_bar.add_cascade(menu=menu_file, label="File")

menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="About...", command=do_nothing)
menu_bar.add_cascade(menu=menu_help, label="Help")

root.config(menu=menu_bar)

btn1 = ctk.CTkButton(root, text="Open Input Dialog", command=open_dialog)
btn1.pack(side="bottom", pady=20)


root.mainloop()
