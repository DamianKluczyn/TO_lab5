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
        return self._x * param.getComponents()[0] + self._y * param.getComponents()[1]

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
        _temp_x = self._srcVector.getComponents()[0]
        _temp_y = self._srcVector.getComponents()[1]
        return math.degrees(math.atan(_temp_y / _temp_x))

class Vector3DDecorator(IVector):
    def __init__(self, Vector2D, z = 0):
        self._srcVector = Vector2D
        self._z = z
    def abs(self):
        _temp_x = self._srcVector.getComponents()[0]
        _temp_y = self._srcVector.getComponents()[1]
        return math.sqrt(_temp_x * _temp_x + _temp_y * _temp_y + self._z * self._z)

    def cdot(self, param):
        _temp_x = self._srcVector.getComponents()[0]
        _temp_y = self._srcVector.getComponents()[1]
        return _temp_x * param.getComponents[0] + _temp_y * param.getComponents[1] + self._z * 0

    def getComponents(self):
        return [self._srcVector.getComponents()[0], self._srcVector.getComponents()[1], self._z]

    def cross(self, param):
        _temp_x = self._srcVector.getComponents[1] * 0 - self._z * param.getComponents()[1]
        _temp_y = self._srcVector.getComponents[0] * 0 - self._z * param.getComponents()[0]
        _temp_z = self._srcVector.getComponents()[0] * param.getComponents()[1] - self._srcVector.getComponents()[1] * param.getComponents()[0]
        return Vector3DDecorator(_temp_x, _temp_y, _temp_z)

    def gerSrcV(self):
        return self._srcVector

class Vector3DInheritance(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    def abs(self):

        return math.sqrt(super()._x * super()._x + super()._y * super()._y + self._z * self._z)

    def cdot(self, param):
        return super()._x * param.getComponents[0] + super()._y * param.getComponents[1] + self._z * 0

    def getComponents(self):
        return [super()._x, super()._y, self._z]

    def cross(self, param):
        _temp_x = super()._y * 0 - self._z * param.getComponents()[1]
        _temp_y = super()._x * 0 - self._z * param.getComponents()[0]
        _temp_z = super()._x * param.getComponents()[1] - super()._y * param.getComponents()[0]
        return Vector3DInheritance(_temp_x, _temp_y, _temp_z)

    def gerSrcV(self):
        return self

class _2DPolarInheritance(Vector2D):
    def __init__(self, x, y):
        Vector2D(x, y)

    def getAngle(self):
        return math.sqrt(Vector2D.getComponents()[1] / Vector2D.getComponents()[0])