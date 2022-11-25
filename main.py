import math
from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

#Interfejsy
class IVector(ABC):
    @abstractmethod
    def getComponents(self):
        pass

    @abstractmethod
    def abs(self):
        pass

    @abstractmethod
    def cdot(self):
        pass

class IPolar2D(ABC):
    @abstractmethod
    def getAngle(self):
        pass

    @abstractmethod
    def abs(self):
        pass

#Klasy
class Vector2D(IVector):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def getComponents(self):
        array = np.array
        array.add(self.x)
        array.add(self.y)
        return array

    def abs(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def cdot(self, param):
        return self.x * self.y + param.getComponents()[0] * param.getComponents()[1]

class Polar2DAdapter(IPolar2D, IVector):
    def __init__(self):
        super().__init__()
        srcVector = IVector()

    def abs(self):
        return srcVector