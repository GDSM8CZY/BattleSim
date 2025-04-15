# @title Battle Sim Code
import random as r
import time as t

# Swords
class Cheat_sword:
  # 9999dmg
  dmg = {'low':9999, 'high':9999}
  # 1-20m
  range = {'low':1, 'high':200}
  # 100%
  hit_chance = 100
  # 1 = 0% + 100%
  crit_dmg = 1
  # 100%
  crit_chance = 100

class Sword:
  # 4-5dmg
  dmg = {'low':4, 'high':5}
  # 1-4m
  range = {'low':1, 'high':4}
  # 70%
  hit_chance = 70
  # 2 = 100% + 100%
  crit_dmg = 2
  # 5%
  crit_chance = 5

class Dagger:
  # 3-4dmg
  dmg = {'low':1, 'high':3}
  # 1-2m
  range = {'low':1, 'high':2}
  # 95%
  hit_chance = 95
  # 4 = 300% + 100%
  crit_dmg = 4
  # 60%
  crit_chance = 60

class Claymore:
  # 5-7dmg
  dmg = {'low':5, 'high':7}
  # 1-6m
  range = {'low':1, 'high':6}
  # 20%
  hit_chance = 20
  # 0 = 100% + 100%
  crit_dmg = 0
  # 0%
  crit_chance = 0

# Bows
class Long_bow:
  # 1-3dmg
  dmg = {'low':1, 'high':3}
  # 4-10m
  range = {'low':4, 'high':10}
  # 65%
  hit_chance = 65
  # 5 = 400% + 100%
  crit_dmg = 5
  # 5%
  crit_chance = 5
  # fires 10 shots
  hit_times = 5

class Short_bow:
  # 4-5dmg
  dmg = {'low':4, 'high':5}
  # 5-8m
  range = {'low':5, 'high':8}
  # 65%
  hit_chance = 65
  # 2 = 100% + 100%
  crit_dmg = 2
  # 1%
  crit_chance = 1
  # fires 2 shots
  hit_times = 2

class Crossbow:
  # 1dmg
  dmg = {'low':1, 'high':1}
  # 3-5m
  range = {'low':3, 'high':5}
  # 50%
  hit_chance = 50
  # 3 = 200% + 100%
  crit_dmg = 3
  # 5%
  crit_chance = 5
  # fires 10 shots
  hit_times = 10

# Fighters
class Player:
  hp = 20
  # 2m/s
  spd = 2
  # healing potions left
  heals = 3
  # will chose wepons later

class Enemy:
  hp = 20
  # 1m/s
  spd = 1
  # healing potions left
  heals = 3
  dmg = {'low':3, 'high':5}
  # 1-7m
  range = {'low':1, 'high':7}
  # 75%
  hit_chance = 75
  # 2 = 100% + 100%
  crit_dmg = 2
  # 1%
  crit_chance = 1

player = Player()
enemy = Enemy()
print("how fast do you want the game to be? (any positive number that reduces delays in game)")
while True:
  try:
    speed = float(input())
    break
  except:
    print("something went wrong, try again")

# 10m
distance = 10
# is it the players turn
player_turn = True
turn = 0

def turn_end_info():
  global turn
  turn += 1

  print("_"*20)
  print(f"TURN: {turn}")
  t.sleep(0.5/speed)
  print("PLAYER HP:", "+" * player.hp, f"({player.hp}hp)")
  t.sleep(0.5/speed)
  print("ENEMY HP:", "+" * enemy.hp, f"({enemy.hp}hp)")
  t.sleep(0.5/speed)
  distance_dashes = "- " * distance
  print(f"P {distance_dashes}E", f"({distance}m)")
  t.sleep(0.5/speed)
  print(f"YOUR HEALS LEFT: {player.heals}")
  t.sleep(0.5/speed)
  print(f"ENEMY HEALS LEFT: {enemy.heals}")
  print("_"*40)

# Called when Game ends
def End(win_or_lose):
  print(f"You {win_or_lose}")
  global turn
  print(f"turns: {turn}")

