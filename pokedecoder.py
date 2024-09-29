import itertools
from itertools import permutations

file1 = open('pokelist.txt', 'r')
pokemon_list = file1.readlines()
pokemon_list = [pokemon.strip().lower() for pokemon in pokemon_list]

while True:
    print("Input Scrambled Pokemon Name:")
    scrambled_input = input()

    input_permutations = [''.join(scrambled).lower() for scrambled in permutations(scrambled_input)]

    correctLenPokemon = []
    for pokemon in pokemon_list:
        if len(pokemon) == len(scrambled_input):
            correctLenPokemon.append(pokemon)
 
    found = False
    for perm in input_permutations:
        if found is True:
            break
        for poke in correctLenPokemon:
            if poke == perm:
                print("Descrambled: " + poke)
                found = True
                break
