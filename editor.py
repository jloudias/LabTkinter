# Editor de texto simples
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import ctypes
import os

ctypes.windll.shcore.SetProcessDpiAwareness(1)  # otimiza resolução da GUI do TKINTER

PROGRAMA_NOME = " Editor de Texto Simples "
file_name = None

# Janela principal
root = tk.Tk()
root.title(PROGRAMA_NOME)
root.geometry("800x500")
root.resizable(False, False)


def faz_nada():
    messagebox.showinfo(title="Aviso", message="Sou uma função que não faz nada!!")


def recortar():
    content_text.event_generate("<<Cut>>")  # texto tem que ser em inglês
    on_content_changed()
    return 'break'  # avisa ao sistema q o evento foi executado e q não deve mais ser propagado


def copiar():
    content_text.event_generate("<<Copy>>")  # texto tem que ser em inglês
    return 'break'


def colar():
    content_text.event_generate("<<Paste>>")  # texto tem que ser em inglês
    on_content_changed()
    return 'break'


def desfazer():
    content_text.event_generate("<<Undo>>")
    on_content_changed()
    return 'break'


def refazer(_event=None):  # _ na frente do nome da variavel informa ao pycharm que ela não sera utilizada
    content_text.event_generate("<<Redo>>")
    on_content_changed()
    return 'break'


# noinspection PyUnusedLocal
def localizar(event=None):
    # janela de pesquisa toplevel
    search_toplevel = tk.Toplevel(root)
    search_toplevel.title("Localizar texto")
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    # componentes da janela de pesquisa
    tk.Label(search_toplevel, text="Pesquisar tudo: ").grid(row=0, column=0, sticky="e")
    search_entry = tk.Entry(search_toplevel, width=25)
    search_entry.grid(row=0, column=1, padx=2, pady=2, stick="we")
    search_entry.focus_set()

    ignore_case_value = tk.IntVar()
    tk.Checkbutton(
        search_toplevel,
        text='Ignorar Maiúscula/Minúscula',
        variable=ignore_case_value).grid(row=1, column=1, sticky="e", padx=2, pady=2)
    tk.Button(
        search_toplevel,
        text="Localizar Todas",
        underline=0,
        command=lambda: search_output(
            search_entry.get(),
            ignore_case_value.get(),
            content_text,
            search_toplevel,
            search_entry)).grid(row=0, column=2, sticky="e" + "w", padx=2, pady=2)

    def close_search_window():
        content_text.tag_remove('match', '1.0', tk.END)
        search_toplevel.destroy()

    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return "break"


def search_output(needle, if_ignore_case, p_content_text, search_toplevel, search_box):
    p_content_text.tag_remove('match', '1.0', tk.END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos,
                                            nocase=if_ignore_case, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config(
            'match', foreground='red', background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))


# noinspection PyUnusedLocal
def selecionar_tudo(event=None):  # comentário 'noinspect PyUnusedLocal' desabilita warning de variável não utilizada
    content_text.tag_add('sel', '1.0', 'end')
    return 'break'


# noinspection PyUnusedLocal
def abrir_arquivo(event=None):
    input_file_name = filedialog.askopenfilename(defaultextension=".txt",
                                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAMA_NOME))
        content_text.delete(1.0, tk.END)
        with open(file_name) as file:
            content_text.insert(1.0, file.read())


def salvar_arquivo(event=None):
    global file_name
    if not file_name:
        salvar_arquivo_como()
    else:
        escrever_no_arquivo(file_name)
    return "break"


def salvar_arquivo_como(event=None):
    input_file_name = tk.filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        escrever_no_arquivo(file_name)
        root.title(f"{os.path.basename(file_name)} - {PROGRAMA_NOME}")
    return "break"


def novo_arquivo(event=None):
    root.title("Sem título")
    global file_name
    file_name = None
    content_text.delete(1.0, tk.END)


def escrever_no_arquivo(file_name):
    try:
        content = content_text.get(1.0, tk.END)
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass


def exibir_mensagem_sobre(event=None):
    messagebox.showinfo("Sôbre...", f"{PROGRAMA_NOME}\n\nTkinter Gui Application\nDevelopment Blueprints")


def exibir_mensagem_ajuda(event=None):
    messagebox.showinfo("Ajuda", "Help Book: \nTkinter Gui Application\nDevelopment Blueprints", icon='question')


def sair(event=None):
    if messagebox.askokcancel("Sair?.", "Finalizar o programa?"):
        root.destroy()


def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = content_text.index("end").split('.')
        # content_text.index("end") retorna uma string com a posição do final do arquivo no formato '3.0'
        # slipt('.') retorna uma lista com dois valores da string acima
        # row, col recebem sequencialmente os valores da lista gerada acima

        for i in range(1, int(row)):
            output += str(i) + '\n'  # output é uma string contendo os números da linhas seguidos de \n
    return output


def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', tk.END)
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')


def show_cursor_info_bar():
    show_cursor_info_checked = show_cursor_info.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand=0, fill='none', side='right', anchor='se')
    else:
        cursor_info_bar.pack_forget()


