# Player Information
import random

obj = 'Player'
object_inf = [f'{obj} Health Points :',
              f'{obj} Attack : ',
              f'{obj} Level :',
              f'{obj} Experience :']

global stats
global p_hp
# Player Stats

p_atk = 5

lvl = 1
exp = 2000
if exp >= (1000 * (exp / 1000)):
    lvl += int(exp / 1000)

player_stats = [p_hp,
                p_atk,
                lvl,
                exp]


# Enemy sort system


class Enemy:
    def __init__(self, enemy_type):
        self.enemy_type = enemy_type
        if enemy_type == 'Bat':
            self.obj = enemy_type
            self.e_hp = 20
            self.e_atk = 5
            self.given_experience = 15

        self.enemy_stats = [self.e_hp,
                            self.e_atk,
                            self.given_experience
                            ]
        self.object_inf = [f'{self.obj} Health Points :',
                           f'{self.obj} Attack :',
                           f'{self.obj} Given Experience :']


# Preciso tirar da vida do inimigo, a quantidade de dano que o jogador dá;
# e_hp -= p_atk


enemy = Enemy('Bat')


def player_turn():
    hit_chance = random.randint(0, 1)
    if hit_chance == 1:
        print(f'\nPlayer attacked {enemy.enemy_type}! ooooo')
        enemy.e_hp -= p_atk
    elif hit_chance == 0:
        print('\nPlayer missed! xxxxx')
    print(enemy.object_inf[0], enemy.e_hp, 'hp')


def enemy_turn():
    global p_hp
    hit_chance = random.randint(0, 1)
    if hit_chance == 1:
        print(f'\n{enemy.enemy_type} attacked Player! ooooo')
        p_hp -= enemy.e_atk
    elif hit_chance == 0:
        print(f'\n{enemy.enemy_type} missed! xxxxx')
    print(object_inf[0], player_stats[0], 'hp')


while enemy.e_hp > 0:
    player_turn()
    enemy_turn()
