import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

root = ctk.CTk()
root.geometry("700x450")
root.title("Textbox and OptionMenu")
root.resizable(False, False)

TITLE = "Meu Título"
PARAGRAPH = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum scelerisque sapien et sodales consequat. Suspendisse neque metus, lobortis sed accumsan sed, iaculis ut metus. Ut venenatis tincidunt massa, id sollicitudin ante mattis quis. Sed semper diam risus, eget facilisis elit posuere dapibus. Curabitur volutpat lacinia nibh eget tempus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla convallis dictum risus ut sagittis. Vestibulum vitae nisl et nisl rhoncus tincidunt ut et quam. Vestibulum sit amet mauris turpis. Aenean interdum diam lobortis tellus ullamcorper, ut euismod mi faucibus. In sed metus dui. Ut maximus rutrum libero ut euismod.\n\n"

top_frame = ctk.CTkFrame(master=root, width=650, height=100, fg_color="transparent")
top_frame.pack()
lbl_title = ctk.CTkLabel(
    master=top_frame,
    text="My Dinamic Text Box",
    font=("Roboto", 24, "bold"),
    text_color="orange",
    fg_color="transparent",
)
lbl_title.pack(padx=20, pady=20)
top_frame.pack()

main_frame = ctk.CTkFrame(master=root, width=500, height=250, fg_color="transparent")
main_frame.pack(fill="both")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=4)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=18)

lbl_menu = ctk.CTkLabel(master=main_frame, text="Choose text lenght:")
lbl_menu.grid(row=0, column=0, sticky="n")


def toggle_size(size):
    # if size == "Small":
    #     number_of_paragraph = 2
    # elif size == "Medium":
    #     number_of_paragraph = 3
    # elif size == "Big":
    #     number_of_paragraph = 6
    # else:
    #     print("Invalid option!")

    match size:
        case "Small":
            number_of_paragraph = 2
        case "Medium":
            number_of_paragraph = 3
        case "Big":
            number_of_paragraph = 6
        case _:
            number_of_paragraph = 1
            CTkMessagebox(
                title="Warning", message="This is not a valid value!", icon="warning"
            )

    tbox1.delete("1.0", "end")
    tbox1.insert(
        "0.0",
        f"\n'{size}' size has {number_of_paragraph} paragraphs.\n\n{PARAGRAPH*number_of_paragraph}",
    )
    opt_menu.set("Choose text size...")


opt_menu = ctk.CTkOptionMenu(
    master=main_frame,
    values=["Small", "Medium", "Big"],
    # width: int = 140,
    # height: int = 28,
    # corner_radius: int | None = None,
    # bg_color: str | Tuple[str, str] = "transparent",
    # fg_color: str | Tuple[str, str] | None = None,
    # button_color: str | Tuple[str, str] | None = None,
    # button_hover_color: str | Tuple[str, str] | None = None,
    # text_color: str | Tuple[str, str] | None = None,
    # text_color_disabled: str | Tuple[str, str] | None = None,
    # dropdown_fg_color: str | Tuple[str, str] | None = None,
    # dropdown_hover_color: str | Tuple[str, str] | None = None,
    # dropdown_text_color: str | Tuple[str, str] | None = None,
    # font: tuple | CTkFont | None = None,
    # dropdown_font: tuple | CTkFont | None = None,
    # variable: Variable | None = None,
    # state: str = tkinter.NORMAL,
    # hover: bool = True,
    command=toggle_size,
    # dynamic_resizing: bool = True,
    # anchor: str = "w",
    # **kwargs: Any
)
opt_menu.set("Choose text size...")
opt_menu.grid(
    row=1,
    column=0,
    sticky="n",
)


tbox1 = ctk.CTkTextbox(
    master=main_frame,
    width=400,
    height=350,
    # corner_radius: int | None = None,
    border_width=3,
    # border_spacing=5,
    # bg_color: str | Tuple[str, str] = "transparent",
    # fg_color: str | Tuple[str, str] | None = None,
    border_color="teal",
    # text_color: str | None = None,
    scrollbar_button_color="green",
    # scrollbar_button_hover_color: str | Tuple[str, str] | None = None,
    font=("Roboto", 14),
    # activate_scrollbars: bool = True,
    # **kwargs: Any
)
tbox1.grid(row=0, column=1, rowspan=2, sticky="ew", padx=(0, 10))


tbox1.insert("0.0", f"\n{TITLE}\n\n{PARAGRAPH}")


root.mainloop()
