from Inimigo import Inimigo
from Player import Player
from Inimigo import Inimigo
from random import randint
from colorama import Fore, Back, Style, just_fix_windows_console
just_fix_windows_console()

def linha():
    print("-"*50)

print(f'{Back.BLACK}{Fore.GREEN}{Style.BRIGHT}', end='')
# --Pegando as informaçõe do Player--
# Nome do Player
while True:
    try:
        nome = str(input('Nome do Player: '))
        break
    except ValueError:
        print('Informe um valor válido!')

# Vida do Player
while True:
    try:
        vida = int(input('Vida do Player: '))
        break
    except ValueError:
        print('Informe um valor válido!')

# Dano do Player
while True:
    try:
        dano = int(input('Dano do Player: '))
        break
    except ValueError:
        print('Informe um valor válido!')

# Construindo o Objeto Player
player = Player(nome, vida, dano)

ci = 0

# Enquanto o Player viver
while player.get_vivo():
    # Crio inimigo
    print(f'{Fore.RED}', end='')
    linha()
    print(f"Novo Inimigo surgiu!\nInimigos Derrotados: {ci}")
    vidainimigo = randint(100, 200)
    danoinimigo = randint(10, 30)
    inimigo = Inimigo('Zumbi', vidainimigo, danoinimigo)

    # Enquanto o player e o inimigo viver
    while player.get_vivo() and inimigo.get_vivo():
        # Opções do Player
        print(f'{Fore.MAGENTA}', end='')
        linha()
        opcoes = ["ATACAR"]
        for opcao in opcoes:
            print(f"[{opcoes.index(opcao)}] {opcao}")
        playerinput = int(input("Opção: "))
        print(f'{Fore.BLUE}', end='')
        linha()

        if playerinput == 0:
            print("ATAQUE DO PLAYER")
            inimigo.set_vida(inimigo.get_vida()-player.get_dano())
            print(f'Ataque realizado com sucesso!\nDano causado: {player.get_dano()}\nVida do inimigo: {inimigo.get_vida_max()}/{inimigo.get_vida()}')

        if inimigo.get_vivo():
             # Ataque do inimigo
            print(f'{Fore.RED}', end='')
            linha()
            print("ATAQUE DO INIMIGO")
            player.set_vida(player.get_vida()-inimigo.get_dano())
            print(f'Ataque recebido!\nDano tomado: {inimigo.get_dano()}\nVida: {player.get_vida_max()}/{player.get_vida()}')
        else:
            ci += 1

print(f'{Fore.RED}{Back.WHITE}')
print("VOCÊ MORREU!")
print(f'{Style.RESET_ALL}')
