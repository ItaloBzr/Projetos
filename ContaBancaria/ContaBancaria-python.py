import os
import time

lista = {}
nomes = []
senhas = []

nomes = ['joao', 'maria']
senhas = [111, 222]
lista = {}

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_senha(senha):
    if not senha.isdigit():
        print("Senha deve ser um número.")
        input("Pressione Enter para continuar...".upper())
        return False
    return True

def adicionar_pessoas():
    while True:
        cls()
        print('Adicionar nova pessoa')
        identificador = input("Identificador = ").lower()
        if identificador not in nomes:
            senha = input('Senha (apenas números): ')
            if not validar_senha(senha):
                continue
            senha = int(senha)
            if senha not in senhas:
                nome = input('Nome: ')
                idade = input('Idade: ')
                dinheiro = input('Dinheiro: ')
                if not idade.isdigit() or not dinheiro.isdigit():
                    print("Idade e dinheiro devem ser números.")
                    input("Pressione Enter para continuar...".upper())
                    continue
                idade = int(idade)
                dinheiro = int(dinheiro)
                nomes.append(identificador)
                senhas.append(senha)
                pessoa = {
                    'IDENTIFICADOR': identificador,
                    'SENHA': senha,
                    'NOME': nome,
                    'IDADE': idade,
                    'DINHEIRO': dinheiro,
                }
                lista[identificador] = pessoa
                print("Pessoa adicionada com sucesso!")
                input("Pressione Enter para continuar...".upper())
                break
            else:
                print("ESSA SENHA JÁ EXISTE!")
                input("Pressione Enter para continuar...".upper())
        else:
            print("ESSE IDENTIFICADOR JÁ EXISTE!")
            input("Pressione Enter para continuar...".upper())

def chamar_nomes():
    cls()
    print(20 * "-", "USUÁRIOS", 20 * "-")
    print("1. Visualizar todos")
    print("2. Buscar por identificador")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        cls()
        for identificador, dados in lista.items():
            for chave, valor in dados.items():
                if chave == "SENHA":
                    print(f"  {chave}: ***")
                else:
                    print(f"  {chave}: {valor}")    
            print("-" * 40)
            time.sleep(0.1)
        input("\nPressione Enter para continuar...".upper())
    elif escolha == '2':
        chamar = input('\nDigite o identificador para obter informações: ').lower()
        if chamar in lista:
            cls()
            for chave, valor in lista[chamar].items():
                if chave == "SENHA":
                    print(f"{chave}: ***")
                else:
                    print(f'{chave}: {valor}')
                    time.sleep(0.1)
        else:
            print("Identificador não encontrado.")
        input("Pressione Enter para continuar...".upper())
    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar...".upper())

def depositar_dinheiro(identificador):
    cls()
    posicao = nomes.index(identificador)
    senha = input("Digite sua senha: ")
    if not validar_senha(senha):
        return
    senha = int(senha)
    if senha != senhas[posicao]:
        print("Senha incorreta.")
        input("Pressione Enter para continuar...".upper())
    else:
        atual_money = lista[identificador]['DINHEIRO']
        quero_money = input(f"Digite o valor para depositar, você atualmente tem {atual_money} R$ = ")
        if not quero_money.isdigit():
            print("Valor inválido.")
            input("Pressione Enter para continuar...".upper())
        else:
            quero_money = int(quero_money)
            lista[identificador]['DINHEIRO'] += quero_money
            print("DEPÓSITO EFETUADO!")
            input("Pressione Enter para continuar...".upper())

def sacar_dinheiro(identificador):
    cls()
    posicao = nomes.index(identificador)
    senha = input("Digite sua senha: ")
    if not validar_senha(senha):
        return
    senha = int(senha)
    if senha != senhas[posicao]:
        print("Senha incorreta.")
        input("Pressione Enter para continuar...".upper())
    else:
        atual_money = lista[identificador]['DINHEIRO']
        quero_money = input(f"Digite o valor para sacar, lembre-se que você tem {atual_money} R$ = ")
        if not quero_money.isdigit():
            print("Valor inválido.")
            input("Pressione Enter para continuar...".upper())
        else:
            quero_money = int(quero_money)
            if quero_money > atual_money:
                print("Dinheiro solicitado é maior do que o possuído.")
            else:
                lista[identificador]['DINHEIRO'] -= quero_money
                print("SAQUE EFETUADO!")
            input("Pressione Enter para continuar...".upper())

