import os
import platform

SO = platform.version()
print(SO)
__a = 1
__b = 2
__c = 3
__d = 4
__e = 5
__f = 6
LOGO = f'''\033[1m\033[31m
\033[3{__a}m000      000\033[3{__b}m       \033[3{__c}m  000000 \033[3{__d}m        \033[3{__e}m 00    \033[3{__f}m
\033[3{__a}m0000    0000\033[3{__b}m       \033[3{__c}m 000   00\033[3{__d}m        \033[3{__e}m 00    \033[3{__f}m 
\033[3{__a}m00 00  00 00\033[3{__b}m  0000 \033[3{__c}m 00      \033[3{__d}m  00000 \033[3{__e}m 00    \033[3{__f}m  0000
\033[3{__a}m00  0000  00\033[3{__b}m 00  00\033[3{__c}m 00      \033[3{__d}m      00\033[3{__e}m 00    \033[3{__f}m 00  00
\033[3{__a}m00   00   00\033[3{__b}m 00    \033[3{__c}m 00      \033[3{__d}m  000000\033[3{__e}m 00    \033[3{__f}m 00
\033[3{__a}m00        00\033[3{__b}m 00  00\033[3{__c}m 000   00\033[3{__d}m 00   00\033[3{__e}m 00    \033[3{__f}m 00  00
\033[3{__a}m00        00\033[3{__b}m  0000 \033[3{__c}m  000000 \033[3{__d}m  00000 \033[3{__e}m 000000\033[3{__f}m  0000
\033[38m*==================================================*\033[0m
'''
PI = 3.14159265358979323846264338327950288419716939937510
MAIN_MENU = '''
[+] Soma           [/] Divisão        [C] Limpar
[-] Subtração      [s] Raiz Quadrada  [**] Exponencial      
[*] Multiplicação  [%] Porcentagem    [q] Sair  
'''


def logo():
    print(LOGO, end="")


def term_clean():
    if "linux" in SO:
        os.system("clear")
    elif "win" in SO:
        os.system("cls")


def have_num(string):
    return any(char.isdigit() for char in string)


class McCalc:
    """
    calculadora
    """
    flag_state = False
    x = None
    y = None
    op = None
    result = None

    # botão igual retorna o valor entre os valores de entrada
    def run(self):
        """Inicializa o programa principal"""
        self.clean()
        self.flag_state = True
        logo()
        self.main_menu()
        pass

    def stop(self):
        """Para a execução do programa"""
        self.flag_state = False
        pass

    def _print_result(self):
        if self.check_none():
            print(f'[{self.x} {self.op} {self.y}] =\033[32m {self.result} \033[0m')

    def check_none(self):
        """Checa se foi inserido uma um valor para x, y e uma opção do do menu principal."""
        return self.x is not None and self.y is not None and self.op is not None

    def main_menu(self):
        """Mostra um menu e uma entrada de prompts"""
        while self.flag_state:
            print(MAIN_MENU)
            op_entry = (input("McCalc:> ").strip().upper())  # por que o input ta no parênteses?

            if have_num(op_entry):
                if self.x is None and self.op is None:
                    self.x = float(op_entry)
                else:
                    self.y = float(op_entry)
            else:
                op_entry = op_entry[:2]
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
                    case 'S':
                        self.op = "s"
                    case 'C':
                        self.clean()
                    case 'Q':
                        self.clean()
                        exit(code=f"\033[1m\033[34mObrigado por usar o McCalc!\033[0m")

            self.calc_result()

    def clean(self):
        """
        Limpa o terminal e reseta as variáveis par None
        """
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
                    self._print_result()
                case '-':
                    self.result = self.sub(self.x, self.y)
                    self._print_result()
                case '*':
                    self.result = self.mult(self.x, self.y)
                    self._print_result()
                case '/':
                    self.result = self.div(self.x, self.y)
                    self._print_result()
                case '**':
                    self.result = self.exp(self.x, self.y)
                    self._print_result()
                case '^':
                    self.result = self.exp(self.x, self.y)
                    self._print_result()

            self.x = self.result
            self.y = None
            self.op = None

        elif self.x is not None and self.op is not None:
            if self.op == "%":
                self.result = self.percent(self.x)
                print(f"{self.x}/100 = \033[32m {self.result} \033[0m")
                self.op = None
            elif self.op == "s":
                self.result = self.sqrt(self.x)
                print(f"sqrt({self.x}) = \033[32m {self.result} \033[0m")
                self.x = self.result
                self.op = None
            elif self.x is not None:
                print(f"= \033[32m {self.x} \033[0m")

    # ###### Métodos staticos da classe #######
    @staticmethod
    def sum(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mult(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        return x / y

    @staticmethod
    def exp(x, y):
        return x ** y

    @staticmethod
    def sqrt(x):
        return x ** (1 / 2)

    @staticmethod
    def percent(x):
        return x / 100
