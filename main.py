import requests

poke = requests.get('https://pokeapi.co/api/v2/pokemon/ditto').json()
print(poke['id'], poke['name'], poke['weight'], poke['height'])


class BasePokemon:
    def __init__(self, name):
        self.name == 'ditto'


class Pokemon(BasePokemon):
    def __init__(self, id, name, height, weight):
        self.id == 132
        self.name == 'ditto'
        self.weight == 40
        self.height == 3
    def __str__(self, id, name, height, weight):
        return f'Pokemon is {self.name}, {self.age}, {self. height}, {self. weight}'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id


    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height


    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight



class PokeAPI(Pokemon):
    def __init__(self, id, name, height, weight, get_full):
        self. id = id
        self. name = name
        self. height = height
        self. weight = weight
        self.get_full  = False

    def get_Pokemon(self, id, get_full):
        return Pokemon

    def get_all(self, get_full):
        yield BasePokemon if get_full == False else print() -> Iterator:

