#----------------------------
# Name:        Exercise 9 (main.py)
# Purpose:     Guides the user through the character creating process for pathfinder 2e
#
# Author:      628262
# Created:     10-Dec-2019
# Updated:     18-Nov-2019
#----------------------------
#Some parts of the program may take a bit of time to load

import logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
import random
from itertools import combinations

logging.debug('Start of program')

#FUNCTIONS
#Creates a random combination of items from a list
def randomSelection(size, theList):
  '''
  This function takes a random combination of items from a list.
  
  This function takes a random combination of items from a list, and uses it to create a new list. The size of
  the selection can be specified.
  
  Parameters
  ----------------------------
  size : int
    The size of the combination
  theList : list
    The list from which a combination is to be taken
  
  Returns
  ----------------------------
  list
    The random combination of list items
  '''
  logging.debug('Starting randomSelection with arguments size' + str(size) + ' and list ' + str(theList))
  
  itemCombination = list(combinations(theList, size))
  
  randomItemCombination = list(itemCombination[random.randint(0,len(itemCombination)-1)])
  logging.debug('randomItemCombination == ' + str(randomItemCombination))
  
  return randomItemCombination

#assert randomSelection(3, [1,2,'three']) == [1,2,'three'], 'expecting a random combination of a list with the same size as the list to be equal to the list'

#CONSTANTS
ERROR = "That is not a valid option. Please enter an integer corresponding to your selected choice"

# LISTS
#preset variables
#Default stats
statList = [10,10,10,10,10,10]

#Default modifiers
modifierList = [0,0,0,0,0,0]

#Epic Skills
skillList = ['Acrobatics', 'Arcana', 'Athletics', 'Crafting', 'Deception', 'Diplomacy', 'Intimidation', 'Lore', 'Medicine', 'Nature', 'Occultism', 'Performance', 'Religion', 'Society', 'Stealth', 'Survival', 'Thievery']

#cantrips and spells (1st level)
arcaneCantrips = ['Electric Arc', 'Shield', 'Tanglefoot', 'Read Aura', 'Detect Magic', 'Ghost Sound', 'Daze', 'Telekinetic Projectile']
arcaneSpells = ['Feather Fall', 'Fleet Step', 'Illusory Object', 'Mending', 'Negate Aroma', 'Sleep', 'Summon Construct', 'Ventriloquism']
divineCantrips = ['Chill Touch', 'Daze', 'Disrupt Undead', 'Divine Lance', 'Forbidding Ward', 'Guidance', 'Sigil', 'Stabilize']
divineSpells = ['Alarm', 'Bane', 'Create Water', 'Disrupting Weapons', 'Harm', 'Lock', 'Magic Weapon', 'Purify Food and Drink']
occultCantrips = ['Chill Touch', 'Dancing Lights', 'Daze', 'Light', 'Mage Hand', 'Shield', 'Sigil', 'Telekinetic Projectile']
occultSpells = ['Bane', 'Command', 'Detect Alignment', 'Illusory Object', 'Lock', 'Magic Aura', 'Protection', 'Sanctuary']
primalCantrips = ['Acid Splash', 'Dancing Lights', 'Detect Magic', 'Disrupt Undead', 'Electric Arc', 'Prestidigitation', 'Ray of Frost', 'Stabilize']
primalSpells = ['Air Bubble', 'Fleet Step', 'Grease', 'Magic Fang', 'Pass Without Trace', 'Pest Form', 'Shillelagh', 'Summon Plant or Fungus']

#Whether or not the character has received this boost already
strengthBoost = False
dexterityBoost = False
constitutionBoost = False
intelligenceBoost = False
wisdomBoost = False
charismaBoost = False

#Program begins
characterName = input("What is your character's name? ")
characterAge = input("Age: ")
characterGender = input("Gender: ")

#Character Alignment
continueRunning = True
while continueRunning == True:
  try:
    print("Is your character good or evil?")
    print("1) Good 2) Neutral 3) Evil 4) Random")
    goodOrEvil = int(input())
    continueRunning = False
    if not isinstance(goodOrEvil, int):
      raise TypeError
    if goodOrEvil > 4 or goodOrEvil < 1:
      raise ValueError
  except (ValueError,TypeError):
    print(ERROR)
    continueRunning = True
if goodOrEvil == 4:
  goodOrEvil = random.randint(1,3)

logging.debug('goodOrEvil == ' + str(goodOrEvil))

