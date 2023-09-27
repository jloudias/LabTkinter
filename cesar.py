import tkinter as tk
from tkinter import messagebox

import ctypes
import pyperclip
from PIL import ImageTk, Image

ctypes.windll.shcore.SetProcessDpiAwareness(1)  # otimiza resolução da GUI do TKINTER

# CONSTANTES E VARIÁVEIS
SIMBOLOS = [
    " ",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

FONT_LABEL = ("Arial", 8, "bold")
PADX = 5
PADY = 5


def aplicar_cesar() -> None:
    """Criptografa/descriptografa a mensagem"""
    # noinspection PyUnusedLocal
    posicao = 0
    texto = txt_mensagem.get("1.0", "end-1c").lower()
    operacao = op.get()
    chave = segredo.get()
    novo_texto = ""

    for t in texto:
        if operacao == 1:
            posicao = SIMBOLOS.index(t) + chave
        else:
            posicao = SIMBOLOS.index(t) - chave

        novo_texto += SIMBOLOS[posicao]

    txt_nova_mensagem.configure(state="normal")
    txt_nova_mensagem.insert("end-1c", novo_texto)

    resp = messagebox.askquestion(
        "Copiar Mensagem", "Deseja copiar a nova mensagem para área de transferência?"
    )
    if resp == "yes":
        # noinspection PyBroadException
        try:
            pyperclip.copy(novo_texto)
            messagebox.showinfo(
                "Informação",
                "Mensagem copiada.",
            )
        except Exception:
            messagebox.showwarning(
                "Atenção",
                "Ocorreu um problema durante a cópia. Contacte o Administrador.",
            )


def limpar_formulario() -> None:
    """Retorna os campos do formulário aos seus valores iniciais."""
    segredo.set(3)
    txt_mensagem.delete("1.0", "end-1c")
    txt_nova_mensagem.delete("1.0", "end-1c")
    txt_nova_mensagem.configure(state="disabled")
    btn_ok.configure(state="disabled")
    op.set(1)
    opt_criptografar.focus()


# noinspection PyUnusedLocal
def habilitar_ok(event=None):
    btn_ok.configure(state="normal")
    return "break"


# JANELA PRINCIPAL -> root
# =========================
root = tk.Tk()
root.title("Cifra de César")
root.geometry("670x470")
root.resizable(False, False)

# FRAME ESQUERDO
# ==============
frame_esquerdo = tk.Frame(root)
lbl_titulo = tk.Label(frame_esquerdo, text="Cifra de\nCésar\n", font="Forte 32 bold")
img = ImageTk.PhotoImage(Image.open("cesar70.png"))
lbl_imagem = tk.Label(frame_esquerdo, image=img)

# grid
frame_esquerdo.grid(column=0, row=0, sticky="SW", padx=10)
lbl_titulo.grid(column=0, row=0)
lbl_imagem.grid(column=0, row=1)

# FRAME DIREITO
# =============
frame_direito = tk.Frame(root)

# campo operação
op = tk.IntVar()
op.set(1)
lbl_operacao = tk.Label(frame_direito, text="Selecione a operação: ", font=FONT_LABEL)
opt_criptografar = tk.Radiobutton(
    frame_direito, text="Criptografar", variable=op, value=1
)
opt_descriptografar = tk.Radiobutton(
    frame_direito, text="Descriptografar", variable=op, value=2
)

# campo mensagem original
lbl_mensagem = tk.Label(
    frame_direito, text="Digite a mensagem: ", justify="left", font=FONT_LABEL
)
txt_mensagem = tk.Text(frame_direito, width=34, height=5)
txt_mensagem.bind("<FocusIn>", habilitar_ok)

# campo chave
segredo = tk.IntVar(root, value=3)
lbl_chave = tk.Label(
    frame_direito, text="Informe a chave: ", justify="left", font=FONT_LABEL
)
sp_chave = tk.Spinbox(frame_direito, from_=0, to=33, textvariable=segredo)

# campo nova mensagem
lbl_nova_mensagem = tk.Label(
    frame_direito, text="Nova mensagem: ", justify="left", font=FONT_LABEL
)
txt_nova_mensagem = tk.Text(frame_direito, width=34, height=5, state="disabled")

# grid
frame_direito.grid(column=1, row=0, sticky="W", padx=PADX, pady=PADY)

lbl_operacao.grid(column=0, row=0, sticky="W", padx=PADX, pady=PADY)
opt_criptografar.grid(column=0, row=1, padx=PADX, pady=PADY)
opt_descriptografar.grid(column=1, row=1, padx=PADX, pady=PADY)
lbl_chave.grid(column=0, row=2, sticky="W", padx=PADX, pady=PADY)
sp_chave.grid(column=1, row=2, sticky="W", padx=PADX, pady=PADY)
lbl_mensagem.grid(column=0, row=3, sticky="W", padx=PADX, pady=PADY)
txt_mensagem.grid(column=0, row=4, sticky="W", columnspan=2, padx=PADX, pady=PADY)
lbl_nova_mensagem.grid(column=0, row=5, sticky="W", padx=PADX, pady=PADY)
txt_nova_mensagem.grid(column=0, row=6, sticky="W", columnspan=2, padx=PADX, pady=PADY)

# FRAME BOTOES
# ============
frame_botoes = tk.Frame(frame_direito)
btn_ok = tk.Button(frame_botoes, text="Ok", width=10, state="disabled", command=aplicar_cesar)
btn_limpar = tk.Button(frame_botoes, text="Limpar", width=10, command=limpar_formulario)
btn_sair = tk.Button(frame_botoes, text="Sair", width=10, command=root.quit)

# grid
frame_botoes.grid(column=0, row=7, columnspan=2, padx=PADX, pady=PADY)
btn_ok.grid(column=0, row=0, padx=PADX, pady=10)
btn_limpar.grid(column=1, row=0, padx=PADX, pady=10)
btn_sair.grid(column=2, row=0, padx=PADX, pady=10)

root.mainloop()
