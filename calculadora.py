import json
import os
import sysconfig
import platform

DIR_MENU_LANG = "lang/pt_br.json"

SO = sysconfig.get_platform()

try:
    with open(DIR_MENU_LANG, "r", encoding="utf-8") as file_menu:
        configs = json.load(file_menu)
        # menu option
        m_exit = configs["opcoes"]["m_exit"]
        m_sum = configs["opcoes"]["m_sum"]
        m_sub = configs["opcoes"]["m_sub"]
        m_mult = configs["opcoes"]["m_mult"]
        m_div = configs["opcoes"]["m_div"]
        m_exp = configs["opcoes"]["m_exp"]
        m_sqrt = configs["opcoes"]["m_sqrt"]
        m_percent = configs["opcoes"]["m_percent"]
        m_clean = configs["opcoes"]["m_clean"]
        # label inputs
        m_input = configs["inputs"]["m_input"]
        in_x = configs["inputs"]["input_x"]
        in_y = configs["inputs"]["input_y"]
        # alerts
        alert_on_quit = configs["alerts"]["a_quit"]
        # configs
        c_logo = configs["configs"]["logo"]
except Exception as e:
    print(e)
    pass


LOGO = '''\033[1m\033[31m _ ___   __    __   ___     ____    _        ____
|   _ `\ \ \  / / / __ `\  / __ \  | |      / __ `\ 
|  |_| |  \ \/ / | /  |_| | |  | | | |     | /  |_|
|  ___,/   \  /  | |   _  | |__| | | |     | |   _
| |        / /   | \__| | |  __  | | |____ | \__| |
|_|       /_/     \____/  |_|  |_| |______| \____/
\033[0m
'''

MAIN_MENU = f'''
[+] {m_sum}\t[/] {m_div}\t[C] {m_clean}
[-] {m_sub}\t[r] {m_sqrt}\t[**] {m_exp}      
[*] {m_mult}\t[%] {m_percent}\t[q] {m_exit}  
'''

PI = 3.14159265358979323846264338327950288419716939937510


def logo():
    if c_logo:
        print(LOGO, end="")


def term_clean():
    if "linux" in SO:
        os.system("clear")
    elif "win" in SO:
        os.system("cls")


def have_num(string):
    return any(char.isdigit() for char in string)


class PyCalc:
    """
    calculadora
    """
    flag_state = False
    x = None
    y = None
    op = None
    result = None

    # botão igual retorna o valor entre os valores de entrada
    def on(self):
        self.clean()
        self.flag_state = True
        print("\033[1m\033[35m" + platform.system() + " " + platform.release(), platform.version(), platform.architecture(),
              platform.processor(), sep=" | ", end="\033[0m\n")
        logo()
        self.main_menu()
        pass

    def off(self):
        self.flag_state = False
        pass

    def _print_result(self):
        if self.check_none():
            print(f'{self.x} {self.op} {self.y} = {self.result}')
        elif self.op == "%":
            print(f"{self.x}/100 = {self.result}")

    def check_none(self):
        return self.x is not None and self.y is not None and self.op is not None

    def main_menu(self):
        while self.flag_state:
            print(MAIN_MENU)
            print(self._print_result())
            op_entry = (input("PyCalc:> ").strip().upper())  # por que o input ta no parênteses?

            if have_num(op_entry):
                if self.x is None and self.op is None:
                    self.x = float(op_entry)
                else:
                    self.y = float(op_entry)
            else:
                match op_entry:
                    case '+':
                        self.op = "+"
                    case '-':
                        self.op = "-"
                    case '*':
                        self.op = "*"
                    case '/':
                        self.op = "/"
                    case '**':
                        self.op = "**"
                    case '^':
                        self.op = "**"
                    case '%':
                        self.op = "%"
                    case 'R':
                        self.op = "r"
                    case 'C':
                        self.clean()
                    case 'Q':
                        self.clean()
                        exit(code=f"\033[1m\033[34m{alert_on_quit}\033[0m")

            self.calc_result()

    def clean(self):
        self.result = None
        self.op = None
        self.x = None
        self.y = None
        term_clean()

    def calc_result(self):
        term_clean()
        logo()
        if self.check_none():
            match self.op:
                case '+':
                    self.result = self.sum(self.x, self.y)
                    #self._print_result()
                case '-':
                    self.result = self.sub(self.x, self.y)
                    #self._print_result()
                case '*':
                    self.result = self.mult(self.x, self.y)
                    #self._print_result()
                case '/':
                    self.result = self.div(self.x, self.y)
                    #self._print_result()
                case '**':
                    self.result = self.exp(self.x, self.y)
                    #self._print_result()
                case '^':
                    self.result = self.exp(self.x, self.y)
                    #self._print_result()
                case '%':
                    self.result = self.percent(self.x)
                    #self._print_result()
                case 'R':
                    self.result = self.sqrt(self.x)
                    #self._print_result()

            self.x = self.result
            self.y = None
            self.op = None

    # ###### Métodos operacionais #######
    def sum(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def exp(self, x, y):
        return x ** y

    def sqrt(self, x):
        return x ** (1 / 2)

    def percent(self, x):
        return x / 100


calc1 = PyCalc()
calc1.on()
