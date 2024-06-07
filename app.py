#Cheat Code for Whalen's testing purposes ONLY: use "ifiwerearichman" in main menu for free currency
#Cheat Code 2 for Whalen's testing purposes ONLY: name yourself: "jeffersongets100?" for boss invincibility and confuse the boss more often lol
#Fuel is useless lol :)

import time
from entities import *
from ship import *
from weapons import *
from locations import *
from functions import *
from player import *
from data import update

clear()
input("Notice: If you type anything random, then you may or may not see the 'invalid input' message, but you will exit the current option either way. You can use this to exit shops and stuff. Good Luck!")
clear()

name = input("Name your character: ")
player = player(name, locations[index_object(locations, "earth")], ships[index_object(ships, "starter")], 0, 0)
player.ship.weapon = weapons[index_object(weapons, "pulse laser")]

while True:
  clear()
  update(player)
  from data import player_class
  player = player_class
  print(f"Current location: {player.location.name}")
  print(f"Current ship: {player.ship.name} | Health: {player.ship.integrity}/{player.ship.maxintegrity} | Shield: {player.ship.shieldintegrity}/{player.ship.maxshieldintegrity} | Fuel: {player.ship.fuel}/{player.ship.maxfuel}")
  print(f"Current weapon: {player.ship.weapon.name} | Damage: {player.ship.weapon.damage}")
  print(f"Void Stones: {player.currency}")
  print("What do you want to do?")
  print("   (1) Explore")
  print("   (2) Repair")
  print("   (3) Shop")
  print("   (4) Travel")
  print("   (5) Quit")
  if player.location.name == "Black Hole":
    print("   (?) ???")
  choice = input().lower()
  if choice == "1" or choice == "explore":
    player.explore()
  elif choice == "2" or choice == "repair":
    player.ship.repair()
  elif choice == "3" or choice == "shop":
    player.shop()
  elif choice == "4" or choice == "travel":
    clear()
    print("Where do you want to travel?")
    for i, loc in enumerate(locations):
      print(f"   ({i + 1}) {loc.name}")
    try:
      loc_choice = int(input()) - 1
      if 0 <= loc_choice < len(locations):
        player.location = locations[loc_choice]
        print(f"Traveled to {player.location.name}!")
    except:
      print("Invalid location!")
      time.sleep(1)
  elif choice == "5" or choice == "quit":
    print("Thanks for playing!")
    break
  elif player.location.name == "Black Hole" and choice in ["?","???"]:
    boss_fight()
  elif choice == "ifiwerearichman":
    print("You are one now! +7777777 Void Stones")
    player.add(7777777)
    time.sleep(1)
  else:
    if choice != "":
      print("Invalid input!")
      time.sleep(1)