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

        # run
        self.mainloop()


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

        self.username = ctk.CTkEntry(
            master=self, placeholder_text="Username...", width=300, text_color="#FFCC70"
        ).pack(pady=(40, 0))

        self.password = ctk.CTkEntry(
            master=self,
            placeholder_text="Password...",
            width=300,
            text_color="#FFCC70",
            show="*",
        ).pack(pady=20)

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
        ).pack(pady=25)

        self.place(x=0, y=80, relwidth=1, relheight=0.8)

    def submit_form(self):
        CTkMessagebox(title="Info", message="  Working o it...  ")


if __name__ == "__main__":

    App("Login", (500, 400))
