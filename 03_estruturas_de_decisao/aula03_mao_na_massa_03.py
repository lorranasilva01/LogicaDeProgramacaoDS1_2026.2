# TODO: Implemente o menu utilizando match-case ou elif
opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))

# Desenvolva a estrutura de seleção aqui
match opcao:
    case 1:
        print("consultar livro")
    case 2:
        print ("realizar emprestimo")
    case 3:
        print ("devolver livro")
    case _:
        print ("não encontrado")