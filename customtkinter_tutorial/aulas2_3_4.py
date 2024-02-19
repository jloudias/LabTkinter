import customtkinter as ctk

# Aula 2 - Customizando a janela principal
# ----------------------------------------
root = ctk.CTk()
root.title("Aula 2")  # título da janela
root.geometry("300x150")  # configura dimensão inicial da janela
root.maxsize(width=500, height=350)  # tamanho máximo da janela
root.minsize(width=250, height=100)  # tamanho mínimo da janela
root.resizable(
    width=True, height=False
)  # permite redimensionar a janela -> dois False desabilita redim
root.focus_set()  # foco na janela principal

# Aula 3 - Customizando o tema
# ----------------------------
root._set_appearance_mode("system")  # aceita 'dark', 'light' e 'system'(default)

# Aula 4 - Criando e alternando múltiplas  janelas
# ------------------------------------------------


def toogle_top(open_top):
    if open_top:
        top_window.deiconify()
        root.iconify()
    else:
        top_window.iconify()
        root.deiconify()


top_window = ctk.CTkToplevel(root, fg_color="teal")
top_window.geometry("300x200")
top_window.title("Top Level")
top_window.iconify()

# Parâmetros para um command de button deve ser passado com função lambda
btn_top = ctk.CTkButton(
    master=root, text="Open Top Window", command=lambda: toogle_top(True)
).place(x=90, y=60)
btn_close_top = ctk.CTkButton(
    master=top_window, text="Close Top Window", command=lambda: toogle_top(False)
).place(x=90, y=60)

root.mainloop()
