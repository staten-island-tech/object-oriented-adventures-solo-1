import math, time, random, sys
from ship import *
from weapons import *
from locations import *
from functions import *

class entity():
  def __init__(self, name, location, ship, rewardmin, rewardmax):
    self.name = name
    self.location = location
    self.ship = ship
    self.reward = math.trunc(rewardmax - random.uniform(0, rewardmax - rewardmin))
