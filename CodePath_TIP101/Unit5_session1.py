#Problem 1 and 2 and 3
class Pokemon:
  def __init__(self, name, types,evolution=None):
      self.name = name
      self.types = types
      self.is_caught = False
      self.evolution = evolution 

  def print_pokemon(self):
    print({
        "name": self.name,   # Output: "name": "Squirtle",
        "types": self.types, # Output: "types": ["Water"],
        "is_caught": self.is_caught # Output: "is_caught": False
    })

  def catch(self):
    self.is_caught = True

  def choose(self):
    if self.is_caught:
      print(f"{self.name} I choose you! ")
    else: 
      print(f"{self.name} is wild. Catch them if you can!")

  def add_type(self, new_type):
    self.types.append(new_type)








# pikatchu = Pokemon("Pikatchu", ["Electric"])
# squirtle = Pokemon("Squirtle", ["Water"], )
# squirtle.is_caught = True
# squirtle.print_pokemon()

#Problem 4

# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()

#Problem 5
# my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.choose()
# my_pokemon.catch()
# my_pokemon.choose()

#Problem 6
# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()

#Problem 7

# def get_by_type(my_pokemon, pokemon_type):
#   typeNames = []
#   for i in range(len(my_pokemon)):
#     types = my_pokemon[i].types

#     for j in range(len(types)):
#       if types[j] == pokemon_type:
#         typeNames.append( my_pokemon[i].name)

#   return typeNames




# # initializing pokemons
# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Ground")
# print(normal_pokemon)

#Problem 8
# def get_evolutionary_line(starter_pokemon):
#   evolutionary_line = []

#   while starter_pokemon is not None:
#     evolutionary_line.append(starter_pokemon.name)
#     starter_pokemon = starter_pokemon.evolution

#   return evolutionary_line

# charizard = Pokemon("Charizard", ["fire", "flying"])
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)