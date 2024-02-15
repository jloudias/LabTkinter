import tkinter as tk
import tkinter.ttk as ttk


class DemoApp:
    def __init__(self, master=None):
        # build ui
        self.root = tk.Tk() if master is None else tk.Toplevel(master)
        self.root.configure(background="#d5d5d5", height=200, width=200)
        self.root.overrideredirect("false")
        self.root.resizable(False, False)
        self.root.title("Demo Pygubu")
        self.frame_main = ttk.Frame(self.root, name="frame_main")
        self.frame_main.configure(height=200, width=200)
        self.lbl_question = ttk.Label(self.frame_main, name="lbl_question")
        self.lbl_question.configure(text="What is my favorite programming language?")
        self.lbl_question.grid(column=0, row=0)
        self.entry2 = ttk.Entry(
            self.frame_main
        )  # add self -> you must define an id for the widget
        self.entry2.grid(column=0, pady=5, row=1, sticky="ew")
        frame3 = ttk.Frame(self.frame_main)
        frame3.configure(height=200, width=200)
        self.btn_submit = ttk.Button(frame3, name="btn_submit")
        self.btn_submit.configure(state="normal", text="Submit")
        self.btn_submit.grid(column=0, pady="10 5", row=0)
        self.btn_submit.configure(command=self.on_submit)
        frame3.grid(column=0, row=2)
        self.frame_main.grid(column=0, padx=2, pady=2, row=0)

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

    def on_submit(self):
        if self.entry2.get() == "python":
            print("You're right! It's Python.")
        else:
            print("Oh,no! Try again.")


if __name__ == "__main__":
    app = DemoApp()
    app.run()
