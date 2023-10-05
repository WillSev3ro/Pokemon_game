import pickle

from pessoa import *
from pokemon import *


def escolher_pokemon_inicial(player):
    print(f'{player}, escolha seu primeiro pokemon para te acompanhar nessa jornada!')

    pikachu = PokemonEletrico('Pikachu', level=1)
    ponyta = PokemonFogo('Ponyta', level=1)
    poliwhirl = PokemonAgua('Poliwhirl', level=1)

    print('-----------------------------------------')
    print('1 -', pikachu)
    print('2 -', ponyta)
    print('3 -', poliwhirl)
    print('-----------------------------------------')

    while True:
        escolha = input('Escolha seu Pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break

        elif escolha == '2':
            player.capturar(ponyta)
            break

        elif escolha == '3':
            player.capturar(poliwhirl)
            break

        else: 
            print('Escolha invalida!')

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('Jogo salvo com sucesso!!')
    except Exception as error:
        print('Erro ao salvar jogo!')
        print(error)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player =  pickle.load(arquivo)
            print('Jogo carregado com sucesso!')
            return player
    except Exception as error:
        print('Ainda não existe jogo salvo!!')
       

if __name__ == '__main__':
    print('------------------------------------------')
    print('Bem vindo ao game Pokemon RPG de terminal!')
    print('------------------------------------------')

    player = carregar_jogo()

    if not player:

        nome = input('Olá jogador, me diga o seu nome: ')
        player = Player(nome) 

        print(f'Seja bem vindo {player}, este é um mundo habitado por pokemons, a partir de agora sua missão é tornar-se um mestre dos pokemons!')
        print('Capture o maximo de pokemons que conseguir durante sua viagem.')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Ja temos algo na sua bolsa, que bom podemos começar nossa viagem sem medo de encontrar inimigos!!')
        else:
            print('Vejo que sua bolsa está vazia, que tal começar a capturar pokemons?')
            escolher_pokemon_inicial(player)

        print('Tudo pronto, agora que você ja possui um pokemon, enfrente o seu maior inimigo, o Gary')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
        player.batalhar(gary)
        
        salvar_jogo(player)

    while True:
        print('-------------------------------------------------------')
        print('O que deseja fazer agora?')
        print('1- Explorar o mundo pokemon')
        print('2- Lutar com um inimigo')
        print('3- Ver meus Pokemons')
        print('0- Sair do jogo')
        print('-------------------------------------------------------')

        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Foi muito bom esse tempo juntos, fechando o programa agora!!')
            break
        
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)

        elif escolha =='3':
            player.mostrar_pokemons()
        
        else:
            print('Ops, essa opção não esta no menu!!')

