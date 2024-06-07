import time, math
from functions import *
from data import update

class ship():
  def __init__(self, name, integrity, maxintegrity, shieldintegrity, maxshieldintegrity, fuel, maxfuel, cost, weapon, owned = False):
    self.name = name
    self.integrity = integrity
    self.maxintegrity = maxintegrity
    self.shieldintegrity = shieldintegrity
    self.maxshieldintegrity = maxshieldintegrity
    self.fuel = fuel
    self.maxfuel = maxfuel
    self.upgrades = {"integrity": 0, "shield integrity": 0, "fuel": 0}
    self.cost = cost
    self.weapon = weapon
    self.owned = owned
  def repair(self, player = False, fighting = False):
    if fighting:
      if player:
        if self.integrity < self.maxintegrity:
          print(f"You repaired your ship by {math.trunc((self.maxintegrity - self.integrity) / 10)}!")
        if self.shieldintegrity < self.maxshieldintegrity:
          print(f"You repaired your shield by {math.trunc((self.maxshieldintegrity - self.shieldintegrity) / 10)}!")
        self.integrity += math.trunc((self.maxintegrity - self.integrity) / 10)
        self.shieldintegrity += math.trunc((self.maxshieldintegrity - self.shieldintegrity) / 10)
      else:
        if self.integrity < self.maxintegrity:
          print(f"{self.name} repaired their ship by {math.trunc((self.maxintegrity - self.integrity) / 10)}!")
        if self.shieldintegrity < self.maxshieldintegrity:
          print(f"{self.name} repaired their shield by {math.trunc((self.maxshieldintegrity - self.shieldintegrity) / 10)}!")
        self.integrity += math.trunc((self.maxintegrity - self.integrity) / 10)
        self.shieldintegrity += math.trunc((self.maxshieldintegrity - self.shieldintegrity) / 10)
    else:
      clear()
      print(f"Your {self.name} has been repaired!")
      self.integrity = self.maxintegrity
      self.shieldintegrity = self.maxshieldintegrity
      time.sleep(1)
  def upgrade(self):
    global currency
    clear()
    print("What would you like to upgrade?")
    displayed = []
    for i in self.upgrades:
      if self.upgrades[i] < 3:
        print(f"   ({len(displayed)+1}) {i.title()} - {(self.upgrades[i] + 1) * self.cost * 2}")
        displayed.append(i)
    if len(displayed) == 0:
      print("You already maxed out all your ship upgrades!")
    else:
      choice = input("").lower()
      selected = None
      if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(displayed):
          selected = displayed[choice - 1]
      elif choice in displayed:
        selected = choice
      if selected is not None:
        if selected == "integrity":
          self.maxintegrity *= 2 ** (1/3)
          self.maxintegrity = math.trunc(self.maxintegrity)
          self.integrity = self.maxintegrity
        elif selected == "shield integrity":
          self.maxshieldintegrity *= 2 ** (1/3)
          self.maxshieldintegrity = math.trunc(self.maxshieldintegrity)
          self.shieldintegrity = self.maxshieldintegrity
        elif selected == "fuel":
          self.maxfuel *= 2 ** (1/3)
          self.maxfuel = math.trunc(self.maxfuel)
          self.fuel = self.maxfuel
        from data import player_data, player_class
        if player_data["currency"] >= (self.upgrades[selected] + 1) * self.cost * 2:
          player_class.add(-1 *((self.upgrades[selected] + 1) * self.cost * 2))
          self.upgrades[selected] += 1
          if self.upgrades[selected] == 3:
            print(f"You maxed out your {selected.capitalize()} upgrade!")
            time.sleep(1)
          else:
            print(f"You upgraded your {selected.capitalize()}!")
            time.sleep(1)
          update(player_class)
        else:
          print("You don't have enough Void Stones!")
          time.sleep(1)

ships = [
  ship("Starter", 100, 100, 25, 25, 50, 50, 50, None, owned = True),
  ship("Ionic Drive", 250, 250, 50, 50, 100, 100, 100, None),
  ship("Pulsive Drive", 500, 500, 100, 100, 250, 250, 250, None),
  ship("Fusion Drive", 1000, 1000, 250, 250, 500, 500, 500, None),
  ship("Plasmic Drive", 2500, 2500, 500, 500, 1000, 1000, 1000, None),
  ship("Warp Drive", 5000, 5000, 1000, 1000, 2500, 2500, 2500, None),
  ship("Hyper Drive", 10000, 10000, 2500, 2500, 5000, 5000, 5000, None),
  ship("Photon Drive", 25000, 25000, 5000, 5000, 10000, 10000, 10000, None),
  ship("Quantum Drive", 50000, 50000, 10000, 10000, 25000, 25000, 25000, None),
  ship("Singularity Drive", 100000, 100000, 25000, 25000, 50000, 50000, 50000, None),
  ship("Trans-Galactic Drive", 250000, 250000, 50000, 50000, 100000, 100000, 100000, None)
]

ships_base = [
  ship("Starter", 100, 100, 25, 25, 50, 50, 50, None),
  ship("Ionic Drive", 250, 250, 50, 50, 100, 100, 100, None),
  ship("Pulsive Drive", 500, 500, 100, 100, 250, 250, 250, None),
  ship("Fusion Drive", 1000, 1000, 250, 250, 500, 500, 500, None),
  ship("Plasmic Drive", 2500, 2500, 500, 500, 1000, 1000, 1000, None),
  ship("Warp Drive", 5000, 5000, 1000, 1000, 2500, 2500, 2500, None),
  ship("Hyper Drive", 10000, 10000, 2500, 2500, 5000, 5000, 5000, None),
  ship("Photon Drive", 25000, 25000, 5000, 5000, 10000, 10000, 10000, None),
  ship("Quantum Drive", 50000, 50000, 10000, 10000, 25000, 25000, 25000, None),
  ship("Singularity Drive", 100000, 100000, 25000, 25000, 50000, 50000, 50000, None),
  ship("Trans-Galactic Drive", 250000, 250000, 50000, 50000, 100000, 100000, 100000, None)
]