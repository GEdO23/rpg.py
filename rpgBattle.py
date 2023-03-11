# Importar modulo random para turnos mais realistas e desafiadores
from random import randint
from time import sleep

# Criação das informações dos "Objetos", ou seja, Jogadores e Inimigos
# Abaixo define o objeto padrão como o Jogador

obj = 'Player'

# Logo após são as informações basicas de um jogador, como por exemplo:
# Vida: A quantidade de vida que um jogador
# Ataque: Quanto de dano um jogador pode dar em um inimigo
# Level: O level em que o jogador está
# Experiencia: A quantidade de experiencia que um jogador tem 

object_inf = [f'{obj} Health Points :',
              f'{obj} Attack : ',
              f'{obj} Level :',
              f'{obj} Experience :']

# Definindo status e hp do jogador como global. Porque? Porque sim, tenha fé que funciona!

global stats

# Definindo os status padrões do jogador em seu nivel 1

player_stats = {
    'p_hp':100, 
    'p_atk':5,
    'lvl':1, 
    'exp':0
    }


# Sistema de level e experiencia, onde a cada mil experiencia que voce obtem, voce aumenta de nivel por um.

def levelup():
    if player_stats['exp']>= (1000 * (player_stats['exp'] / 1000)):
        player_stats['lvl'] += int(player_stats['exp'] / 1000)

# Sistema de identificação do tipo de Inimigo
# Dependendo do inimigo, o sistema da diferentes tipos de vida, ataque e experiencia que serão dadas ao jogador

class Enemy:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type
        if enemy_type == 'Green Slime':
            self.elemental_type = 'NATURE'
            self.obj = enemy_type
            self.base_e_hp =  9
            self.e_atk = 8
            self.given_experience = 160
        elif enemy_type == 'Red Slime':
            self.elemental_type = 'FIRE'
            self.obj = enemy_type
            self.base_e_hp =  20
            self.e_atk = 10
            self.given_experience = 300

        self.e_hp =  self.base_e_hp
        self.enemy_stats = [self.enemy_type,
                            self.elemental_type,
                            self.e_hp,
                            self.e_atk,
                            self.given_experience
                            ]
        self.object_inf = [ f'{self.obj} TYPE OF ENEMY: ',
                            f'{self.obj} ELEMENTAL TYPE:  ',
                            f'{self.obj} Health Points :',
                            f'{self.obj} Attack :',
                            f'{self.obj} Given Experience :']


# Declaração do tipo de inimigo
enemy = Enemy('Red Slime')

# ELEMENTAL ATTACK SYSTEM
# TYPE OF ATTACK can be FIRE, NATURE or WATER
# FIRE > NATURE > WATER
# NATURE > WATER > FIRE
# WATER > FIRE > NATURE

def elemental_system():
    type_of_attack = int(input('\n\n[0] NORMAL\n[1] NATURE\n[2] WATER\n[3] FIRE\nChoose attack : '))
    # NATURE ATTACK 
    if type_of_attack == 1:

        if enemy.elemental_type == 'WATER':
            player_stats['p_atk'] *= 2

        elif enemy.elemental_type == 'FIRE':
            player_stats['p_atk'] *= 0.5

    # WATER ATTACK
    elif type_of_attack == 2:

        if enemy.elemental_type == 'NATURE':
            player_stats['p_atk'] *= 0.5

        elif enemy.elemental_type == 'FIRE':
            player_stats['p_atk'] *= 2

    # FIRE ATTACK
    elif type_of_attack == 3:

        if enemy.elemental_type == 'NATURE':
            player_stats['p_atk'] *= 2

        elif enemy.elemental_type == 'WATER':
            player_stats['p_atk'] *= 0.5
            

# Turno do jogador, com a chance de acerto de um ataque e sua consequencia

def player_turn():
    # CHANCE DE ACERTO
    # Caso 0, o jogador erra o ataque
    # Caso 1, o jogador acerta o ataque

    elemental_system()
    hit_chance = randint(0, 1)
    if hit_chance == 1:
        enemy.e_hp -= player_stats['p_atk']
        print(f'\nPlayer attacked {enemy.enemy_type}! ooooo')
        
    elif hit_chance == 0:
        print('\nPlayer missed! xxxxx')

    print(object_inf[0], player_stats['p_hp'], 'hp')    
    print(enemy.object_inf[2], enemy.e_hp, 'hp')

# Turno de um inimigo, com a chance de acerto de um ataque e sua consequencia

def enemy_turn():
    # CHANCE DE ACERTO
    # Caso 0, o inimigo erra o ataque
    # Caso 1, o inimigo acerta o ataque

    hit_chance = randint(0, 1)
    if hit_chance == 1:
        player_stats['p_hp'] -= enemy.e_atk
        print(f'\n{enemy.enemy_type} attacked Player! ooooo')
    
    elif hit_chance == 0:
        print(f'\n{enemy.enemy_type} missed! xxxxx')
    
    print(object_inf[0], player_stats['p_hp'], 'hp')    
    print(enemy.object_inf[2], enemy.e_hp, 'hp')


def restart_hp():
    enemy.e_hp = enemy.base_e_hp


# Sistema de loop, onde os turnos irão se repetir até o jogador ou inimigo terem seu hp como zero, ou seja, até eles perderem a vida
def rpg_battle():
    while enemy.e_hp > 0 or player_stats['p_hp'] > 0:
        if player_stats['p_hp'] <= 0:
            print('\nGAME OVER\n')
            break
        player_turn()
        if enemy.e_hp <= 0:
            print('\nYOU WIN\n')
            player_stats['exp'] += enemy.given_experience
            levelup()
            break
        enemy_turn()
    restart_hp()

rpg_battle()
