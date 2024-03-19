import customtkinter as ctk
from PIL import Image

LABEL_FONT = ("Roboto", 20, "bold")
APP_TITLE = "Aula 15 - Mastering Segmented Buttons"

# images definitions
image_sat = ctk.CTkImage(
    # light_image=Image.open("images/satia1.jpg"),
    dark_image=Image.open("images/satia1.jpg"),
    size=(120, 120),
)
image_ju = ctk.CTkImage(
    # light_image=Image.open("images/satia1.jpg"),
    dark_image=Image.open("images/ju.jpg"),
    size=(120, 120),
)
image_ss = ctk.CTkImage(
    # light_image=Image.open("images/satia1.jpg"),
    dark_image=Image.open("images/ss.jpg"),
    size=(120, 120),
)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")

        self.title("Segmented Buttons")
        self.geometry("600x480")
        self.top_title = TopTitle(self, APP_TITLE)
        self.main_frame = Main(self)


class TopTitle(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)

        self.lbl_title = ctk.CTkLabel(
            self, text=title, font=LABEL_FONT, text_color="orange"
        ).pack(pady=40)

        self.pack(fill="x")


class Main(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        v_theme = ctk.StringVar()

        def show_image(value):

            match value:
                case "Sátia":
                    v_image = image_sat
                case "Sinthia e Sandro":
                    v_image = image_ss
                case "Jussara":
                    v_image = image_ju

            self.lbl_image.configure(image=v_image)
            self.lbl_image.pack(pady=40)

        def toggle_theme():
            print(v_theme.get())
            if v_theme == "light":
                ctk.set_appearance_mode("light")
            else:
                ctk.set_appearance_mode("dark")

        self.btn_segmented = ctk.CTkSegmentedButton(
            master=self,
            width=140,
            height=36,
            corner_radius=None,
            # border_width=3,
            # bg_color="transparent",
            # fg_color=None,
            # selected_color=None,
            # selected_hover_color=None,
            # unselected_color=None,
            # unselected_hover_color=None,
            # text_color=None,
            # text_color_disabled=None,
            # background_corner_colors=None,
            # font=None,
            values=["Sátia", "Sinthia e Sandro", "Jussara"],
            # variable=None,
            # dynamic_resizing=True,
            command=show_image,
        )
        # self.btn_segmented.set("Sátia")
        self.btn_segmented.pack()

        self.lbl_image = ctk.CTkLabel(self, text="", width=120, height=120)

        self.theme_mode = ctk.CTkSwitch(
            self,
            width=100,
            height=24,
            switch_width=36,
            switch_height=18,
            # corner_radius = None,
            # border_width = None,
            # button_length= None,
            # bg_color = "transparent",
            # fg_color= None,
            # border_color= "transparent",
            # progress_color= None,
            # button_color = None,
            # button_hover_color= None,
            # text_color = None,
            # text_color_disabled= None,
            text="Toggle Theme",
            # font = None,
            # textvariable= None,
            onvalue="dark",
            offvalue="light",
            variable=v_theme,
            # hover= True,
            command=toggle_theme,
            # state= tkinter.NORMAL
        )
        self.theme_mode.pack(pady=30)

        self.pack(expand=True, fill="both")


if __name__ == "__main__":
    root = App()
    root.mainloop()
