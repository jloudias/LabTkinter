import customtkinter as ctk

"""To reflect the layout in the code and follow the principle of always using classes from the intro, we will move the frame and checkbox code into a separate class. """


class MyCheckboxFrame(ctk.CTkFrame):
    """This is a dynamic solution for the checkboxes."""

    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []
        self.title = title

        self.title = ctk.CTkLabel(
            self,
            text=self.title,
            fg_color="gray30",
            corner_radius=6,
            text_color="white",
        )
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            # The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
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

        self._set_appearance_mode("system")
        self.title("My App - OOP")
        self.geometry("400x250")
        self.grid_columnconfigure(0, weight=1)  # expand column
        self.grid_rowconfigure((0, 1), weight=1)  # expand rows

        # Checkbox Section -> moved to MyCheckboxFrame class
        self.checkbox_frame_left = MyCheckboxFrame(
            self,
            values=["Love Python", "Hate Pascal", "Love C/C++"],
            title="Programming Languages",
        )
        self.checkbox_frame_left.grid(
            row=0, column=0, padx=10, pady=(10, 0), sticky="w"
        )
        self.checkbox_frame_right = MyCheckboxFrame(
            self, values=["Doutorado", "Mestrado"], title="Graduação"
        )
        self.checkbox_frame_right.grid(
            row=0, column=1, padx=10, pady=(10, 0), sticky="w"
        )

        # Button Section
        self.button1 = ctk.CTkButton(self, text="Submit", command=self.button_callback)
        self.button1.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("Checked left checkboxes: ", self.checkbox_frame_left.get())
        print("Checked right checkboxes: ", self.checkbox_frame_right.get())


app = App()
app.mainloop()
