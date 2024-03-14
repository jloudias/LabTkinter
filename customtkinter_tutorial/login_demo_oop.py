import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

# The same as login_demo.py but using OOP approach


class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()

        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        ctk.set_appearance_mode("dark")

        # widgets
        self.top_title = TopTitle(self)
        self.main = Main(self)


class TopTitle(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(
            self,
            text="Enter your credentials...",
            font=("Roboto", 20),
            text_color="#FFCC70",
            # fg_color="blue",
        ).pack(expand=True, fill="both")

        self.place(x=0, y=0, relwidth=1, relheight=0.2)


class Main(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.v_username = ctk.StringVar()
        self.v_password = ctk.StringVar()

        self.lbl_username = ctk.CTkLabel(self, text="Enter your name").pack(
            pady=(40, 0)
        )
        self.username = ctk.CTkEntry(
            master=self,
            placeholder_text="Username...",
            width=300,
            text_color="#FFCC70",
            textvariable=self.v_username,
        ).pack(pady=(5, 0))

        self.lbl_password = ctk.CTkLabel(self, text="Enter your password").pack(
            pady=(20, 0)
        )
        self.password = ctk.CTkEntry(
            master=self,
            placeholder_text="Password...",
            width=300,
            text_color="#FFCC70",
            show="*",
            textvariable=self.v_password,
        ).pack(pady=5)

        ctk.CTkButton(
            master=self,
            text="Submit",
            corner_radius=32,
            hover_color="gray",
            fg_color="white",
            text_color="black",
            border_color="#FFCC70",
            border_width=2,
            command=self.submit_form,
        ).pack(pady=(50, 0))

        self.place(x=0, y=80, relwidth=1, relheight=0.8)

    def submit_form(self):
        # CTkMessagebox(title="Info", message="  Working o it...  ")
        print(self.v_username.get())
        print(self.v_password.get())


if __name__ == "__main__":

    root = App("Login", (500, 400))
    root.mainloop()