continueRunning = True
while continueRunning == True:
  try:
    print("Is your character lawful or chaotic?")
    print("1) Lawful 2) Neutral 3) Chaotic 4) Random")
    lawfulOrChaotic = int(input())
    continueRunning = False
    if not isinstance(lawfulOrChaotic, int):
      raise TypeError
    if lawfulOrChaotic > 4 or lawfulOrChaotic < 1:
      raise ValueError
  except (ValueError, TypeError):
    print(ERROR)
    continueRunning = True
if lawfulOrChaotic == 4:
  lawfulOrChaotic = random.randint(1,3)
  
logging.debug('lawfulOrChaotic == ' + str(lawfulOrChaotic))
  
#Ancestry
continueRunning = True
while continueRunning == True:
  try:
    print("Choose an ancestry:")
    print("1) Dwarf 2) Elf 3) Gnome 4) Goblin 5) Halfling 6) Human 7) Random")
    ancestry = int(input())
    continueRunning = False
    if not isinstance(ancestry, int):
      raise TypeError
    if ancestry > 7 or ancestry < 1:
      raise ValueError
  except (ValueError, TypeError):
    print(ERROR)
    continueRunning = True
if ancestry == 7:
  ancestry = random.randint(1,6)
  
logging.debug('ancestry == ' + str(ancestry))

#Dwarf
if ancestry == 1:
  hitPoints = 10
  speed = 20
  statList[2] = statList[2] + 2
  statList[4] = statList[4] + 2
  statList[5] = statList[5] - 2
  constitutionBoost = True
  wisdomBoost = True
  #assert statList[5]==8, 'expecting dwarf charisma to be 8'
#Elf
elif ancestry == 2:
  hitPoints = 6
  speed = 30
  statList[1] = statList[1] + 2
  statList[3] = statList[3] + 2
  statList[2] = statList[2] - 2
  dexterityBoost = True
  intelligenceBoost = True
  #assert statList[1]==12, 'expecting elf dexterity to be 12'
#Gnome
elif ancestry == 3:
  hitPoints = 8
  speed = 25
  statList[2] = statList[2] + 2
  statList[5] = statList[5] + 2
  statList[0] = statList[0] - 2
  constitutionBoost = True
  charismaBoost = True
  #assert statList[5]==12, 'expecting gnome charisma to be 12'
#Goblin
elif ancestry == 4:
  hitPoints = 6
  speed = 25
  statList[1] = statList[1] + 2
  statList[5] = statList[5] + 2
  statList[4] = statList[4] - 2
  dexterityBoost = True
  charismaBoost = True
  #assert statList[4]==8, 'expecting goblin wisdom to be 8'
#Halfling
elif ancestry == 5:
  hitPoints = 6
  speed = 25
  statList[1] = statList[1] + 2
  statList[4] = statList[4] + 2
  statList[0] = statList[0] - 2
  dexterityBoost = True
  wisdomBoost = True
  #assert statList[1]==12, 'expecting halfling dexterity to be 12'
#Human
else:
  hitPoints = 8
  speed = 25

#Free ability boost
continueRunning = True
continueToRun = True
while continueRunning == True and continueToRun == True:
  try:
    print("Choose a free ability boost:")
    print("1) Strength 2) Dexterity 3) Constitution 4) Intelligence 5) Wisdom 6) Charisma 7) Random")
    abilityBoost1 = int(input())
    continueRunning = False
    if not isinstance(abilityBoost1, int):
      raise TypeError
    if abilityBoost1 > 7 or abilityBoost1 < 1:
      raise ValueError
  except (TypeError, ValueError):
    print(ERROR)
    continueRunning = True

  if abilityBoost1 == 1 and strengthBoost == True or abilityBoost1 == 2 and dexterityBoost == True or abilityBoost1 == 3 and constitutionBoost == True or abilityBoost1 == 4 and intelligenceBoost == True or abilityBoost1 == 5 and wisdomBoost == True or abilityBoost1 == 6 and charismaBoost == True:
    print("That is not a valid option. Please choose an ability boost that you have not received yet.")
    print("You currently have ability boosts in:")
    if strengthBoost == True:
      print("strength")
    if dexterityBoost == True:
      print("dexterity")
    if constitutionBoost == True:
      print("constitution")
    if intelligenceBoost == True:
      print("intelligence")
    if wisdomBoost == True:
      print("wisdom")
    if charismaBoost == True:
      print("charisma")
    print("Choose a free ability boost:")
    print("1) Strength 2) Dexterity 3) Constitution 4) Intelligence 5) Wisdom 6) Charisma 7) Random")
    abilityBoost1 = int(input())
  else:
    continueToRun = False
  if abilityBoost1 == 7:
    abilityBoost1 = random.randint(1,6)
    while abilityBoost1 == 1 and strengthBoost == True or abilityBoost1 == 2 and dexterityBoost == True or abilityBoost1 == 3 and constitutionBoost == True or abilityBoost1 == 4 and intelligenceBoost == True or abilityBoost1 == 5 and wisdomBoost == True or abilityBoost1 == 6 and charismaBoost == True:
      abilityBoost1 = random.randint(1,6)
  if abilityBoost1 == 1:
    statList[0] = statList[0] + 2
    strengthBoost = True
  elif abilityBoost1 == 2:
    statList[1] = statList[1] + 2
    dexterityBoost = True
  elif abilityBoost1 == 3:
    statList[2] = statList[2] + 2
    constitutionBoost = True
  elif abilityBoost1 == 4:
    statList[3] = statList[3] + 2
    intelligenceBoost = True
  elif abilityBoost1 == 5:
    statList[4] = statList[4] + 2
    wisdomBoost = True
  else:
    statList[5] = statList[5] + 2
    charismaBoost = True

