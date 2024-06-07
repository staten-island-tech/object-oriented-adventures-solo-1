import math, time, random, sys
from ship import *
from weapons import *
from locations import *
from functions import *
from entities import *
from data import *

class player(entity):
  def __init__(self, name, location, ship, currency, rewardmin = 0, rewardmax = 0):
    super().__init__(name, location, ship, rewardmin, rewardmax)
    self.currency = currency
  def fight(self, enemy):
    global currency
    move = 0
    while self.ship.integrity > 0 and enemy.ship.integrity > 0:
      clear()
      print("Player Stats:")
      print(f"Ship: {self.ship.name} | Health: {self.ship.integrity}/{self.ship.maxintegrity} | Shield: {self.ship.shieldintegrity}/{self.ship.maxshieldintegrity} | Fuel: {self.ship.fuel}/{self.ship.maxfuel}")
      print(f"Weapon: {self.ship.weapon.name} | Damage: {self.ship.weapon.damage}")
      print("\nEnemy Stats:")
      print(f"Ship: {enemy.ship.name} | Health: {enemy.ship.integrity}/{enemy.ship.maxintegrity} | Shield: {enemy.ship.shieldintegrity}/{enemy.ship.maxshieldintegrity}")
      print(f"Weapon: {enemy.ship.weapon.name} | Damage: {enemy.ship.weapon.damage}")
      if move == 0:
        choice = input("What do you want to do?\n   (1) Attack\n   (2) Repair\n   (3) Escape\n").lower()
        if choice == "1" or choice == "attack":
          if enemy.ship.shieldintegrity < self.ship.weapon.damage:
            if enemy.ship.shieldintegrity == 0:
              print(f"You attacked {enemy.name} with your {self.ship.weapon.name} and did {self.ship.weapon.damage} damage!")
            else:
              print(f"You attacked {enemy.name} with your {self.ship.weapon.name} and did {self.ship.weapon.damage - enemy.ship.shieldintegrity} damage! You also broke their shield!")
            enemy.ship.integrity -= self.ship.weapon.damage - enemy.ship.shieldintegrity
            enemy.ship.shieldintegrity = 0
            move = 1
          else:
            print("You damaged their shield!")
            enemy.ship.shieldintegrity -= self.ship.weapon.damage
        elif choice == "2" or choice == "repair":
          self.ship.repair(True, True)
          move = 1
        elif choice == "3" or choice == "escape":
          print(f"You escaped from {enemy.name}!")
          break
        else:
          print("Invalid input!")
          time.sleep(1)
          continue
      elif move == 1:
        if self.ship.shieldintegrity + self.ship.integrity <= enemy.ship.weapon.damage:
          if self.ship.shieldintegrity < enemy.ship.weapon.damage:
            if self.ship.shieldintegrity == 0:
              print(f"{enemy.name} attacked you with their {enemy.ship.weapon.name} and did {enemy.ship.weapon.damage} damage!")
            else:
              print(f"{enemy.name} attacked you with their {enemy.ship.weapon.name} and did {enemy.ship.weapon.damage - self.ship.shieldintegrity} damage! You also broke their shield!")
            self.ship.integrity -= enemy.ship.weapon.damage - self.ship.shieldintegrity
            self.ship.shieldintegrity = 0
          else:
            print(f"{enemy.name} damaged your shield!")
            self.ship.shieldintegrity -= enemy.ship.weapon.damage
        elif enemy.ship.integrity + enemy.ship.shieldintegrity <= self.ship.weapon.damage:
          enemy.ship.repair(False, True)
        else:
          if self.ship.shieldintegrity < enemy.ship.weapon.damage:
            if self.ship.shieldintegrity == 0:
              print(f"{enemy.name} attacked you with their {enemy.ship.weapon.name} and did {enemy.ship.weapon.damage} damage!")
              self.ship.integrity -= enemy.ship.weapon.damage
            else:
              print(f"{enemy.name} attacked you with their {enemy.ship.weapon.name} and did {enemy.ship.weapon.damage - self.ship.shieldintegrity} damage! They also broke your shield!")
              self.ship.integrity -= enemy.ship.weapon.damage - self.ship.shieldintegrity
              self.ship.shieldintegrity = 0
          else:
            print(f"{enemy.name} damaged your shield!")
            self.ship.shieldintegrity -= enemy.ship.weapon.damage
        move = 0
      time.sleep(1)
    if self.ship.integrity <= 0:
      print("You died! It was a good run...")
      sys.exit()
    elif enemy.ship.integrity <= 0:
      print(f"You defeated {enemy.name}! You gained {enemy.reward} Void Stones!")
      self.add(enemy.reward)
      time.sleep(1)
    else:
      print("You ran away! Such a coward...")
      time.sleep(1)
    enemy.ship.integrity = enemy.ship.maxintegrity
    enemy.ship.shieldintegrity = enemy.ship.maxshieldintegrity
    enemy.ship.weapon = None
  def explore(self):
    global currency
    clear()
    print(f"You explored {self.location.name}!")
    time.sleep(1)
    result = str(random.choices(self.location.exploreresults, self.location.explorechances)[0]).lower()
    if "void stones" in result:
      val = math.trunc(self.location.rewardmax - random.uniform(0, self.location.rewardmax - self.location.rewardmin))
      self.add(val)
      print(f"You found {result}! You gained {val} Void Stones! You now have {self.currency} Void Stones!")
      time.sleep(1)
    elif "enemy" in result:
      enemy = entity(random.choice(self.location.entitynames), self.location, random.choice(self.location.entityships), self.location.rewardmin, self.location.rewardmax)
      enemy.ship.weapon = random.choice(self.location.entityweapons)
      print(f"You encountered {enemy.name}!")
      time.sleep(1)
      self.fight(enemy)
  def shop(self):
    global currency
    clear()
    print("What would you like to do?\n   (1) Storage\n   (2) Purchase")
    choice = input().lower()
    clear()
    if choice in ["1", "storage", "2", "purchase"]:
      print("What would you like to see?\n   (1) Ships\n   (2) Weapons")
      choice2 = input().lower()
      if choice in ["1", "storage"] and choice2 in ["1", "ships"]:
        clear()
        displayed = []
        print("Which ship would you like to view?")
        for i in ships:
          if i.owned:
            print(f"   ({len(displayed) + 1}) {i.name} - {i.maxintegrity} Health - {i.maxshieldintegrity} Shield - {i.maxfuel} Fuel")
            displayed.append(i)
        selected = None
        choice3 = input().lower()
        if choice3.isdigit():
          choice3 = int(choice3)
          if 1 <= choice3 <= len(displayed):
            selected = displayed[choice3 - 1]
        else:
          selected_index = index_object(ships, choice3)
          if selected_index is not None and ships[selected_index].owned:
            selected = ships[selected_index]
        if selected is not None:
          clear()
          choice4 = input(f"What would you like to do with your {selected.name}?\n   (1) Upgrade\n   (2) Equip\n")
          if choice4 in ["1", "upgrade"]:
            selected.upgrade()
          elif choice4 in ["2", "equip"]:
            print(f"You equipped your {selected.name}")
            time.sleep(1)
            selected.weapon = self.ship.weapon
            self.ship = selected
      elif choice in ["1", "storage"] and choice2 in ["2", "weapons"]:
        clear()
        displayed = []
        print("Which weapon would you like to view?")
        for i in weapons:
          if i.owned:
            print(f"   ({len(displayed) + 1}) {i.name} - {i.damage} Damage")
            displayed.append(i)
        selected = None
        choice3 = input().lower()
        if choice3.isdigit():
          choice3 = int(choice3)
          if 1 <= choice3 <= len(displayed):
            selected = displayed[choice3 - 1]
        else:
          selected_index = index_object(weapons, choice3)
          if selected_index is not None and weapons[selected_index].owned:
            selected = weapons[selected_index]
        if selected is not None:
          clear()
          choice4 = input(f"What would you like to do with your {selected.name}?\n   (1) Upgrade\n   (2) Equip\n")
          if choice4 in ["1", "upgrade"]:
            selected.upgrade()
          elif choice4 in ["2", "equip"]:
            print(f"You equipped your {selected.name}")
            time.sleep(1)
            self.ship.weapon = selected
      elif choice in ["2", "purchase"] and choice2 in ["1", "ships"]:
        clear()
        displayed = []
        print("Which ship would you like to purchase?")
        for i in ships:
          if not i.owned:
            print(f"   ({len(displayed) + 1}) {i.name} - {i.maxintegrity} Health - {i.maxshieldintegrity} Shield - {i.maxfuel} Fuel - {i.cost} Void Stones")
            displayed.append(i)
        choice3 = input().lower()
        selected = None
        if choice3.isdigit():
          choice3 = int(choice3)
          if 1 <= choice3 <= len(displayed):
            selected = displayed[choice3 - 1]
        else:
          selected_index = index_object(ships, choice3)
          if selected_index is not None and not ships[selected_index].owned:
            selected = ships[selected_index]
        if selected is not None:
          if self.currency >= selected.cost:
            selected.owned = True
            self.add(-1 * selected.cost)
            print(f"You purchased {selected.name}! Equip it through the storage!")
            time.sleep(1)
          else:
            print("You don't have enough Void Stones!")
            time.sleep(1)
      elif choice in ["2", "purchase"] and choice2 in ["2", "weapons"]:
        clear()
        displayed = []
        print("Which weapon would you like to purchase?")
        for i in weapons:
          if not i.owned:
            print(f"   ({len(displayed) + 1}) {i.name} - {i.damage} Damage - {i.cost} Void Stones")
            displayed.append(i)
        choice3 = input().lower()
        selected = None
        if choice3.isdigit():
          choice3 = int(choice3)
          if 1 <= choice3 <= len(displayed):
            selected = displayed[choice3 - 1]
        else:
          selected_index = index_object(weapons, choice3)
          if selected_index is not None and not ships[selected_index].owned:
            selected = weapons[selected_index]
        if selected is not None:
          if self.currency >= selected.cost:
            selected.owned = True
            self.add(-1 * selected.cost)
            print(f"You purchased {selected.name}! Equip it through the storage!")
            time.sleep(1)
          else:
            print("You don't have enough Void Stones!")
            time.sleep(1)
  def add(self, amount):
    self.currency += amount
    update(self)