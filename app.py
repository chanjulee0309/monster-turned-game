import random


class Character:

    def __init__(self, name, hp, normal_power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.normal_power = normal_power

    def normal_attack(self, other):
        damage = random.randint(self.normal_power - 2, self.normal_power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 일반공격! {other.name}에게 {damage}의 일반데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


class Player(Character):

    def __init__(self, name, hp, mp, normal_power, magic_power):
        super().__init__(name, hp, normal_power)
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power
        self.level = 1

    def magic_attack(self, other):
        if self.mp < 5:
            print("마나가 부족합니다.")
            return
        self.mp -= 5
        damage = random.randint(self.magic_power, self.magic_power + 4)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 마법데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def player_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, MP {self.mp}/{self.max_mp}")

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.max_mp += 5
        self.mp = self.max_mp
        self.normal_power += 2
        self.magic_power += 3


class Zombie(Character):

    def __init__(self, name, hp, normal_power):
        super().__init__(name, hp, normal_power)

    def zombie_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Stage:

    def __init__(self, name, level, zombies):
        self.name = name
        self.level = level
        self.zombies = zombies


print("=== 게임 시작 ===")

player_name = input("플레이어의 이름을 입력하세요: ")
player = Player(player_name, 100, 20, 10, 15)

stages = [
    Stage("stage 1", 1, [Zombie("좀비 1", 30, 5), Zombie("좀비 2", 40, 6)]),
    Stage("stage 2", 2, [Zombie("좀비 3", 50, 7), Zombie("좀비 4", 60, 8)]),
    Stage("stage 3", 3, [Zombie("좀비 5", 70, 9), Zombie("좀비 6", 80, 10)]),
    Stage("stage 4", 4, [Zombie("좀비 7", 90, 11), Zombie("좀비 8", 100, 12)]),
    Stage("stage 5", 5, [Zombie("좀비 9", 120, 13), Zombie("좀비 10", 140, 14)]),
    Stage("stage 6", 6, [Zombie("좀비 11", 160, 15), Zombie("좀비 12", 180, 16)]),
    Stage("stage 7", 7, [Zombie("좀비 13", 200, 17), Zombie("좀비 14", 220, 18)]),
    Stage("stage 8", 8, [Zombie("좀비 15", 240, 19), Zombie("좀비 16", 260, 20)]),
    Stage("stage 9", 9, [Zombie("좀비 17", 280, 21), Zombie("좀비 18", 300, 22)]),
    Stage("stage 10", 10, [Zombie("보스좀비", 500, 50)])
]

current_stage_index = 0

while True:
    current_stage = stages[current_stage_index]
    print(f"\n=== {current_stage.name} ===")
    for zombie in current_stage.zombies:
        print(f"{zombie.name}이(가) 나타났습니다!")
        while True:
            print("\n=== 새로운 턴 ===")
            player.player_status()
            zombie.zombie_status()

            action = input("어떤 공격을 사용하시겠습니까? (1: 일반공격, 2: 마법공격) ")
            if action == "1":
                player.normal_attack(zombie)
            elif action == "2":
                player.magic_attack(zombie)
            else:
                print("잘못된 입력입니다. 다시 입력해주세요.")
                continue

            if zombie.hp == 0:
                print(f"{zombie.name}을(를) 물리쳤습니다!")
                break

            zombie.normal_attack(player)
            if player.hp == 0:
                print("게임에서 패배했습니다.")
                break

        if player.hp == 0:
            break

    if player.hp == 0:
        break

    print(f"{current_stage.name}을(를) 클리어했습니다!")
    player.level_up()
    print(f"{player.name}의 레벨이 {player.level}로 올라갔습니다.")
    print(f"{player.name}의 HP가 {player.max_hp - 10}에서 {player.max_hp}로 증가했습니다.")
    print(f"{player.name}의 MP가 {player.max_mp - 5}에서 {player.max_mp}로 증가했습니다.")
    print(f"{player.name}의 공격력이 {player.normal_power - 2}에서 {player.normal_power}로 증가했습니다.")
    print(f"{player.name}의 마법력이 {player.magic_power - 3}에서 {player.magic_power}로 증가했습니다.")

    current_stage_index += 1
    if current_stage_index == len(stages):
        print("모든 스테이지를 클리어했습니다. 게임을 종료합니다.")
        break

print("=== 게임 종료 ===")
