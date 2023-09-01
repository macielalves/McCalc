import lang
import json

dir_lang = "lang/pt_br.json"

menu_options = {
    'm_exit': "Sair",
    'm_sum': "Soma",
    'm_sub': "Subtração",
    'm_mult': "Multiplicação",
    'm_div': "Divisão",
    'm_exp': "Exponencial",
    'm_sqrt': "Raiz Quadrada",
    'm_percent': "Porcentagem"
}

with open(dir_lang, "w", encoding="utf-8") as file:
    json.dump(menu_options,
              file,
              ensure_ascii=False,
              indent=4
              )
    file.close()
