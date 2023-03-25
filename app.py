import random

class Player:
    def __init__(self, name, hp, mp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power

    def normal_attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 일반공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def magic_attack(self, other):
        if self.mp < 5:
            print("마나가 부족합니다.")
            return
        self.mp -= 5
        damage = random.randint(self.power, self.power + 4)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, MP {self.mp}/{self.max_mp}")

class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")

print("=== 게임 시작 ===")

player_name = input("플레이어의 이름을 입력하세요: ")
player = Player(player_name, 100, 20, 10)
monster = Monster("슬라임", 50, 8)

while True:
    print("\n=== 새로운 턴 ===")
    player.show_status()
    monster.show_status()

    action = input("어떤 공격을 사용하시겠습니까? (일반, 마법) ")
    if action == "일반":
        player.normal_attack(monster)
    elif action == "마법":
        player.magic_attack(monster)
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    if monster.hp == 0:
        print("승리했습니다!")
        break

    monster.attack(player)
    if player.hp == 0:
        print("패배했습니다.")
        break

print("=== 게임 종료 ===")
