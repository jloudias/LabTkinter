from tkinter import *  # noqa
from tkinter import ttk
from tkinter import messagebox
import pyperclip as pc
from num2words import num2words as nw
from PIL import ImageTk, Image

LANGUAGE = "pt_BR"
FONT_LABEL = ("Arial", 9, "normal")
LABEL_COLOR = "blue"


def convert_number():
    try:
        float_number = float(str_number.get())
        match op.get():
            case 1:
                option = "cardinal"
            case 2:
                option = "ordinal"
                float_number = round(float_number)
            case 3:
                option = "currency"
            case _:
                option = "cardinal"
        text_of_number = nw(number=float_number, lang=LANGUAGE, to=option)
        number_text.configure(state="normal")
        number_text.insert("end-1c", text_of_number)
    except ValueError:
        messagebox.showerror(
            "Erro", "O valor informado não é um número válido.\nTente novamente."
        )
        clear_all()
        txt_number.focus()


def clear_all():
    str_number.set("")
    op.set = 1
    number_text.delete("1.0", "end-1c")
    number_text.configure(state="disabled")
    txt_number.focus()


def copy_text():

    try:
        the_text = number_text.get("1.0", "end-1c")
        pc.copy(the_text)
        messagebox.showinfo(
            "Informação",
            "Texto copiado com sucesso.",
        )
    except Exception:
        messagebox.showwarning(
            "Atenção",
            "Ocorreu um problema durante a cópia. Contacte o Administrador.",
        )


def exit_app():
    if messagebox.askyesno("Exit", "Are you sure?"):
        root.quit()
    else:
        clear_all()


def about():
    ABOUT_COLOR = "#E3CF57"  # banana color
    top_about = Toplevel(bg=ABOUT_COLOR)
    top_about.title("About")
    top_about.geometry("300x150")

    about_title = Label(
        top_about,
        text="NUMBER TO WORDS\nby Jorge",
        font=("Arial", 10, "bold"),
        bg=ABOUT_COLOR,
    )
    about_text = Label(
        top_about,
        text="A simple app to convert a number\nto correspondent words.\n\nATTENTION:\n1. The number must be a float (with decimal point)\n2.'Copy' sends text to clipboard.",
        font=("Arial", 8, "normal"),
        bg=ABOUT_COLOR,
    )
    about_title.pack()
    about_text.pack(expand=True, fill="both", padx=5)


root = Tk()
root.title("Num2Word")
root.geometry("500x320")
root.resizable(False, False)


str_number = StringVar()
str_number.set("")

right_frame = Frame(root, width=100, bg="black")
right_frame.pack(side="left", fill="y")

img = ImageTk.PhotoImage(Image.open("images/number.png"))
lbl_imagem = Label(right_frame, image=img, width=50, height=50, bg="black")
lbl_imagem.pack(pady=12)

style = ttk.Style()
# style.theme_use("clearlook")
style.configure("my.TButton", foreground="black", background="black")

btn_submit = ttk.Button(
    right_frame, text="Submit", width=8, command=convert_number, style="my.TButton"
)
btn_submit.pack(padx=10, pady=10)

btn_clear = ttk.Button(
    right_frame, text="Clear All", width=8, command=clear_all, style="my.TButton"
)
btn_clear.pack(padx=10, pady=10)

btn_copy = ttk.Button(
    right_frame, text="Copy", width=8, command=copy_text, style="my.TButton"
)
btn_copy.pack(padx=10, pady=10)

btn_about = ttk.Button(
    right_frame, text="About", width=8, command=about, style="my.TButton"
)
btn_about.pack(padx=10, pady=10)

btn_exit = ttk.Button(
    right_frame, text="Exit", width=8, command=exit_app, style="my.TButton"
)
btn_exit.pack(padx=10, pady=10)


main_frame = Frame(root, width=500)
main_frame.pack(side=LEFT, fill="x", padx=10)
lbl_number = Label(
    main_frame, text="Enter the number:", font=FONT_LABEL, fg=LABEL_COLOR
)
lbl_number.pack(fill="x", expand=True, pady=5)
txt_number = Entry(main_frame, textvariable=str_number)
txt_number.pack(fill="x", expand=True, padx=5, pady=5)
txt_number.focus()

# campo operação
op = IntVar()
op.set(1)
lbl_operacao = Label(main_frame, text="Show as: ", font=FONT_LABEL, fg=LABEL_COLOR)
lbl_operacao.pack(fill="x", expand=True, padx=15, pady=5)
opt_cardinal = Radiobutton(main_frame, text="Cardinal", variable=op, value=1)
opt_ordinal = Radiobutton(main_frame, text="Ordinal", variable=op, value=2)
opt_currency = Radiobutton(main_frame, text="Currency", variable=op, value=3)

opt_cardinal.pack(expand=True, fill="x")
opt_ordinal.pack(expand=True, fill="x")
opt_currency.pack(expand=True, fill="x")

lbl_text = Label(main_frame, text="The text", font=FONT_LABEL, fg=LABEL_COLOR)
lbl_text.pack(expand=True, pady=5)
number_text = Text(main_frame, width=46, height=4, state="disabled")
number_text.pack(padx=5)

root.mainloop()
