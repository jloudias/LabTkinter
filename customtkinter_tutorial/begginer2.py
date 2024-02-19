import customtkinter as ctk

"""To reflect the layout in the code and follow the principle of always using classes from the intro, we will move the frame and checkbox code into a separate class. """


class MyCheckboxFrame(ctk.CTkFrame):
    """This class inherits from CTkFrame and an instance of this class gets created in the main App class. Only the master argument needs to get passed into the __init__ method of the new MyCheckboxFrame and so that it can then get passed to the __init__ of the super class which is the CTkFrame."""

    def __init__(self, master):
        super().__init__(master)
        self.checkbox_1 = ctk.CTkCheckBox(self, text="First Checkbox")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = ctk.CTkCheckBox(self, text="Second Checkbox")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_3 = ctk.CTkCheckBox(self, text="ThirdCheckbox")
        self.checkbox_3.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")

    def get(self):
        """
        Implement a get method for the MyCheckboxFrame class.
        Keyword arguments: self
        Return: a list of strings with the text attributes of the checked checkboxes.
        """

        checked_checkboxes = []
        if self.checkbox_1.get() == 1:
            checked_checkboxes.append(
                self.checkbox_1.cget("text")
            )  # cget gets an attribute value, in case, 'text'
        if self.checkbox_2.get() == 1:
            checked_checkboxes.append(self.checkbox_2.cget("text"))
        if self.checkbox_3.get() == 1:
            checked_checkboxes.append(self.checkbox_3.cget("text"))
        # returns the list
        return checked_checkboxes


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My App - OOP")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)  # expand column
        self.grid_rowconfigure((0, 1), weight=1)  # expand rows

        # Checkbox Section -> moved to MyCheckboxFrame class
        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        # Button Section
        self.button1 = ctk.CTkButton(self, text="Submit", command=self.button_callback)
        self.button1.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("Checked checkboxes: ", self.checkbox_frame.get())


app = App()
app.mainloop()