logging.debug('abilityBoost1 == ' + str(abilityBoost1))
  
#Free Ability Boost for Human Ancestry
if ancestry == 6:
  print("Choose a free ability boost:")
  print("1) Strength 2) Dexterity 3) Constitution 4) Intelligence 5) Wisdom 6) Charisma 7) Random")
  abilityBoost2 = int(input())
  while abilityBoost2 != 1 and abilityBoost2 != 2 and abilityBoost2 != 3 and abilityBoost2 != 4 and abilityBoost2 != 5 and abilityBoost2 != 6 and abilityBoost2 != 7:
    print(ERROR)
    print("Choose a free ability boost:")
    print("1) Strength 2) Dexterity 3) Constitution 4) Intelligence 5) Wisdom 6) Charisma 7) Random")
    abilityBoost2 = int(input())
  while abilityBoost2 == 1 and strengthBoost == True or abilityBoost2 == 2 and dexterityBoost == True or abilityBoost2 == 3 and constitutionBoost == True or abilityBoost2 == 4 and intelligenceBoost == True or abilityBoost2 == 5 and wisdomBoost == True or abilityBoost2 == 6 and charismaBoost == True:
    print(ERROR)
    print("You currently have ability boosts in:")
    if strengthBoost == True:
      print("strength")
    if dexterityBoost == True:
      print("dexterity")
    if constitutionBoost == True:
      print("constitution")
    if intelligenceBoost == True:
      print("intelligence")
    if wisdomBoost == True:
      print("wisdom")
    if charismaBoost == True:
      print("charisma")
    print("Choose a free ability boost:")
    print("1) Strength 2) Dexterity 3) Constitution 4) Intelligence 5) Wisdom 6) Charisma 7) Random")
    abilityBoost2 = int(input())
  if abilityBoost2 == 7:
    abilityBoost2 = random.randint(1,6)
    while abilityBoost2 == 1 and strengthBoost == True or abilityBoost2 == 2 and dexterityBoost == True or abilityBoost2 == 3 and constitutionBoost == True or abilityBoost2 == 4 and intelligenceBoost == True or abilityBoost2 == 5 and wisdomBoost == True or abilityBoost2 == 6 and charismaBoost == True:
      abilityBoost2 = random.randint(1,6)
  if abilityBoost2 == 1:
    statList[0] = statList[0] + 2
  elif abilityBoost2 == 2:
    statList[1] = statList[1] + 2
  elif abilityBoost2 == 3:
    statList[2] = statList[2] + 2
  elif abilityBoost2 == 4:
    statList[3] = statList[3] + 2
  elif abilityBoost2 == 5:
    statList[4] = statList[4] + 2
  else:
    statList[5] = statList[5] + 2
  logging.debug('abilityBoost2 == ' + str(abilityBoost2))
    
#Choosing a class
continueRunning = True
while continueRunning == True:
  try:
    print("Choose a class:")
    print("1) Alchemist 2) Barbarian 3) Bard 4) Champion 5) Cleric 6) Druid 7) Fighter 8) Monk 9) Ranger 10) Rogue 11) Sorcerer 12) Wizard 13) Random")
    characterClass = int(input())
    continueRunning = False
    if not isinstance(characterClass, int):
      raise TypeError
    if characterClass > 13 or characterClass < 1:
      raise ValueError
  except (TypeError,ValueError):
    print(ERROR)
    continueRunning = True
