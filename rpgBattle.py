# Importar modulo random para turnos mais realistas e desafiadores
import random
import time

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
    'p_atk':5
    }

lvl = 1 
exp = 2000

# Sistema de level e experiencia, onde a cada mil experiencia que voce obtem, voce aumenta de nivel por um.

if exp >= (1000 * (exp / 1000)):
    lvl += int(exp / 1000)

# Sistema de identificação do tipo de Inimigo
# Dependendo do inimigo, o sistema da diferentes tipos de vida, ataque e experiencia que serão dadas ao jogador

class Enemy:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type
        if enemy_type == 'Bat':
            self.obj = enemy_type
            self.e_hp = 100
            self.e_atk = 20
            self.given_experience = 15

        self.enemy_stats = [self.e_hp,
                            self.e_atk,
                            self.given_experience
                            ]
        self.object_inf = [f'{self.obj} Health Points :',
                           f'{self.obj} Attack :',
                           f'{self.obj} Given Experience :']


# Declaração do tipo de inimigo
enemy = Enemy('Bat')


# Turno do jogador, com a chance de acerto de um ataque e sua consequencia

def player_turn():
    hit_chance = random.randint(0, 1)
    if hit_chance == 1:
        enemy.e_hp -= player_stats['p_atk']
        print(f'\nPlayer attacked {enemy.enemy_type}! ooooo')
    
    elif hit_chance == 0:
        print('\nPlayer missed! xxxxx')
    
    print(enemy.object_inf[0], enemy.e_hp, 'hp')

# Turno de um inimigo, com a chance de acerto de um ataque e sua consequencia (WIP)

def enemy_turn():
    hit_chance = random.randint(0, 1)
    if hit_chance == 1:
        player_stats['p_hp'] -= enemy.e_atk
        print(f'\n{enemy.enemy_type} attacked Player! ooooo')
    
    elif hit_chance == 0:
        print(f'\n{enemy.enemy_type} missed! xxxxx')
    
    print(object_inf[0], player_stats['p_hp'], 'hp')

# Sistema de loop, onde os turnos irão se repetir até o jogador ou inimigo terem seu hp como zero, ou seja, até eles perderem a vida
while enemy.e_hp > 0 or player_stats['p_hp'] > 0:
    if player_stats['p_hp'] <= 0:
        print('\nGAME OVER\n')
        break
    player_turn()
    if enemy.e_hp <= 0:
        print('\nYOU WIN\n')
        break
    enemy_turn()
         