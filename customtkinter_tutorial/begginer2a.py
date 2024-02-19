import customtkinter as ctk

"""To reflect the layout in the code and follow the principle of always using classes from the intro, we will move the frame and checkbox code into a separate class. """


class MyCheckboxFrame(ctk.CTkFrame):
    """This is a dynamic solution for the checkboxes."""

    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            # The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):

        checked_checkboxes = []

        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(
                    checkbox.cget("text")
                )  # cget gets an attribute value, in case, 'text'

        return checked_checkboxes


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My App - OOP")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)  # expand column
        self.grid_rowconfigure((0, 1), weight=1)  # expand rows

        # Checkbox Section -> moved to MyCheckboxFrame class
        cbox_text_values = ["Love Python", "Hate Pascal", "Love C/C++"]
        self.checkbox_frame = MyCheckboxFrame(self, cbox_text_values)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        # Button Section
        self.button1 = ctk.CTkButton(self, text="Submit", command=self.button_callback)
        self.button1.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("Checked checkboxes: ", self.checkbox_frame.get())


app = App()
app.mainloop()