def update_cursor_info_bar():
    row, col = content_text.index('insert').split('.')
    line_num, col_num = str(int(row)), str(int(col) + 1)
    infotext = f"Line: {line_num} | Column: {col_num}"
    cursor_info_bar.config(text=infotext)


def on_content_changed(event=None):
    update_line_numbers()
    update_cursor_info_bar()


def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0, tk.END)
    content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)


def undo_highlight():
    content_text.tag_remove("active_line", 1.0, tk.END)


def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()


def change_theme(event=None):
    selected_theme = theme_choice.get()
    fg_bg_colors = color_schemes.get(selected_theme)
    foreground_color, background_color = fg_bg_colors.split('.')
    content_text.config(background=background_color, fg=foreground_color)


def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)


# ============
# Imagens
# ============
ICONE_NOVO = ImageTk.PhotoImage(Image.open("icons/new_file.gif"))
ICONE_ABRIR = ImageTk.PhotoImage(Image.open("icons/open_file.gif"))
ICONE_SALVAR = ImageTk.PhotoImage(Image.open("icons/save.gif"))
ICONE_DESFAZER = ImageTk.PhotoImage(Image.open("icons/undo.gif"))
ICONE_REFAZER = ImageTk.PhotoImage(Image.open("icons/redo.gif"))
ICONE_RECORTAR = ImageTk.PhotoImage(Image.open("icons/cut.gif"))
ICONE_COPIAR = ImageTk.PhotoImage(Image.open("icons/copy.gif"))
ICONE_COLAR = ImageTk.PhotoImage(Image.open("icons/paste.gif"))
ICONE_LOCALIZAR = ImageTk.PhotoImage(Image.open("icons/find_text.gif"))

# ==============
# BARRA DE MENUS
# ==============
menu_bar = tk.Menu(root)

# Menu "Arquivo"
# -------------
# tearoff=0 evita linhas pontilhadas ao clicar no menu
menu_arquivo = tk.Menu(menu_bar, tearoff=0)  # --- Início menu "Arquivo"  ---
menu_arquivo.add_command(
    label="Novo",
    accelerator="Ctrl+N",
    compound="left",  # habilita imagem ao lado do texto
    underline=0,
    image=ICONE_NOVO,
    command=novo_arquivo,
)
menu_arquivo.add_command(
    label="Abrir",
    accelerator="Ctrl+O",
    compound="left",
    underline=0,
    image=ICONE_ABRIR,
    command=abrir_arquivo,
)
menu_arquivo.add_command(
    label="Salvar",
    accelerator="Ctrl+S",
    compound="left",
    underline=0,
    image=ICONE_SALVAR,
    command=salvar_arquivo,
)
menu_arquivo.add_command(
    label="Salvar como",
    accelerator="Shift+Ctrl+S",
    compound="left",
    underline=0,
    command=salvar_arquivo_como,
)
menu_arquivo.add_separator()
menu_arquivo.add_command(
    label="Sair",
    accelerator="Alt+F4",
    compound="left",
    underline=0,
    command=sair,
)

menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)  # ---  Fim do Menu Arquivo ---

# Menu "Editar"
# -------------
menu_editar = tk.Menu(menu_bar, tearoff=0)

menu_editar.add_command(
    label="Desfazer",
    accelerator="Ctrl+Z",
    compound="left",
    image=ICONE_DESFAZER,
    command=desfazer,
)
menu_editar.add_command(
    label="Refazer",
    accelerator="Ctrl+Y",
    compound="left",
    image=ICONE_REFAZER,
    command=refazer,
)
menu_editar.add_separator()

menu_editar.add_command(
    label="Recortar",
    accelerator="Ctrl+X",
    compound="left",
    image=ICONE_RECORTAR,
    command=recortar,
)
menu_editar.add_command(
    label="Copiar",
    accelerator="Ctrl+C",
    compound="left",
    image=ICONE_COPIAR,
    command=copiar,
)
menu_editar.add_command(
    label="Colar",
    accelerator="Ctrl+V",
    compound="left",
    image=ICONE_COLAR,
    command=colar,
)

menu_editar.add_separator()

menu_editar.add_command(
    label="Localizar...",
    accelerator="Ctrl+F",
    compound="left",
    command=localizar,
)
menu_editar.add_separator()

menu_editar.add_command(
    label="Selecionar tudo",
    accelerator="Ctrl+A",
    compound="left",
    command=selecionar_tudo,
)

menu_bar.add_cascade(label="Editar", menu=menu_editar)

# Menu "Exibir"
# -------------
menu_exibir = tk.Menu(menu_bar, tearoff=0)

show_line_number = tk.IntVar()
show_line_number.set(1)
menu_exibir.add_checkbutton(
    label="Exibir número da linha", variable=show_line_number
)

show_cursor_info = tk.IntVar()
show_cursor_info.set(1)
menu_exibir.add_checkbutton(label="Exibir posição do cursor", variable=show_cursor_info, command=show_cursor_info_bar)

to_highlight_line = tk.IntVar()
menu_exibir.add_checkbutton(
    label="Destacar linha atual", variable=to_highlight_line, onvalue=1, offvalue=0, command=toggle_highlight
)

