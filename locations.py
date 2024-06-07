from ship import *
from weapons import *
from functions import *

class location():
  def __init__(self, name, exploreresults, explorechances, entitynames, entityships, entityweapons, rewardmin, rewardmax):
    self.name = name
    self.exploreresults = exploreresults
    self.explorechances = explorechances
    self.entitynames = entitynames
    self.entityships = entityships
    self.entityweapons = entityweapons
    self.rewardmin = rewardmin
    self.rewardmax = rewardmax

locations = [
  location("Earth", ["void stones", "enemy"], [0.2, 0.8], ["Terrarians"], [ships_base[index_object(ships_base, "Starter")], ships_base[index_object(ships_base, "Ionic Drive")]], [weapons_base[index_object(weapons_base, "Pulse Laser")]], 1, 100),
  location("Alpha Centauri", ["void stones", "enemy"], [0.3, 0.7], ["Aliens"], [ships_base[index_object(ships_base, "Starter")], ships_base[index_object(ships_base, "Ionic Drive")], ships_base[index_object(ships_base, "Pulsive Drive")]], [weapons_base[index_object(weapons_base, "Pulse Laser")], weapons_base[index_object(weapons_base, "Plasma Blaster")]], 100, 250),
  location("Orion", ["void stones", "enemy"], [0.4, 0.6], ["Aliens", "Alien Spartan", "Alien Gladiator", "Alien Soldier", "Alien Commander"], [ships_base[index_object(ships_base, "Starter")], ships_base[index_object(ships_base, "Ionic Drive")], ships_base[index_object(ships_base, "Pulsive Drive")]], [weapons_base[index_object(weapons_base, "Pulse Laser")], weapons_base[index_object(weapons_base, "Plasma Blaster")], weapons_base[index_object(weapons_base, "Railgun")]], 250, 500),
  location("Betelgeuse", ["void stones", "enemy"], [0.2, 0.8], ["Aliens", "Alien Beetles", "Sand Aliens", "Alien Pharoahs", "Alien God"], [ships_base[index_object(ships_base, "Fusion Drive")], ships_base[index_object(ships_base, "Plasmic Drive")], ships_base[index_object(ships_base, "Warp Drive")], ships_base[index_object(ships_base, "Hyper Drive")]], [weapons_base[index_object(weapons_base, "Photon Torpedoes")], weapons_base[index_object(weapons_base, "Fusion Beam")], weapons_base[index_object(weapons_base, "Quantum Disruptor")], weapons_base[index_object(weapons_base, "Antimatter Missiles")]], 500, 1000),
  location("Polarius", ["void stones", "enemy"], [0.1, 0.9], ["Aliens", "Ice Alien", "Alien Yeti"], [ships_base[index_object(ships_base, "Warp Drive")], ships_base[index_object(ships_base, "Hyper Drive")], ships_base[index_object(ships_base, "Photon Drive")], ships_base[index_object(ships_base, "Quantum Drive")]], [weapons_base[index_object(weapons_base, "Quantum Disruptor")], weapons_base[index_object(weapons_base, "Antimatter Missiles")], weapons_base[index_object(weapons_base, "Dark Matter Cannon")], weapons_base[index_object(weapons_base, "Graviton Pulse Cannon")]], 1000, 2500),
  location("Black Hole", ["void stones", "enemy"], [0.1, 0.9], ["Black Hole Creature"], [ships_base[index_object(ships_base, "Quantum Drive")], ships_base[index_object(ships_base, "Singularity Drive")], ships_base[index_object(ships_base, "Trans-Galactic Drive")]], [weapons_base[index_object(weapons_base, "Graviton Pulse Cannon")], weapons_base[index_object(weapons_base, "Singularity Projector")], weapons_base[index_object(weapons_base, "Hyperspace Cannon")]], 2500, 10000)
]