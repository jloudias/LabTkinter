import customtkinter as ctk

"""Creating an scrollabelframe to display more checkboxes than there is space in the layout or on the screen """


class MyScrollabelCheckboxFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self._set_appearance_mode("system")
        self.title("My App - OOP")
        self.geometry("400x250")
        self.grid_columnconfigure(0, weight=1)  # expand column
        self.grid_rowconfigure(0, weight=1)  # expand rows

        values = [
            "Jorge Dias",
            "Jussara Belém",
            "Sátia Loureiro",
            "Sinthia Tamayo",
            "Laura Tamayo",
            "Sandro Tamayo",
        ]

        # Checkbox Section -> moved to MyCheckboxFrame class
        self.checkbox_frame = MyScrollabelCheckboxFrame(
            self,
            values=values,
            title="We are Family",
        )
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # Button Section
        self.button1 = ctk.CTkButton(self, text="Submit", command=self.button_callback)
        self.button1.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("Checked: ", self.checkbox_frame.get())


app = App()
app.mainloop()
