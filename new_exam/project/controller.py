from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def create_aquarium_by_type(aquarium_type, name):
        aquarium_dict = {'FreshwaterAquarium': FreshwaterAquarium,
                         'SaltwaterAquarium': SaltwaterAquarium}
        if aquarium_type not in aquarium_dict:
            return False
        return aquarium_dict[aquarium_type](name)

    @staticmethod
    def create_decoration_by_type(decoration_type):
        decoration_dict = {"Plant": Plant,
                           "Ornament": Ornament}
        if not decoration_type in decoration_dict:
            return False
        return decoration_dict[decoration_type]()

    @staticmethod
    def create_fish(fish_type, fish_name, fish_species, price):
        fish_dict = {"SaltwaterFish": SaltwaterFish,
                     "FreshwaterFish": FreshwaterFish}
        if not fish_type in fish_dict:
            return False
        return fish_dict[fish_type](fish_name, fish_species, price)

    def add_aquarium(self, aquarium_type, aquarium_name):
        if not self.create_aquarium_by_type(aquarium_type, aquarium_name):
            return "Invalid aquarium type."
        aquarium = self.create_aquarium_by_type(aquarium_type, aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if not self.create_decoration_by_type(decoration_type):
            return "Invalid decoration type."
        decoration = self.create_decoration_by_type(decoration_type)
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                for decoration in self.decorations_repository.decorations:
                    if decoration.__class__.__name__ == decoration_type:
                        aquarium.add_decoration(decoration)
                        self.decorations_repository.remove(decoration)
                        return f"Successfully added {decoration_type} to {aquarium_name}."

                return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if not self.create_fish(fish_type, fish_name, fish_species, price):
            return f"There isn't a fish of type {fish_type}."
        fish = self.create_fish(fish_type, fish_name, fish_species, price)
        aquarium = ''
        for aquariumm in self.aquariums:
            if aquariumm.name == aquarium_name:
                aquarium = aquariumm
        if len(aquarium.fish) == aquarium.capacity:
            return "Not enough capacity."
        if aquarium.__class__.__name__ == 'FreshwaterAquarium' and fish_type == 'FreshwaterFish':
            return aquarium.add_fish(fish)
        elif aquarium.__class__.__name__ == 'SaltwaterAquarium' and fish_type == 'SaltwaterFish':
            return aquarium.add_fish(fish)
        return "Water not suitable."

    def feed_fish(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.feed()
                return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                total_sum = sum(x.price for x in aquarium.decorations) + sum(x.price for x in aquarium.fish)
                return f"The value of Aquarium {aquarium_name} is {total_sum:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'
        return result.strip()
