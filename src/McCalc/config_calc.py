import json

dir_lang = "lang/pt_br.json"

menu_options = {
    "opcoes": {
        'm_exit': "Sair",
        'm_sum': "Soma",
        'm_sub': "Subtração",
        'm_mult': "Multiplicação",
        'm_div': "Divisão",
        'm_exp': "Exponencial",
        'm_sqrt': "Raiz Quadrada",
        'm_percent': "Porcentagem",
        'm_clean': "Limpar"
    },
    "inputs": {
        'm_input': "Digite uma das opções acima e tecle enter: ",
        'input_x': "Digite um numero: ",
        'input_y': "Digite um segundo valor: "
    },
    "alerts": {
        "a_quit": "Obrigado por usar o PyCalc!"
    },
    "configs": {
        "logo": True
    }
}

with open(dir_lang, "w", encoding="utf-8") as file:
    json.dump(menu_options,
              file,
              ensure_ascii=False,
              indent=4)
    file.close()
