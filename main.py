while True:
    comando = input("Digite um comando [ABOUT/QUIT/ADD]: ").upper()
    match comando:
        case "ABOUT":
            print("Seja bem vindo ao Gestor de Portfólio do Caíque.")
        case "QUIT":
            print("Saindo do Gestor de Portfólio.")
            break
        case "ADD":
            while True:
                quantidade_projeto = int(input("Informe quantos projetos deseja adicionar: "))
                if quantidade_projeto <= 0:
                    print("A quantidade de projetos não pode ser menor ou igual a zero!")
                else:
                    for i in range(quantidade_projeto):
                        nome_projeto = input("Digite o nome do projeto: ")
                        print(f"SUCESSO: Projeto '{nome_projeto}' adicionado.")
                    break
        case _:
            print("ERRO: Comando não reconhecido.")

print("Até logo!!!")
