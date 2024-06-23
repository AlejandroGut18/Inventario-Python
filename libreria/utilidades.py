import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
  
def input_validado_numero(message = "", menu = None, is_negative = False, min = None, max = None, options = None):
    entrada = None
    while entrada == None:
        clear()
        if menu:
            print(menu)
        entrada = input(message)
        if not entrada.isdigit():
            print("Ingrese un número válido")
            entrada = None
            input("Presione enter para continuar...")
            continue
        entrada = int(entrada)
        if options and entrada not in options:
            print("Escoja una opción válida")
            entrada = None
            input("Presione enter para continuar...")
            continue
        else:
            break
       
    return entrada