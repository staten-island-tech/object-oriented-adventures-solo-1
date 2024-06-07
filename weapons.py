import time, math
from functions import *
from data import update

class weapon():
  def __init__(self, name, damage, cost, owned = False):
    self.name = name
    self.damage = damage
    self.cost = cost
    self.upgrades = {"damage": 0}
    self.owned = owned
  def upgrade(self):
    global currency
    clear()
    print("What would you like to upgrade?")
    displayed = 0
    for i in self.upgrades:
      if self.upgrades[i] < 3:
        print(f"   ({displayed + 1}) {i.title()} - {(self.upgrades[i] + 1) * self.cost * 2}")
        displayed += 1
    if displayed == 0:
      print("You already maxed out all your weapon upgrades!")
      time.sleep(1)
    else:
      choice = input("").lower()
      selected = None
      if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= displayed:
          selected = list(self.upgrades.keys())[choice - 1]
      elif choice in self.upgrades:
        selected = choice
      if selected is not None:
        from data import player_data, player_class
        if player_data["currency"] >= (self.upgrades[selected] + 1) * self.cost * 2:
          player_class.add(-1 * ((self.upgrades[selected] + 1) * self.cost * 2))
          self.upgrades[selected] += 1
          if selected == "damage":
            self.damage *= 2 ** (1/3)
            self.damage = math.trunc(self.damage)
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

weapons = [
  weapon("Pulse Laser", 25, 50, owned = True),
  weapon("Plasma Blaster", 50, 100),
  weapon("Railgun", 100, 250),
  weapon("Photon Torpedoes", 250, 500),
  weapon("Fusion Beam", 500, 1000),
  weapon("Quantum Disruptor", 1000, 2500),
  weapon("Antimatter Missiles", 2500, 5000),
  weapon("Dark Matter Cannon", 5000, 10000),
  weapon("Graviton Pulse Cannon", 10000, 25000),
  weapon("Singularity Projector", 25000, 50000),
  weapon("Hyperspace Cannon", 50000, 100000)
]

weapons_base = [
  weapon("Pulse Laser", 25, 50),
  weapon("Plasma Blaster", 50, 100),
  weapon("Railgun", 100, 250),
  weapon("Photon Torpedoes", 250, 500),
  weapon("Fusion Beam", 500, 1000),
  weapon("Quantum Disruptor", 1000, 2500),
  weapon("Antimatter Missiles", 2500, 5000),
  weapon("Dark Matter Cannon", 5000, 10000),
  weapon("Graviton Pulse Cannon", 10000, 25000),
  weapon("Singularity Projector", 25000, 50000),
  weapon("Hyperspace Cannon", 50000, 100000)
]