import random

from pokemon import *

NOMES = [
    'Alice', 'Miguel', 'Sophia', 'Arthur', 'Bernardo', 'Helena', 'Valentina'
]

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Ponyta'),
    PokemonFogo('Charizard'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonEletrico('Magnemite'),
    PokemonAgua('Slowpoke'),
    PokemonAgua('Tentacruel'),
    PokemonAgua('Poliwhirl'),
]


class Pessoa:
   
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome 
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons
 
        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}:')
            for index, pokemon in enumerate(self.pokemons):
                print(f'{index}-{pokemon}')
        else:
            print(f'{self}, sua bolsa está vazia!')
    
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f'{self} escolheu {pokemon_escolhido}!')
            return pokemon_escolhido

        else:
            print('ERRO:Jogador sem pokemons em sua bolsa!!')

    def mostrar_dinheiro(self):
        print(f'Você possui ${self.dinheiro}')

    def ganhar_dinheiro(self, quantidade):
        self.dinheiro+= quantidade
        print(f'Você ganhou ${quantidade}') 
        self.mostrar_dinheiro()


    def batalhar(self, pessoa):
        print(f'{self} iniciou uma batalha com {pessoa}')

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()

        pokemon =self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f'{self} ganhou a batalha!!')
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f'{pessoa} ganhou a batalha!!')
                    break
        
        else:
            print('Para ocorrer a batalha, deve haver lutadores dos dois lados!!')


class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}!')

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha = int(input('Escolha seu Pokemon: '))
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f'{pokemon_escolhido} eu escolho você!')
                    return pokemon_escolhido
                except:
                    print('Escolha invalida')
        else:
            print('ERRO:Jogador sem pokemons em sua bolsa!!')

    def explorar(self):
        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print(f'Um poquemon selvagem apareceu: {pokemon}')
            
            escolha = input('Deseja capturar esse pokemon? (s/n):')
            if escolha == 's':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print(f'O {pokemon} fugiu, quem sabe na próxima você consiga!!')
            
            else:
                print('Tudo bem, só não se arrependa depois!!')
        
        else:
            print('Não foi dessa vez, não desista de continuar explorando!!!')


class Inimigo(Pessoa):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None ):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1,6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome=nome, pokemons=pokemons_aleatorios)

        else:
            super().__init__(nome=nome, pokemons=pokemons)
