import time

#Isso serve para mostrar olá mundo

# o código abaixo mostra uma saudação


tempo = 2

def saudacao():
    print("Seja bem vindo")

    nome = input("Qual seu nome?")

    print("bem vindo",nome)
    time.sleep(tempo)

def menu():
    print("Como posso ajudar?")
    time.sleep(tempo)
    print("1-impala")
    print("2-risqué")
    print("3-colorama")

    opcao = int(input("escolha a opção desejada"))

    if opcao == 1:
        print("impala:praíso, serena, gatinha")
    elif opcao == 2:
        print("risqué:lágrimas de vênus, rebu, carmin")
    elif opcao == 3:
        print("colorama: 40 graus, branco lunar, nude")

    else:
        print("não há está opção")

saudacao()
menu()
