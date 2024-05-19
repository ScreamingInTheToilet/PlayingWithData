import json
# An import statement imporing Json, a lightweight data interchange format.

# This is a variable called item_record. We need it so we can keep track of pieces of data that we want to add or count.
item_record = ['Fire 🔥', 
        'Coin 🪙', 
        'Toolkit🔧',
        'Weapon ⚔️',
        'Map 🗺️'
       ] #item data

# A with statement that uses Json to read a dictionary from the Data.json file. This statement is required for the define function datacount() to work.
with open(r'C:/Users/dell/OneDrive - Nord Anglia Education/AnhKhoaProgramming/PlayingWithData/Data.py', 'r') as f:
  data = json.load(f)
  
# Define function that counts a person's inventory
def datacount(person):
  for item in data["people"]:
    name = item["name"]
    bag = item["bag"]
    info = [{"person":name, "inv":bag}]
    if name == person:
      for x in info:
        person = x["person"]
        inv = x["inv"]
        for i in item_record:
          counter = inv.count(i)
          if counter == 0:
            continue
          else:
            print(f'{counter}:{i}')


# A define function that adds data into a person's inventory. add_data(person, item_add, amount)
def add_data(person, item_add, amount):
  amount = int(amount)
  for item in data["people"]:
    name = item["name"]
    bag = item["bag"]
    info = [{"person":name, "inv":bag}]
    if name == person:
      for x in info:
        person = x["person"]
        inv = x["inv"]
        for i in item_record:
          if item_add == i:
            for e in range(amount):
              inv.append(i)
              
# This define function named 'pop' clears data inside a list.
def pop():
  inv.pop()

# A define function to remove all data inside the person's inventory.
def clear_data(person):
  global inv
  for item in data["people"]:
    name = item["name"]
    bag = item["bag"]
    info = [{"person":name, "inv":bag}]
    if name == person:
      for x in info:
        person = x["person"]
        inv = x["inv"]
        for i in inv:
          pop()

# Use define functions in this area here :).


        
add_data('Samuel', 'Fire 🔥', 3)


# A with statement to update/dump data into the dictionary. This is a required statement for define functions like add_data(), and clear_data() to work.
with open('Data.json', 'w') as f:
  json.dump(data, f)






  
    

      
      



