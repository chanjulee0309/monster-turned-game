import random

class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """
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

class Player(Character):
    def __init__(self, name, hp, mp, power, magic_power):
        super().__init__(name, hp, power)
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power
        self.level = 1

    def normal_attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 일반공격! {other.name}에게 {damage}의 일반데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

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

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}, MP {self.mp}/{self.max_mp}")

    def turn_end(self):
        self.mp = min(self.mp + 2, self.max_mp)

    def level_up(self):
        self.level += 1
        self.max_hp += 10
        self.hp = self.max_hp
        self.max_mp += 5
        self.mp = self.max_mp
        self.power += 2
        self.magic_power += 3

class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 일반공격! {other.name}에게 {damage}의 일반데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")

monster_list = [
    Monster("슬라임", 50, 8),
    Monster("주황버섯", 50, 8),
    Monster("리본돼지", 50, 8),
    Monster("골렘", 100, 15),
    Monster("드래곤", 150, 20),
    Monster("오크", 80, 12),
    Monster("뱀파이어", 120, 18),
]

print("=== 게임 시작 ===")

player_name = input("플레이어의 이름을 입력하세요: ")
player = Player(player_name, 100, 20, 10, 15)
monster = random.choice(monster_list)

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

    player.turn_end()

    current_level = player.level
    current_hp = player.hp
    current_mp = player.mp
    current_power = player.power
    current_magic_power = player.magic_power
    if monster.hp == 0:
        print("승리했습니다!")
        player.level_up()
        print(f"{player.name}의 레벨이 {player.level}로 올라갔습니다.")
        print(f"{player.name}의 HP가 {player.max_hp - 10}에서 {player.max_hp}로 증가했습니다.")
        print(f"{player.name}의 MP가 {player.max_mp - 5}에서 {player.max_mp}로 증가했습니다.")
        print(f"{player.name}의 공격력이 {player.power - 2}에서 {player.power}로 증가했습니다.")
        print(f"{player.name}의 마법력이 {player.magic_power - 3}에서 {player.magic_power}로 증가했습니다.")
        monster_list.remove(monster)  # 몬스터 리스트에서 삭제
        if not monster_list:
            print("모든 몬스터를 물리쳤습니다. 게임을 종료합니다.")
            break
        monster = random.choice(monster_list)
        continue

    monster.attack(player)
    if player.hp == 0:
        print("게임에서 패배했습니다.")
        break

    # 레벨이 올라 갔을 때의 상태를 출력
    if player.level > current_level:
        print(f"{player.name}의 레벨이 {player.level}로 올라갔습니다.")
        print(f"{player.name}의 HP가 {current_hp}에서 {player.hp}로 증가했습니다.")
        print(f"{player.name}의 MP가 {current_mp}에서 {player.mp}로 증가했습니다.")
        print(f"{player.name}의 공격력이 {current_power}에서 {player.power}로 증가했습니다.")
        print(f"{player.name}의 마법력이 {current_magic_power}에서 {player.magic_power}로 증가했습니다.")
        current_level = player.level
        current_hp = player.hp
        current_mp = player.mp
        current_power = player.power
        current_magic_power = player.magic_power

print("=== 게임 종료 ===")