# name: battle sim
print(
"""
@@@@    @@@@@   @@@@@   @@@@@    @       @@@@@
@   @   @   @     @       @      @       @
@   @   @   @     @       @      @       @
@@@@    @@@@@     @       @      @       @@@
@   @   @   @     @       @      @       @
@   @   @   @     @       @      @       @
@@@@    @   @     @       @      @@@@@   @@@@@

@@@@@   @@@@@   @@   @@
@         @     @ @ @ @
@         @     @  @  @       |------------+
@@@@@     @     @     @   o===|@@@@@@@@@@@@@@)
    @     @     @     @       |------------+
    @     @     @     @
@@@@@   @@@@@   @     @
_________________________________________________
How To Play:
  - enter a number to select actions/choices

  - the distance between you and the enemy
    is indicated by the dashes

  - enemy and player health is indicated
    by the plus symbols

  - you can have your choice of sword and bow

  - you and the enemy start with 3 healing potions,
    one healing potion will heal you 5 health
""")

t.sleep(16/speed)

# select melee weapon
while True:
  print(
  """Do you want a sword, a dagger, or a claymore?
  ________________________________
  Sword (enter 1 to select):
  - 4 to 5 dammage
  - range of 1 to 4 meters
  - 70% chance to hit
  - 5% chance to critical hit and do +100% dammage""")
  t.sleep(1/speed)
  print(
  """________________________________
  Dagger (enter 2 to select):
  - 1 to 3 dammage
  - range of 1 to 2 meters
  - 95% chance to hit
  - 60% chance to critical hit and do +300% dammage""")
  t.sleep(1/speed)
  print(
  """________________________________
  Claymore (enter 3 to select):
  - 5 to 7 dammage
  - range of 1 to 5 meters
  - 20% chance to hit
  - cannot do critical hits""")
  try:
    melee_weapon_select = int(input())
    if melee_weapon_select == 1:
      print("|-Sword Selected-|")
      player.sword = Sword()
      break
    elif melee_weapon_select == 2:
      print("|-Dagger Selected-|")
      player.sword = Dagger()
      break
    elif melee_weapon_select == 3:
      print("|-Claymore Selected-|")
      player.sword = Claymore()
      break
    else:
      print("Number not one of the options")
  except:
    print("something went wrong, try again")

t.sleep(1/speed)

# select ranged weapon
while True:
  print(
  """What bow do you want?
  ________________________________
  Long Bow (enter 1 to select):
  - 1 to 3 dammage
  - range of 4 to 10 meters
  - 45% chance to hit
  - 5% chance to critical hit and do +400% dammage
  - shoots 5 times""")
  t.sleep(1/speed)
  print(
  """________________________________
  Short Bow (enter 2 to select):
  - 4 to 5 dammage
  - range of 5 to 8 meters
  - 65% chance to hit
  - 1% chance to critical hit and do +100% dammage
  - shoots 2 times""")
  t.sleep(1/speed)
  print(
  """________________________________
  Crossbow (enter 3 to select):
  - 1 dammage
  - range of 3 to 5 meters
  - 30% chance to hit
  - 5% chance to critical hit and do +200% dammage
  - shoots 10 times""")
  try:
    ranged_weapon_select = int(input())
    if ranged_weapon_select == 1:
      print("|-Long bow Selected-|")
      player.bow = Long_bow()
      break
    elif ranged_weapon_select == 2:
      print("|-Short bow Selected-|")
      player.bow = Short_bow()
      break
    elif ranged_weapon_select == 3:
      print("|-Crossbow Selected-|")
      player.bow = Crossbow()
      break
    else:
      print("Number not one of the options")
  except:
    print("something went wrong, try again")

if speed == 1.234:
  player.sword = Cheat_sword()
  print("|-Cheat sword acquired-|")

if speed == 32.64:
  player.hp *= 5
  player.sword.dmg['low'] *= 5
  player.sword.dmg['high'] *= 5
  player.bow.dmg['low'] *= 5
  player.bow.dmg['high'] *= 5
  enemy.hp *= 5
  enemy.dmg['low'] *= 5
  enemy.dmg['high'] *= 5
  print("|-Big numbers activated-|")

t.sleep(1/speed)
turn_end_info()
game_running = True

