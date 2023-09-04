from tkinter import (Tk, Button, Entry, Frame)
import sysconfig
import re
from term_calc import McCalc

so = sysconfig.get_platform()
print(f"Sistema operacional: \033[31m[{so}]\033[0m")


class CalcGUI:
    tela = Tk()
    tela.title("Calculadora")
    tela.geometry("320x465")  # 320x455 é o padrão
    tela.resizable(False, False)
    bg = "#ff8e42"
    bt_bg_color = "#ff6014"
    h_bt_color = "red"
    a_bt_fg_color = "#222"
    a_bt_bg_color = "#ff6014"
    a_bt_sum_color = "#ff0c2d"
    bt_sum_bg_color = "#ff0c2d"
    a_bt_sum_fg_color = "black"
    a_bt_sum_bg_color = "#c20b22"
    tela.configure(bg=bg)
    # data_entry = None
    digitos = None
    col1 = 0.01
    col2 = 0.26
    col3 = 0.51
    col4 = 0.76
    row1 = 0.02
    row2 = 0.18
    row3 = 0.34
    row4 = 0.50
    row5 = 0.66
    row6 = 0.82
    pad_x: int = 4
    pad_y: int = pad_x
    gap = 5
    bt_font_size = 24
    bt_size_w: int = 70
    bt_size_h: int = 50
    bt_border_width = 1.5
    bt_font: str = "consolas"
    # Funcionais
    flag_state = False
    x = None
    y = None
    op = None

    def __init__(self) -> None:
        self.data_entry = None
        self.display()
        self.botoes()

    def start(self):
        self.tela.mainloop()

    def display(self) -> None:
        check_num = (self.tela.register(self.validate), '%P')

        self.data_entry = Entry(self.tela, insertwidth=2, font=(self.bt_font, 30), justify="right", validate="key",
                                validatecommand=check_num)
        self.data_entry.place(x=10, y=10, width=300, height=100)
        self.data_entry.bind("<Return>", self.result)

    def botoes(self) -> None:
        # frame para espaço para os botões numéricos
        self.digitos = Frame(self.tela, bg=self.bg)
        self.digitos.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.76)

        # ############################ Teclado numérico ##############################################
        n1 = Button(self.digitos, text="1", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "1"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n1.place(relx=self.col1, rely=self.row3, width=self.bt_size_w, height=self.bt_size_h)

        n2 = Button(self.digitos, text="2", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "2"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n2.place(relx=self.col2, rely=self.row3, width=self.bt_size_w, height=self.bt_size_h)

        n3 = Button(self.digitos, text="3", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "3"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n3.place(relx=self.col3, rely=self.row3, width=self.bt_size_w, height=self.bt_size_h)

        n4 = Button(self.digitos, text="4", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "4"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n4.place(relx=self.col1, rely=self.row4, width=self.bt_size_w, height=self.bt_size_h)

        n5 = Button(self.digitos, text="5", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "5"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n5.place(relx=self.col2, rely=self.row4, width=self.bt_size_w, height=self.bt_size_h)

        n6 = Button(self.digitos, text="6", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "6"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n6.place(relx=self.col3, rely=self.row4, width=self.bt_size_w, height=self.bt_size_h)

        n7 = Button(self.digitos, text="7", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "7"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n7.place(relx=self.col1, rely=self.row5, width=self.bt_size_w, height=self.bt_size_h)

        n8 = Button(self.digitos, text="8", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "8"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n8.place(relx=self.col2, rely=self.row5, width=self.bt_size_w, height=self.bt_size_h)

        n9 = Button(self.digitos, text="9", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "9"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n9.place(relx=self.col3, rely=self.row5, width=self.bt_size_w, height=self.bt_size_h)

        n0 = Button(self.digitos, text="0", font=(self.bt_font, self.bt_font_size),
                    borderwidth=self.bt_border_width,
                    command=lambda: self.data_entry.insert("end", "0"), bg=self.bt_bg_color,
                    activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                    highlightbackground=self.h_bt_color)
        n0.place(relx=self.col2, rely=self.row6, width=self.bt_size_w, height=self.bt_size_h)
        ###############################################################################################

        dot = Button(self.digitos, text=".", font=(self.bt_font, self.bt_font_size), command=self.insert_dot,
                     bg=self.bt_bg_color, activebackground=self.a_bt_bg_color,
                     activeforeground=self.a_bt_fg_color, highlightbackground=self.h_bt_color)
        dot.place(relx=self.col1, rely=self.row6, width=self.bt_size_w, height=self.bt_size_h)

        but = Button(self.digitos, text="☠", font=(self.bt_font, self.bt_font_size),
                     command=lambda: print("botão sem utilidade"),
                     bg=self.bt_bg_color,
                     activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                     highlightbackground=self.h_bt_color)
        but.place(relx=self.col2, rely=self.row1, width=self.bt_size_w, height=self.bt_size_h)

        but1 = Button(self.digitos, text="☠", font=(self.bt_font, self.bt_font_size),
                      command=lambda: print("botão sem utilidade"), bg=self.bt_bg_color,
                      activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                      highlightbackground=self.h_bt_color)
        but1.place(relx=self.col3, rely=self.row1, width=self.bt_size_w, height=self.bt_size_h)

        soma = Button(self.digitos, text="+", font=(self.bt_font, self.bt_font_size), bg=self.bt_sum_bg_color,
                      activebackground=self.a_bt_sum_bg_color, activeforeground=self.a_bt_sum_fg_color,
                      command=lambda: print("Soma"))
        soma.place(relx=self.col4, rely=self.row5, width=self.bt_size_w, height=self.bt_size_h * 2.11)

        sub = Button(self.digitos, text="-", font=(self.bt_font, self.bt_font_size), bg=self.bt_bg_color,
                     activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                     highlightbackground=self.h_bt_color)
        sub.place(relx=self.col4, rely=self.row4, width=self.bt_size_w, height=self.bt_size_h)

        div = Button(self.digitos, text="÷", font=(self.bt_font, self.bt_font_size), bg=self.bt_bg_color,
                     activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                     highlightbackground=self.h_bt_color)
        div.place(relx=self.col4, rely=self.row2, width=self.bt_size_w, height=self.bt_size_h)

        mult = Button(self.digitos, text="×", font=(self.bt_font, self.bt_font_size), bg=self.bt_bg_color,
                      activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                      highlightbackground=self.h_bt_color)
        mult.place(relx=self.col4, rely=self.row3, width=self.bt_size_w, height=self.bt_size_h)

        porc = Button(self.digitos, text="﹪", font=(self.bt_font, self.bt_font_size), bg=self.bt_bg_color,
                      activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                      highlightbackground=self.h_bt_color)
        porc.place(relx=self.col3, rely=self.row2, width=self.bt_size_w, height=self.bt_size_h)

        igual = Button(self.digitos, text="=", font=(self.bt_font, self.bt_font_size), bg=self.bt_bg_color,
                       activebackground=self.a_bt_bg_color, activeforeground=self.a_bt_fg_color,
                       highlightbackground=self.h_bt_color)
        igual.place(relx=self.col3, rely=self.row6, width=self.bt_size_w, height=self.bt_size_h)

        bk = Button(self.digitos, text="«", font=(self.bt_font, self.bt_font_size), borderwidth=self.bt_border_width,
                    command=self.backspace, bg=self.bt_bg_color, activebackground=self.a_bt_bg_color,
                    activeforeground=self.a_bt_fg_color, highlightbackground=self.h_bt_color)
        bk.place(relx=self.col1, rely=self.row1, width=self.bt_size_w, height=self.bt_size_h)

        exp = Button(self.digitos, text="x²", font=(self.bt_font, self.bt_font_size),
                     borderwidth=self.bt_border_width, bg=self.bt_bg_color, activebackground=self.a_bt_bg_color,
                     activeforeground=self.a_bt_fg_color, highlightbackground=self.h_bt_color)
        exp.place(relx=self.col1, rely=self.row2, width=self.bt_size_w, height=self.bt_size_h)

        sqrt = Button(self.digitos, text="√", font=(self.bt_font, self.bt_font_size),
                      borderwidth=self.bt_border_width, bg=self.bt_bg_color, activebackground=self.a_bt_bg_color,
                      activeforeground=self.a_bt_fg_color, highlightbackground=self.h_bt_color, command=self.sqrt)
        sqrt.place(relx=self.col2, rely=self.row2, width=self.bt_size_w, height=self.bt_size_h)

        clean = Button(self.digitos, text="C", font=(self.bt_font, self.bt_font_size),
                       borderwidth=self.bt_border_width,
                       command=self.clean_all, bg=self.bt_bg_color, activebackground=self.a_bt_bg_color,
                       activeforeground=self.a_bt_fg_color, highlightbackground=self.h_bt_color)
        clean.place(relx=self.col4, rely=self.row1, width=self.bt_size_w, height=self.bt_size_h)
        ...

    def backspace(self):
        self.data_entry.delete("-end")

    def hello(self, *args):
        txt = f"\033[32m[{self.data_entry.get():>20}]\033[0m"
        print(txt)
        pass

    def get_display(self):
        return self.data_entry.get()

    def sintax_error(self):
        ...

    def insert_dot(self):
        if self.get_display() != "" and "." not in self.get_display():
            self.data_entry.insert("end", ".")

    def clean_all(self):
        self.data_entry.delete(0, "end")
        ...

    @staticmethod
    def validate(newval):
        return re.match('^[0-9ex.pi]*$', newval) is not None

    def check_void(self):
        if self.get_display() == "":
            self.data_entry.insert("end", "0")

    def result(self):
        pass

    def sum(self):
        return self.x + self.y

    def sqrt(self):
        aux = self.data_entry.get()
        a = float(aux)
        b = McCalc.sqrt(a)
        self.clean_all()
        self.data_entry.insert("end", f"{b}")
