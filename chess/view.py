from tkinter import Tk, Menu, Label, Frame, Canvas, RIGHT, messagebox
from configurations import *  # noqa
import controller


class View:
    """Handles the frontend presentation"""

    board_color_1 = BOARD_COLOR_1
    board_color_2 = BOARD_COLOR_2

    def __init__(self, parent, controller):
        self.parent = parent
        self.controller = controller
        self.create_chess_base()
        self.canvas.bind("<Button-1>", self.on_square_clicked)

    #
    # MENU BEGIN -------------------------
    #
    def create_top_menu(self):
        self.menu_bar = Menu(self.parent)  # create menu barr
        self.create_file_menu()
        self.create_edit_menu()
        self.create_about_menu()

    def create_file_menu(self):
        """create file menu, add menu itens, cascade itens and attach menu bar to main window"""
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New Game", command=self.on_new_game_clicked)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.on_exit_clicked)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.parent.config(menu=self.menu_bar)

    def create_edit_menu(self):
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(
            label="Preferences", command=self.on_preferences_menu_clicked
        )
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.parent.config(menu=self.menu_bar)

    def create_about_menu(self):
        self.about_menu = Menu(self.menu_bar, tearoff=0)
        self.about_menu.add_command(label="About", command=self.on_about_menu_clicked)
        self.menu_bar.add_cascade(label="About", menu=self.about_menu)
        self.parent.config(menu=self.menu_bar)

    def on_new_game_clicked(self):
        pass

    def on_exit_clicked(self):
        if messagebox.askyesno("Exit", "Are you sure?"):
            self.parent.destroy()

    def on_preferences_menu_clicked(self):
        pass

    def on_about_menu_clicked(self):
        pass

    # MENU END -----------------------------------------
    
    # CANVAS BEGIN -------------------------------------

    def create_canvas(self):
        canvas_width = NUMBER_OF_COLUMNS * DIMENSION_OF_EACH_SQUARE
        canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
        self.canvas = Canvas(self.parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)

    def on_square_clicked(self, event):
        clicked_row, clicked_column = self.get_clicked_row_column(event)
        print("Hey you clicked on", clicked_row, clicked_column)


    def draw_board(self):
        current_color = BOARD_COLOR_2
        for row in range(NUMBER_OF_ROWS):
            current_color = self.get_alternate_color(current_color)
            for col in range(NUMBER_OF_COLUMNS):
                x1, y1 = self.get_x_y_coordinate(row, col)
                x2, y2 = x1 + DIMENSION_OF_EACH_SQUARE, y1 + DIMENSION_OF_EACH_SQUARE
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,  fill=current_color)
                current_color = self.get_alternate_color(current_color)


    def get_alternate_color(self, current_color):
        if current_color == self.board_color_2:
            next_color = self.board_color_1
        else:
            next_color=self.board_color_2
        return next_color
    
    def get_x_y_coordinate(self, row, col):
        x = (col * DIMENSION_OF_EACH_SQUARE)
        y = ((7 - row) * DIMENSION_OF_EACH_SQUARE)
        return (x, y)
    

    def create_botton_frame(self):
        pass

    def create_chess_base(self):
        self.create_top_menu()
        self.create_canvas()
        self.draw_board()
        self.create_botton_frame()


def main(controller):
    root = Tk()
    root.title("Chess")
    View(root, controller)
    root.mainloop()


def init_new_game():
    game_controller = controller.Controller()
    main(game_controller)


if __name__ == "__main__":
    init_new_game()
