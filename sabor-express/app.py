# Importacao de bibliotecas 'os'
import os

# Dicionário de dados --> conceito de 'chave':valor
restaurantes = [{'nome':'Coco Bambu', 'categoria':'Frutos do Mar', 'ativo':False},
                {'nome':'Madero', 'categoria':'Prato Feito', 'ativo':True},
                {'nome':'Pizzaria X', 'categoria':'Massas', 'ativo':False}]  

def exibir_nome_do_programa():
    '''Exibe o nome do programa
    '''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
''')

def exibir_opcoes():
    '''Exibe as opcoes existentes para o usuario
    '''
    print('1. Cadastar restaurante')
    print('2. Listar restaurante(s)')
    print('3. Alternar estado do restaurante')
    print('4. Sair do aplicativo\n')

# Definindo uma função
def finalizar_app():
    '''Função que quando invocada encerra a aplicação mostrando uma mensagem
    '''
    exibir_subtitulo('Encerrando o aplicativo... ')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Exibe a mensagem de opção inválida para tratamento de exceções, e retorna ao menu prinicipal
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Exibe um texto, denominado subtitulo com argumento a ser colocado, quando invocada a função, para personalizar o (texto) da funcao exibir_subtitulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do restaurante
    - Categoria do Restaurante
    
    Output:
    - Adiciona um  novo restaurante a lista de dicionário de restaurantes
    '''

    exibir_subtitulo('Cadastro de novos restaurantes: ')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante, {nome_do_restaurante}: ')
    
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_restaurante, 'ativo':False}

    # Adicionando a lista de dicionário de dados ao array [restaurantes]
    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''''Essa função é responsável por listar todos os restaurantes

    Outputs:
    - Exibe a lista de restaurantes no terminal

    '''

    exibir_subtitulo('Listando os restaurantes... ')

    print (f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativacao_restaurante = 'Ativado.' if restaurante['ativo'] else 'Desativado.'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativacao_restaurante}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    ''''Essa função é responsável por alterar o estado do restaurante, invertendo o estado atual

    Outputs:
    - Exibe no terminal o resultado da alteração, indicando seu êxito
    ''' 

    exibir_subtitulo('Alternando o estado do restaurante!!!')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] 
            # Palavra reservada not inverte o valor da variavel
            
            mensagem = f'O restaurante, {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante, {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')

    voltar_ao_menu_principal()
     


def escolher_opcao():
    '''Funcao que aguarda input da opcao que o usuario deseja acessar

    Outputs:
    - Executa a opcao digitada pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if(opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif(opcao_escolhida == 2):
            listar_restaurantes()
        elif(opcao_escolhida == 3):
            alternar_estado_restaurante()
        elif(opcao_escolhida == 4):
            finalizar_app()
        else :
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Funcao principal do programa, onde são estruturadas as demais funcoes. Ela que inicia o programa
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

#Indicando para o Python que este arquivo.py é o principal
if __name__ == '__main__':
    main()