import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My App - OOP")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)  # expand column
        self.grid_rowconfigure((0, 1), weight=1)  # expand rows

        # Checkbox Section
        self.checkbox_1 = ctk.CTkCheckBox(self, text="First Checkbox")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(self, text="Second Checkbox")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        # Button Section
        self.button1 = ctk.CTkButton(self, text="Submit", command=self.button_callback)
        self.button1.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")


app = App()
app.mainloop()
