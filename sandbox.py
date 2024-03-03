import tkinter as tk

root = tk.Tk()
root.title("Sandbox")
root.geometry("400x300")

# my_canvas = tk.Canvas(root, width=200, height=200, background="blue")
# my_canvas.pack(padx=50, pady=25)

# my_canvas.create_rectangle(10, 10, 80, 80, fill="yellow")
# my_canvas.create_line(90, 90, 150, 90, fill="red")
# my_canvas.create_text(
#     100, 100, text="Desenhando", font=("Arial", 18, "bold"), fill="white"
# )


# Learning Dictionary - count word frequency in a text


# review menu building with tkinter
def sair():
    root.destroy()


def sobre():
    pass


menu_bar = tk.Menu(root)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Exit", command=sair)
menu_bar.add_cascade(menu=menu_file, label="File")

menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="About...", command=sobre)
menu_bar.add_cascade(menu=menu_help, label="Help")

root.config(menu=menu_bar)

root.mainloop()