menu_exibir.add_separator()

menu_temas = tk.Menu(menu_bar, tearoff=0)
menu_exibir.add_cascade(label="Temas", menu=menu_temas)
"""
color scheme is defined with dictionary elements like -
        theme_name : foreground_color.background_color
"""
color_schemes = {
    "Default": "#000000.#FFFFFF",
    "Greygarious": "#83406A.#D1D4D1",
    "Aquamarine": "#5B8340.#D1E7E0",
    "Bold Beige": "#4B4620.#FFF0E1",
    "Cobalt Blue": "#ffffBB.#3333aa",
    "Olive Green": "#D1E7E0.#5B8340",
    "Night Mode": "#FFFFFF.#000000",
}
theme_choice = tk.StringVar()
theme_choice.set("Default")
for k in sorted(color_schemes):
    menu_temas.add_radiobutton(label=k, variable=theme_choice, command=change_theme)

menu_bar.add_cascade(label="Exibir", menu=menu_exibir)

# Menu "Sobre"
# ------------
menu_ajuda = tk.Menu(menu_bar, tearoff=0)

menu_ajuda.add_command(
    label="Ajuda",
    compound="left",
    command=exibir_mensagem_ajuda,
)

menu_ajuda.add_separator()

menu_ajuda.add_command(
    label="Sobre...",
    command=exibir_mensagem_sobre,
)

menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

root.config(menu=menu_bar)

# =======================
# BARRA DE FERRAMENTAS
# =======================
shortcut_bar = tk.Frame(root, height=25, background="light sea green")
shortcut_bar.pack(expand=0, fill="x")
# criando os botões com imagem e comando
btn_novo_arquivo = tk.Button(shortcut_bar, image=ICONE_NOVO, command=novo_arquivo)
btn_abrir_arquivo = tk.Button(shortcut_bar, image=ICONE_ABRIR, command=abrir_arquivo)
btn_salvar_arquivo = tk.Button(shortcut_bar, image=ICONE_SALVAR, command=salvar_arquivo)
btn_recortar = tk.Button(shortcut_bar, image=ICONE_RECORTAR, command=recortar)
btn_copiar = tk.Button(shortcut_bar, image=ICONE_COPIAR, command=copiar)
btn_colar = tk.Button(shortcut_bar, image=ICONE_COLAR, command=colar)
btn_desfazer = tk.Button(shortcut_bar, image=ICONE_DESFAZER, command=desfazer)
btn_refazer = tk.Button(shortcut_bar, image=ICONE_REFAZER, command=refazer)
btn_localizar = tk.Button(shortcut_bar, image=ICONE_LOCALIZAR, command=localizar)
# pack no frame
btn_novo_arquivo.pack(side="left")
btn_abrir_arquivo.pack(side="left")
btn_salvar_arquivo.pack(side="left")
btn_recortar.pack(side="left")
btn_copiar.pack(side="left")
btn_colar.pack(side="left")
btn_desfazer.pack(side="left")
btn_refazer.pack(side="left")
btn_localizar.pack(side="left")

# ==========================
# BARRA DE NÚMERO DAS LINHAS
# ==========================
line_number_bar = tk.Text(
    root,
    width=4,
    padx=3,
    takefocus=0,
    border=0,
    background="khaki",
    state="disabled",
    wrap="none",
)
line_number_bar.pack(side="left", fill="y")

# ==================================
# TEXTO PRINCIPAL
# ==================================
content_text = tk.Text(root, wrap="word", undo=True)
content_text.tag_configure('active_line', background='ivory2')

# Eventos
# -------
content_text.bind('<Control-F>', localizar)
content_text.bind('<Control-f>', localizar)
content_text.bind('<Control-y>', refazer)
content_text.bind('<Control-Y>', refazer)
content_text.bind('<Control-A>', selecionar_tudo)
content_text.bind('<Control-a>', selecionar_tudo)
content_text.bind('<Control-o>', abrir_arquivo)
content_text.bind('<Control-O>', abrir_arquivo)
content_text.bind('<Control-s>', salvar_arquivo)
content_text.bind('<Control-S>', salvar_arquivo)
content_text.bind('<Control-n>', novo_arquivo)
content_text.bind('<Control-N>', novo_arquivo)
content_text.bind('<KeyPress-F1>', exibir_mensagem_ajuda)
content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.pack(expand=1, fill="both")

# Barra de rolagem
# ----------------
scroll_bar = tk.Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side="right", fill="y")

# Cursor
# NOTE: position on code matters
# ------
cursor_info_bar = tk.Label(content_text, text="Line: 1 | Column: 1")
cursor_info_bar.pack(expand=0, fill='none', side='right', anchor='se')

# Context menu
# -------------
popup_menu = tk.Menu(content_text)
for i in ('recortar', 'copiar', 'colar', 'desfazer', 'refazer'):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Selecionar Tudo', underline=7, command=selecionar_tudo)

content_text.bind('<Button-3>', show_popup_menu)

root.protocol("WM_DELETE_WINDOW", sair)
root.mainloop()