if characterClass == 13:
  characterClass = random.randint(1,12)

logging.debug('characterClass == ' + str(characterClass))
  
#Class-based stat boosts
if characterClass == 1 or characterClass == 12:
  statList[3] = statList[3] + 2
elif characterClass == 2:
  statList[0] = statList[0] + 2
elif characterClass == 3 or characterClass == 11:
  statList[5] = statList[5] + 2
elif characterClass == 5 or characterClass == 6:
  statList[4] = statList[4] + 2
elif characterClass == 10:
  statList[1] = statList[1] + 2
else:
  continueRunning = True
  while continueRunning == True:
    try:
      print("Choose a stat boost:")
      print("1) Strength 2) Dexterity 3) Random")
      strengthOrDexterityBoost = int(input())
      continueRunning = False
      if not isinstance(strengthOrDexterityBoost, int):
        raise TypeError
      if strengthOrDexterityBoost < 1 or strengthOrDexterityBoost > 3:
        raise ValueError
    except (ValueError, TypeError):
      print(ERROR)
      continueRunning = True
  if strengthOrDexterityBoost == 3:
    strengthOrDexterityBoost = random.randint(1,2)
  if strengthOrDexterityBoost == 1:
    statList[0] = statList[0] + 2
  if strengthOrDexterityBoost == 2:
    statList[1] == statList[1] + 2



#calculating ability score modifiers
logging.debug('calculating modifiers')
logging.debug('Stats are ' + str(statList))
for i in range (0,len(statList),1):
  intermediate = statList[i]-10
  modifierList[i] = int(intermediate/2)

logging.debug('Modifiers are ' + str(modifierList))
  
#adding more HP
hitPoints = hitPoints + modifierList[2]
if characterClass == 1 or characterClass == 3 or characterClass == 5 or characterClass == 6 or characterClass == 10:
  hitPoints = hitPoints + 8
elif characterClass == 2:
  hitPoints = hitPoints + 12
elif characterClass == 4 or characterClass == 7 or characterClass == 8 or characterClass == 9:
  hitPoints = hitPoints + 10
else:
  hitPoints = hitPoints + 6

logging.debug('hitPoints == ' + str(hitPoints))
  
#Character Sheet
print()
print()
print()
print("Character Sheet")
print("Character Name: " + characterName + "  Age: " + characterAge + "  Gender: " + characterGender)
if ancestry == 1:
  print("Ancestry: Dwarf")
elif ancestry == 2:
  print("Ancestry: Elf")
elif ancestry == 3:
  print("Ancestry: Gnome")
elif ancestry == 4:
  print("Ancestry: Goblin")
elif ancestry == 5:
  print("Ancestry: Halfling")
else:
  print("Ancestry: Human")

if characterClass == 1:
  print("Class: Alchemist")
elif characterClass == 2:
  print("Class: Barbarian")
elif characterClass == 3:
  print("Class: Bard")
elif characterClass == 4:
  print("Class: Champion")
elif characterClass == 5:
  print("Class: Cleric")
elif characterClass == 6:
  print("Class: Druid")
elif characterClass == 7:
  print("Class: Fighter")
elif characterClass == 8:
  print("Class: Monk")
elif characterClass == 9:
  print("Class: Ranger")
elif characterClass == 10:
  print("Class: Rogue")
elif characterClass == 11:
  print("Class: Sorcerer")
else:
  print("Class: Wizard")

print("Level: 1  XP: 0")

if lawfulOrChaotic == 1 and goodOrEvil == 1:
  print("Alignment: Lawful Good")
elif lawfulOrChaotic == 1 and goodOrEvil == 2:
  print("Alignment: Lawful Neutral")
elif lawfulOrChaotic == 1 and goodOrEvil == 3:
  print("Alignment: Lawful Evil")
elif lawfulOrChaotic == 2 and goodOrEvil == 1:
  print("Alignment: Neutral Good")
elif lawfulOrChaotic == 2 and goodOrEvil == 2:
  print("Alignment: Neutral")
elif lawfulOrChaotic == 2 and goodOrEvil == 3:
  print("Alignment: Neutral Evil")
elif lawfulOrChaotic == 3 and goodOrEvil == 1:
  print("Alignment: Chaotic Good")