def enviar_dinheiro(identificador):
    cls()
    posicao = nomes.index(identificador)
    senha = input("Digite sua senha: ")
    if not validar_senha(senha):
        return
    senha = int(senha)
    if senha != senhas[posicao]:
        print("Senha incorreta.")
        input("Pressione Enter para continuar...".upper())
    else:
        pessoa = input("Digite o identificador da pessoa desejada: ").lower()
        if pessoa not in nomes or pessoa == identificador:
            print("Identificador não existe ou é o seu próprio.")
        else:
            print(f'Nome = {lista[pessoa]["NOME"]}')
            escolha = input('Essa é a pessoa desejada (S/N)? ').lower()
            if escolha == 's':
                valor = input(f"Digite o valor para enviar, lembre-se que você possui {lista[identificador]['DINHEIRO']}: ")
                if not valor.isdigit():
                    print("Valor inválido.")
                    input("Pressione Enter para continuar...".upper())
                else:
                    valor = int(valor)
                    if valor > lista[identificador]['DINHEIRO']:
                        print("O valor que você quer enviar não é viável.")
                    else:
                        lista[pessoa]["DINHEIRO"] += valor
                        lista[identificador]['DINHEIRO'] -= valor
                        print("Dinheiro enviado com sucesso!")
        input("Pressione Enter para continuar...".upper())

def alterar_senha(identificador):
    cls()
    posicao = nomes.index(identificador)
    senha_atual = input("Digite sua senha atual: ")
    if not validar_senha(senha_atual):
        return
    senha_atual = int(senha_atual)
    if senha_atual != senhas[posicao]:
        print("Senha incorreta.")
        input("Pressione Enter para continuar...".upper())
    else:
        senha = input("Digite sua nova senha: ")
        confirm_senha = input("Confirme sua nova senha: ")
        if not validar_senha(senha) or not validar_senha(confirm_senha):
            return
        senha = int(senha)
        confirm_senha = int(confirm_senha)
        if senha == confirm_senha:
            lista[identificador]["SENHA"] = confirm_senha
            senhas[posicao] = confirm_senha
            print("SENHA ALTERADA COM SUCESSO!")
        else:
            print("As senhas não conferem, tente novamente.")
        input("Pressione Enter para continuar...".upper())

def excluir_conta(identificador):
    cls()
    posicao = nomes.index(identificador)
    senha = input("Digite sua senha: ")
    if not validar_senha(senha):
        return
    senha = int(senha)
    if senha != senhas[posicao]:
        print("Senha incorreta.")
        input("Pressione Enter para continuar...".upper())
    else:
        print("Excluindo conta...")
        del lista[identificador]
        nomes.pop(posicao)
        senhas.pop(posicao)
        print("Conta excluída com sucesso!")
        input("Pressione Enter para continuar...".upper())

def menu_admin():
    while True:
        cls()
        print("--- MENU ADMIN ---")
        print("1. Listar usuários")
        print("2. Sair")
        escolha = input("Digite o número da opção desejada: ")
        if escolha == '1':
            if not nomes:
                print('NÃO TEM PESSOAS NA LISTA')
                input("Pressione Enter para continuar...".upper())
            else:
                chamar_nomes()
        elif escolha == '2':
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...".upper())

def menu_usuario(identificador):
    while True:
        cls()
        print("1. Alterar senha")
        print("2. Depositar dinheiro")
        print("3. Sacar dinheiro")
        print("4. Enviar dinheiro")
        print("5. Excluir conta")
        print("6. Sair")
        escolha = input("Digite o número da opção desejada: ")
        if escolha == '1':
            alterar_senha(identificador)
        elif escolha == '2':
            depositar_dinheiro(identificador)
        elif escolha == '3':
            sacar_dinheiro(identificador)
        elif escolha == '4':
            enviar_dinheiro(identificador)
        elif escolha == '5':
            excluir_conta(identificador)
        elif escolha == '6':
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...".upper())

def login():
    cls()
    print("=== LOGIN ===")
    identificador = input("Identificador: ").lower()
    senha = input("Senha: ")
    if not validar_senha(senha):
        return
    senha = int(senha)
    if identificador == "admin" and senha == 1234:
        return "admin"
    elif identificador in nomes:
        posicao = nomes.index(identificador)
        if senha == senhas[posicao]:
            return "usuario", identificador
        else:
            print("Senha inválida.")
            input("Pressione Enter para continuar...".upper())
    else:
        print("Identificador não encontrado.")
        input("Pressione Enter para continuar...".upper())

def main():
    while True:
        cls()
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        escolha = input("Digite o número da opção desejada: ")
        if escolha == '1':
            adicionar_pessoas()
        elif escolha == '2':
            cls()
            print("=== LOGIN ===")
            identificador = input("Identificador: ").lower()
            senha = input("Senha: ")
            if not validar_senha(senha):
                continue
            senha = int(senha)
            if identificador == "admin" and senha == 1234:
                menu_admin()
            elif identificador in nomes:
                posicao = nomes.index(identificador)
                if senha == senhas[posicao]:
                    menu_usuario(identificador)
                else:
                    print("Senha inválida.")
                    input("Pressione Enter para continuar...".upper())
            else:
                print("Identificador não encontrado.")
                input("Pressione Enter para continuar...".upper())
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...".upper())

main()