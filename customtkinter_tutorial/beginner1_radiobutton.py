"""
CUSTOM TKINTER TUTORIAL - BEGGINER

Formulário solicita usuário declare se ama ou odeia o Python. Ao submeter, exibe message box com resultado.

1. Grid System
- uso de 'weight=1' em 'grid_column configure' para extender widgets para toda largura do app
- uso de 'sticky'
- uso de 'columnspan'
2. Emprego de CTKRadioButton, CTkLabel e CTKButton
"""

import customtkinter as ctk

# from tkinter import messagebox
from CTkMessagebox import CTkMessagebox

root = ctk.CTk()
root.title("Tutorial")
root.geometry("400x150")
"""
The grid splits a window or frame into columns and rows, which collapse when they are empty, but adapt to the size of the widgets placed inside them. If you want to center the widget in the example, you would have to give the first column a 'weight' other than zero, so that it does not collapse to the size of the button anymore (use grid_rowconfigure() for rows):
"""
root.grid_columnconfigure((0), weight=1)


def button_clicked():

    status = "love" if radio_var.get() == 1 else "hate"
    CTkMessagebox(
        title="Information",
        message=f"You clicked me!\nBy the way, it seems you {status} Python.",
        # master: Any = None,
        # width: int = 400,
        # height: int = 200,
        option_1="OK",
        # option_2: str = None,
        # option_3: str = None,
        # options: list = [],
        # border_width=3,
        # border_color="blue",
        # button_color: str = "default",
        # bg_color="#290fe1",
        # fg_color="white",
        # text_color: str = "default",
        # title_color="blue",
        # button_text_color: str = "default",
        # button_width: int = None,
        # button_height: int = None,
        # cancel_button_color: str = None,
        # cancel_button: str = None,
        # button_hover_color: str = "default",
        # icon="icons/bulb.ico",
        # icon_size: tuple = None,
        # corner_radius: int = 15,
        # justify: str = "right",
        # font: tuple = None,
        # header: bool = False,
        # topmost: bool = True,
        # fade_in_duration: int = 0,
        # sound: bool = False,
        # option_focus: Literal[1, 2, 3] = None
    )


lbl_title = ctk.CTkLabel(
    master=root,
    text="CustomTkinter Tutorial",
    font=("Roboto", 20),
    text_color="#b95c00",
)
"""
You can also configure the button to expand with it's grid cell if you add a 'sticky' argument to the grid call. 
In the example bellow, the button sticks to the grid cell on the east and west side. 
You can notice that grid cell and therefore the button size adapts if you resize the window.
"""
lbl_title.grid(row=0, column=0, pady=(10, 25), padx=10, sticky="ew", columnspan=2)

radio_var = ctk.IntVar()
opt_1 = ctk.CTkRadioButton(
    root,
    text="Love Python",
    variable=radio_var,
    value=1,
)
opt_1.grid(row=1, column=0, padx=5, pady=5, sticky="w")
opt_2 = ctk.CTkRadioButton(
    root,
    text="Hate Python",
    variable=radio_var,
    value=2,
)
opt_2.grid(row=1, column=1, padx=5, pady=5, sticky="w")

btn_submit = ctk.CTkButton(master=root, text="Click Me", command=button_clicked)
btn_submit.grid(row=2, column=0, padx=10, pady=15, sticky="ew", columnspan=2)


root.mainloop()
