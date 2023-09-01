import json

DIR_MENU_LANG = "lang/pt_br.json"

try:
    with open(DIR_MENU_LANG, "r", encoding="utf-8") as file_menu:
        menu_options = json.load(file_menu)
        m_exit = menu_options["m_exit"]
        m_sum = menu_options["m_sum"]
        m_sub = menu_options["m_sub"]
        m_mult = menu_options["m_mult"]
        m_div = menu_options["m_div"]
        m_exp = menu_options["m_exp"]
        m_sqrt = menu_options["m_sqrt"]
        m_percent = menu_options["m_percent"]
except Exception as e:
    print(e)
    pass


class CalcPrompt:
    """
    Desktop calc
    """

    flag_state = False
    x: int | float | complex = None
    y: int | float | complex = None
    resultado = None
    MAIN_MENU = f'''
  _
 / _
| |
| |
| |__
 \____/
[0] {m_exit}  
[1] {m_sum}
[2] {m_sub}
[3] {m_mult}      
[4] {m_div}      
[5] {m_exp}      
[6] {m_sqrt}      
[7] {m_percent}
'''

    # botão igual retorna o valor entre os valores de entrada
    def ligar(self):
        self.flag_state = True
        pass

    def desligar(self):
        self.flag_state = False
        pass

    def main_menu(self):
        if self.flag_state:
            print(self.MAIN_MENU, end="")
        pass

    def sum(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def sqrt(self, x):
        return x**(1 / 2)

    def percent(self, x, y):
        return (x/100) * y


calc1 = CalcPrompt()
calc1.ligar()
calc1.main_menu()
print(calc1.div(100, 4))

