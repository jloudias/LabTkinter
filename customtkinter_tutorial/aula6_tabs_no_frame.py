import customtkinter as ctk


root = ctk.CTk()
root.title("My tabs app")
root.geometry("700x400")
root.resizable(False, False)

tab_view = ctk.CTkTabview(
    master=root,
    width=300,
    height=250,
    corner_radius=10,
    border_width=5,
    # bg_color="",
    fg_color="teal",
    border_color="navy",
    segmented_button_fg_color="brown",
    # segmented_button_selected_color= str | Tuple[str, str] | None = None,
    # segmented_button_selected_hover_color= str | Tuple[str, str] | None = None,
    # segmented_button_unselected_color="pink",
    # segmented_button_unselected_hover_color= str | Tuple[str, str] | None = None,
    # text_color= str | Tuple[str, str] | None = None,
    # text_color_disabled= str | Tuple[str, str] | None = None,
    # command= ((...) -> Any) | Any = None,
    anchor="center",
    state="normal",
)
tab_view.pack(pady=40)
#
tab_view.add("Nomes")
tab_view.add("Idades")
tab_view.add("Genero")

tab_view.tab("Nomes").grid_columnconfigure(0, weight=1)
tab_view.tab("Idades").grid_columnconfigure(0, weight=1)
tab_view.tab("Genero").grid_columnconfigure(0, weight=1)

nome1 = ctk.CTkLabel(
    tab_view.tab("Nomes"),
    text="Jorge Loureiro Dias\n\nJussara Belém Loureiro Dias\n\nSátia Belém Loureiro Dias",
    font=("Roboto", 16),
    text_color="white",
)
nome1.pack(pady=5)

idades1 = ctk.CTkLabel(
    tab_view.tab("Idades"),
    text=f"68\n61\n41\n----\n{68+61+41}",
    font=("Roboto", 16),
    text_color="white",
)
idades1.pack(pady=5)

tab_view.tab("Genero").grid_columnconfigure(0, weight=1)

genero1 = ctk.CTkLabel(
    master=tab_view.tab("Genero"),
    text="1",
    font=("Roboto", 32),
    text_color="white",
    height=50,
    width=150,
    fg_color="blue",
    corner_radius=20,
)
genero1.grid(row=0, column=0, pady=10)

genero2 = ctk.CTkLabel(
    master=tab_view.tab("Genero"),
    text="2",
    font=("Roboto", 32),
    text_color="white",
    height=50,
    width=150,
    fg_color="red",
    corner_radius=20,
)
genero2.grid(row=1, column=0, pady=10)

root.mainloop()
