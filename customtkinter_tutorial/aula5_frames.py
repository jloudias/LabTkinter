import customtkinter as ctk

root = ctk.CTk()
root.geometry("700x700")
root.title("App Treinamento")
root.maxsize(width=900, height=550)
root.minsize(width=500, height=300)
root.resizable(width=False, height=False)

# Aula 5 - Frames

frame1 = ctk.CTkFrame(master=root, width=200, height=330, fg_color="teal")
frame1.place(x=10, y=60)
frame2 = ctk.CTkFrame(master=root, width=200, height=330, fg_color="navy")
frame2.place(x=230, y=60)
frame3 = ctk.CTkFrame(
    master=root,
    width=200,
    height=330,
    fg_color="orange",
    border_color="black",
    border_width=4,
    corner_radius=30,
)
frame3.place(x=440, y=60)


root.mainloop()
