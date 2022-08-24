from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort, price):
        self.price = price
        self.comfort = comfort
