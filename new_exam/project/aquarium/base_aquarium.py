from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decorations)

    def add_fish(self, fish):

        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if len(self.fish) == 0:
            result += f"Fish: none"
        else:
            result += f"Fish: "
            for fish in self.fish:
                result += f"{fish.name} "
            result = result.strip()
        result += '\n' + f"Decorations: {len(self.decorations)}\n"
        comfort = self.calculate_comfort()
        result += f"Comfort: {comfort}"
        return result.strip()