elif lawfulOrChaotic == 3 and goodOrEvil == 2:
  print("Alignment: Chaotic Neutral")
elif lawfulOrChaotic == 3 and goodOrEvil == 3:
  print("Alignment: Chaotic Evil")
  
print("Strength  Score: " + str(statList[0]) + " Modifier: " + str(modifierList[0]))
print("Dexterity  Score: " + str(statList[1]) + " Modifier: " + str(modifierList[1]))
print("Constitution  Score: " + str(statList[2]) + " Modifier: " + str(modifierList[2]))
print("Intelligence  Score: " + str(statList[3]) + " Modifier: " + str(modifierList[3]))
print("Wisdom  Score: " + str(statList[4]) + " Modifier: " + str(modifierList[4]))
print("Charisma  Score: " + str(statList[5]) + " Modifier: " + str(modifierList[5]))

#Skills
print("Skills: ", end = ' ')
#Alchemist
if characterClass == 1:
  del skillList[3]
  skillCombination = randomSelection(3+modifierList[3], skillList)
  skillCombination.append('Crafting')
  print(*skillCombination, sep = ", ")
#Barbarian
elif characterClass == 2:
  del skillList[2]
  skillCombination = randomSelection(3+modifierList[3], skillList)
  skillCombination.append('Athletics')
  print(*skillCombination, sep = ", ")
#Bard
elif characterClass == 3:
  del skillList[10]
  del skillList[10]
  skillCombination = randomSelection(3+modifierList[3], skillList)
  skillCombination.append('Occultism')
  skillCombination.append('Performance')
  print(*skillCombination, sep = ", ")
#Champion and Cleric
elif characterClass == 4 or characterClass == 5:
  del skillList[12]
  skillCombination = randomSelection(2+modifierList[3], skillList)
  skillCombination.append('Religion')
  print(*skillCombination, sep = ", ")
#Druid
elif characterClass == 6:
  del skillList[9]
  skillCombination = randomSelection(2+modifierList[3], skillList)
  skillCombination.append('Nature')
  print(*skillCombination, sep = ", ")
#Fighter
elif characterClass == 7:
  acrobaticsOrAthletics = random.randint(0,1)
  if acrobaticsOrAthletics == 0:
    print('Acrobatics - Expert')
    del skillList[0]
    skillCombination = randomSelection(3+modifierList[3], skillList)
    print(*skillCombination, sep = ", ")
  else:
    print('Athletics - Expert')
    del skillList[2]
    skillCombination = randomSelection(3+modifierList[3], skillList)
    print(*skillCombination, sep = ", ")
#Monk
elif characterClass == 8:
  skillCombination = randomSelection(4+modifierList[3], skillList)
  print(*skillCombination, sep = ", ")
#Ranger
elif characterClass == 9:
  del skillList[9]
  del skillList[14]
  skillCombination = randomSelection(4+modifierList[3], skillList)
  skillCombination.append('Nature')
  skillCombination.append('Survival')
  print(*skillCombination, sep = ", ")
#Rogue
elif characterClass == 10:
  del skillList[14]
  skillCombination = randomSelection(7+modifierList[3], skillList)
  skillCombination.append('Stealth')
  print(*skillCombination, sep = ", ")
#Sorcerer
elif characterClass == 11:
  skillCombination = randomSelection(2+modifierList[3], skillList)
  print(*skillCombination, sep = ", ")
#Wizard
else:
  del skillList[1]
  skillCombination = randomSelection(2+modifierList[3], skillList)
  skillCombination.append('Arcana')
  print(*skillCombination, sep = ", ")
  
#Cantrips
print("Cantrips:", end = ' ')
#Bard
if characterClass == 3:
  cantripCombination = randomSelection(5, occultCantrips)
  print(*cantripCombination, sep = ", ")
#Cleric
elif characterClass == 5:
  cantripCombination = randomSelection(5, divineCantrips)
  print(*cantripCombination, sep = ", ")
#Druid
elif characterClass == 6:
  cantripCombination = randomSelection(5, primalCantrips)
  print(*cantripCombination, sep = ", ")
#Sorcerer
elif characterClass == 11:
  allCantrips = occultCantrips + divineCantrips + primalCantrips + arcaneCantrips
  allCantrips = list(dict.fromkeys(allCantrips))
  cantripCombination = randomSelection(5, allCantrips)
  print(*cantripCombination, sep = ", ")
