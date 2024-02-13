from tkinter import *  # noqa
from tkinter import ttk
from tkinter import messagebox
import pyperclip as pc
from num2words import num2words as nw

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


root = Tk()
root.title("Num2Word")
root.geometry("400x320")
root.resizable(False, False)

str_number = StringVar()
str_number.set("")

main_frame = Frame(root)
main_frame.pack(side=TOP, expand=True, fill="both")
lbl_number = Label(
    main_frame, text="Enter the number:", font=FONT_LABEL, fg=LABEL_COLOR
)
lbl_number.pack(fill="x", expand=True, pady=5)
txt_number = Entry(main_frame, textvariable=str_number)
txt_number.pack(fill="x", expand=True, padx=5, pady=5)

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
number_text.pack()

bottom_frame = Frame(root, pady=15, padx=15)
bottom_frame.pack(
    side="bottom",
    fill="both",
    expand=True,
)
ttk.Separator(
    master=bottom_frame,
    orient=HORIZONTAL,
    style="blue.TSeparator",
    class_=ttk.Separator,
    takefocus=1,
    cursor="",
).grid(row=0, column=0, ipadx=12, pady=10)

btn_submit = ttk.Button(bottom_frame, text="Submit", width=10, command=convert_number)
btn_submit.grid(row=0, column=1, padx=10)

btn_clear = ttk.Button(bottom_frame, text="Clear All", width=10, command=clear_all)
btn_clear.grid(row=0, column=2, padx=10)

btn_copy = ttk.Button(
    bottom_frame, text="Copy to Clipboard", width=18, command=copy_text
)
btn_copy.grid(row=0, column=3, padx=10)

ttk.Separator(
    master=bottom_frame,
    orient=HORIZONTAL,
    style="blue.TSeparator",
    class_=ttk.Separator,
    takefocus=1,
    cursor="",
).grid(row=0, column=4, ipadx=12, pady=10)


root.mainloop()
