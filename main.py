import math
from abc import ABC, abstractmethod

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
        self._x = x
        self._y = y

    def getComponents(self):
        return [self._x, self._y]

    def abs(self):
        return math.sqrt(self._x * self._x + self._y * self._y)

    def cdot(self, param):
        return self._x * self._y + param.getComponents()[0] * param.getComponents()[1]

class Polar2DAdapter(IPolar2D, IVector):
    def __init__(self, Vector2D):
        self._srcVector = Vector2D

    def abs(self):
        return self._srcVector.abs()

    def cdot(self, param):
        return self._srcVector.cdot(param)

    def getComponents(self):
        return self._srcVector.getComponents()

    def getAngle(self):
        x = self._srcVector.getComponents()[0]
        y = self._srcVector.getComponents()[1]
        return math.degrees(math.atan(y / x))

class Vector3DDecorator(IVector):
    def __init__(self, Vector2D, z = 0):
        self._srcVector = Vector2D
        self._z = z
    def abs(self):
        return self._srcVector.abs()

    def cdot(self, param):
        return self._srcVector.cdot