#Wizard
elif characterClass == 12:
  cantripCombination = randomSelection(5, arcaneCantrips)
  print(*cantripCombination, sep = ", ")
#Other
else:
  print('none')

#Spells
print("1st-level Spells:", end = ' ')
#Bard
if characterClass == 3:
  spellCombination = randomSelection(2, occultSpells)
  print(*spellCombination, sep = ", ")
#Cleric
elif characterClass == 5:
  spellCombination = randomSelection(2, divineSpells)
  print(*spellCombination, sep = ", ")
#Druid
elif characterClass == 6:
  spellCombination = randomSelection(2, primalSpells)
  print(*spellCombination, sep = ", ")
#Sorcerer
elif characterClass == 11:
  allSpells = occultSpells + divineSpells + primalSpells + arcaneSpells
  allSpells = list(dict.fromkeys(allSpells))
  spellCombination = randomSelection(3, allSpells)
  print(*spellCombination, sep = ", ")
#Wizard
elif characterClass == 12:
  spellCombination = randomSelection(2, arcaneSpells)
  print(*spellCombination, sep = ", ")
else:
  print('none')

#Equipment
print("Equipment:")
#Alchemist
if characterClass == 1:
  print("Armour: Studded Leather Armour")
  print("Weapons: Dagger, Sling, Sling Bullet *20")
  print("Gear: Adventurer's Pack, Alchemist's Tools, Bandolier, Basic Crafter's Book, Set of Caltrops *2, Sheath, Repair Kit")
  print("Wealth: 3gp, 4sp")
#Barbarian
elif characterClass == 2:
  print("Armour: Hide Armour")
  print("Weapons: Javelin *4, Greataxe *2")
  print("Gear: Adventurer's Pack, Grappling Hook, Sheath *2")
  print("Wealth: 9gp, 8sp")
#Bard
elif characterClass == 3:
  print("Armour: Studded Leather Armour")
  print("Weapons: Dagger, Rapier, Sling, Sling Bullet *20")
  print("Gear: Adventurer's Pack, Bandolier, Handheld Instrument, Sheath")
  print("Wealth: 8gp, 2sp")
#Champion
elif characterClass == 4:
  print("Armour: Hide Armour")
  print("Weapons: Javelin *4, Dagger")
  print("Gear: Adventurer's Pack, Grappling Hook, Sheath, Crowbar")
  print("Wealth: 11gp, 2sp")
#Cleric
elif characterClass == 5:
  print("Armour: Hide Armour")
  print("Gear: Adventurer's Pack, Bandolier, Set of Caltrops *2, Religious Symbol (Wooden)")
  print("Wealth: 11gp")
#Druid
elif characterClass == 6:
  print("Armour: Leather Armour")
  print("Weapons: Javelin *4, Longspear")
  print("Gear: Adventurer's Pack, Bandolier, Holly and Mistletoe, Healer's Tools")
  print("Wealth: 6gp, 3sp")
#Fighter
elif characterClass == 7:
  print("Armour: Hide Armour")
  print("Weapons: Dagger, Longsword, Steel Shield")
  print("Gear: Adventurer's Pack, Grappling Hook, Sheath")
  print("Wealth: 9gp")
#Monk
elif characterClass == 8:
  print("Weapons: Longspear, Staff")
  print("Gear: Adventurer's Pack, Grappling Hook, Bandolier, Climbing Kit, Lesser Smokestick")
  print("Wealth: 10gp, 2sp")
#Ranger
elif characterClass == 9:
  print("Armour: Leather Armour")
  print("Weapons: Longbow, Arrow *20")
  print("Gear: Adventurer's Pack, Sheath")
  print("Wealth: 5gp, 9sp")
#Rogue
elif characterClass == 10:
  print("Armour: Leather Armour")
  print("Weapons: Dagger, Rapier")
  print("Gear: Adventurer's Pack, Climbing Kit, Sheath, Thieves' Tools")
  print("Wealth: 6gp, 6sp")
#Sorcerer
elif characterClass == 11:
  print("Weapons: Dagger, Slingshot, Sling Bullet *20")
  print("Gear: Adventurer's Pack, Bandolier, Set of Caltrops *2, Sheath")
  print("Wealth: 12gp, 9sp")
#Wizard
elif characterClass == 12:
  print("Weapons: Staff, Crossbow, Bolt *20")
  print("Gear: Adventurer's Pack, Material Component Pouch, Writing Set")
  print("Wealth: 8gp, 6sp")
  
logging.debug('End of program')