while game_running == True:
  # Players turn code
  while player_turn == True:
    hit_dmg = 0
    print("What do you want to do?")
    last_input = input("Attack Enemy-1 | Heal-2 | Run Away-3 | Chase Enemy-4 | Quit Game-5 ")
    try:
      last_input = int(last_input)
    except:
      print("|-Something went wrong, try again-|")
    print("_"*20)

    # Attack option code
    if last_input == 1:
      # sword attack code
      if distance >= player.sword.range['low'] and distance <= player.sword.range['high']:
        if r.randint(1, 100) <= player.sword.hit_chance:
          if r.randint(1, 100) <= player.sword.crit_chance:
            hit_dmg = r.randint(player.sword.dmg['low'], player.sword.dmg['high']) * player.sword.crit_dmg
            print(f"|-You crit and did {hit_dmg} damage-|")
          else:
            hit_dmg = r.randint(player.sword.dmg['low'], player.sword.dmg['high'])
            print(f"|-You hit and did {hit_dmg} damage-|")
          if enemy.hp - hit_dmg <= 0:
            enemy.hp = 0
          else:
            enemy.hp -= hit_dmg
        else:
          print("|-You missed!-|")
          hit_dmg = 0
      # bow attack code
      elif distance >= player.bow.range['low'] and distance <= player.bow.range['high']:
        for shots in list(range(player.bow.hit_times)):
          if r.randint(1, 100) <= player.bow.hit_chance:
            if r.randint(1, 100) <= player.bow.crit_chance:
              hit_dmg = r.randint(player.bow.dmg['low'], player.bow.dmg['high']) * player.bow.crit_dmg
              print(f"|-You crit and did {hit_dmg} damage-|")
            else:
              hit_dmg = r.randint(player.bow.dmg['low'], player.bow.dmg['high'])
              print(f"|-You hit and did {hit_dmg} damage-|")
            if enemy.hp - hit_dmg <= 0:
              enemy.hp = 0
            else:
              enemy.hp -= hit_dmg
          else:
            print("|-You missed!-|")
            hit_dmg = 0
          t.sleep(1/speed)
      else:
        print("|-The Enemy was not in range!-|")
      turn_end_info()
      player_turn = False

    # Heal option code
    if last_input == 2:
      if player.heals > 0 and player.hp <= 20:
        player.heals -= 1
        if player.hp + 5 >= 20:
          print("|-You healed to max hp-|")
          player.hp = 20
        else:
          print("|-You healed for 5 hp-|")
          player.hp += 5
      elif player.heals == 0:
        print("|-Out of heals, try something else-|")
      turn_end_info()
      player_turn = False

    # Run option code
    if last_input == 3:
      if r.randint(1, 100) <= 50:
        print("|-You ran-|")
        distance += player.spd
      else:
        print("|-You tried to run, but the enemy chases you!-|")
        distance -= enemy.spd
      turn_end_info()
      player_turn = False

    # Chase option code
    if last_input == 4 and distance > player.spd:
      distance -= player.spd
      print("|-You chase the enemy!-|")
      turn_end_info()
      player_turn = False

    # Quit game code
    if last_input == 5:
      game_running = False
      break

    # Error handling
    if last_input not in [1, 2, 3, 4, 5]:
      print("|-put in 1, 2, 3, 4 or 5 to select an option-|")

    # player win code
    if enemy.hp <= 0:
      End("Win!")
      game_running = False
      player_turn = True
      break

  # Enemy turn code
  while player_turn == False:
    hit_dmg = 0
    t.sleep(r.randint(2, 5)/speed)
    # enemy heal code
    if enemy.hp <= (enemy.hp/2) and enemy.heals >= 1:
      enemy.heals -= 1
      enemy.hp += (enemy.hp/4)
      print("|-The enemy healed!-|")
      turn_end_info()
      player_turn = True
    else:
      # enemy attack code
      if distance <= enemy.range['high'] and distance >= enemy.range['low']:
        if r.randint(1, 100) <= 80:
          if r.randint(1, 100) <= enemy.hit_chance:
            if r.randint(1, 100) <= enemy.crit_chance:
              hit_dmg = r.randint(enemy.dmg['low'], enemy.dmg['high']) * enemy.crit_dmg
              print(f"|-The enemy crit you for {hit_dmg} damage-|")
              turn_end_info()
              if player.hp - hit_dmg == 0:
                player.hp = 0
              else:
                player.hp -= hit_dmg
              player_turn = True
            else:
              hit_dmg = r.randint(enemy.dmg['low'], enemy.dmg['high'])
              print(f"|-The enemy hit you for {hit_dmg} damage-|")
              if player.hp - hit_dmg == 0:
                player.hp = 0
              else:
                player.hp -= hit_dmg
              turn_end_info()
              player_turn = True
          else:
            print("|-The enemy missed!-|")
            turn_end_info()
            player_turn = True
        else:
          # enemy chase code
          distance += enemy.spd
          print("|-The enemy runs!-|")
          turn_end_info()
          player_turn = True
      else:
        # enemy run code
        distance -= enemy.spd
        print("|-The enemy chases you!-|")
        turn_end_info()
        player_turn = True

  # enemy win code
  if player.hp <= 0:
    End("Lose")
    game_running = False
    player_turn = False
    break
