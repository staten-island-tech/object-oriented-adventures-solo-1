import time, random, math, os, sys

def index_object(list, name):
  return next((index for index, ship in enumerate(list) if ship.name.lower() == name.lower()), None)

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def boss_fight():
  from data import player_class
  player = player_class
  clear()
  print("Not very creative with cutscenes, so...")
  time.sleep(3)
  print("Singularity: I hate cutscenes. Just fight me already!")
  print("*Note: This Boss Bypasses All Shield*")
  time.sleep(3)
  boss = "Singularity"
  boss_hp = 1000000000
  special = None
  boss_weapon = "The FORCE???"
  boss_dmg = 50000
  clear()
  while player.ship.integrity > 0 and boss_hp > 0:
      clear()
      move = random.randint(1,10)
      if move == 1:
          special = "Pull"
          print(f"The {boss} uses Pull! You're next attack is ineffective!")
      elif move == 2:
          special = "Orbit"
          print(f"The {boss} uses Orbit! You're next attack is will damage you!")
      elif move == 3:
          special = "Quantum Influx"
          print(f"The {boss} uses Quantum Influx! You're next attack is may miss!")
      elif move == 4:
          special = "Miniature Blackhole"
          print(f"The {boss} uses Miniature Blackhole! You're turn might be skipped!")
      elif move == 5:
          special = "Spin"
          print(f"The {boss} uses Spin! It's damage increases!")
      else:
          special = None
          print(f"The {boss} uses {boss_weapon}! It deals {boss_dmg} damage!")
          player.ship.integrity -= boss_dmg
          if player.name == "jeffersongets100?" and player.ship.integrity < 1:
            print("Divine Intervention 🤣")
            player.ship.integrity = 1
      time.sleep(2)
      if player.ship.integrity >= 0:
          if special == "Spin":
              boss_dmg *= 1.5
          if (special == "Miniature Blackhole" and random.randint(1,10) > 7) or special != "Miniature Blackhole":
              print(f"The {boss} is on {boss_hp} HP!")
              time.sleep(.5)
              print(f"You are on {player.ship.integrity} HP!")
              time.sleep(.5)
              print("What do you do?")
              time.sleep(.5)
              print(" (1) - Fire")
              print(" (2) - Repair")
              print(" (3) - Skip")
              choice = input("").lower()
              if choice in ["1", "2", "3", "fire", "repair", "skip"]:
                  pass
              else:
                  print("Invalid Choice! A Random Option Will Be Chosen For You!")
                  time.sleep(1)
                  choice = random.choice(["1", "2", "3"])
              if choice in ["1", "fire"]:
                  if special == "Pull":
                      print("You fire your weapon, but nothing happened!")
                      time.sleep(1)
                  elif special == "Orbit":
                      print("You fire your weapon, but you hit yourself!")
                      time.sleep(1)
                      player.ship.integrity -= player.ship.weapon.damage
                      if player.name == "jeffersongets100?" and player.ship.integrity <= 0:
                        player.ship.integrity = 1
                  elif special == "Quantum Influx" and random.randint(1,10) < 7:
                      print("You fire your weapon, but it missed!")
                      time.sleep(1)
                  else:
                      print(f"You successfully hit the {boss}! It deals {player.ship.weapon.damage} damage!")
                      boss_hp -= player.ship.weapon.damage
                      time.sleep(1)
              elif choice in ["2", "repair"]:
                  player.ship.repair()
              elif choice in ["3", "skip"]:
                  print("You skipped your turn! Hopefully you made the right decision!")
                  time.sleep(1.5)
                  if random.randint(1,10) == 1 or (random.randint(1,10) in [1, 2, 3] and player.name == "jeffersongets100?"):
                      print("The boss is confused! It loses half it health!")
                      boss_hp /= 2
                      boss_hp = math.trunc(boss_hp)
                      time.sleep(1.5)
          else:
              print("Your turn has been skipped!")
              time.sleep(1)
  if player.ship.integrity > 0:
      print(f"You have overtaken the {boss}!")
      time.sleep(1)
      print("GG")
      sys.exit()
  else:
      print(f"You have been defeated by the {boss}...")
      time.sleep(1)
      print("So Close, Yet So Far...")
      time.sleep(1)
      print("Game Over")
      time.sleep(3)
      sys.exit()