import tkinter as tk


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.entry = tk.Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botões
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("=", 4, 2),
            ("+", 4, 3),
        ]

        for text, row, col in buttons:
            self.button = tk.Button(
                master,
                text=text,
                padx=20,
                pady=20,
                command=lambda t=text: self.button_click(t),
            )
            self.button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, value):
        if value == "=":
            self.calculate()
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + value)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
