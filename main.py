comando = input("Digite um comando [ABOUT/QUIT]: ").upper()

match comando:
    case "ABOUT":
        print("Seja bem vindo ao Gestor de Portfólio do Caíque.")
    case "QUIT":
        print("Saindo do Gestor de Portfólio.")
    case _:
        print("ERRO: Comando não reconhecido.")
print("Até logo!!!")



