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
        return math.atan(_temp_y / _temp_x)

class Vector3DDecorator(Vector2D):
    def __init__(self, x, y , z = 0):
        super().__init__(x, y)
        self._srcVector = Vector2D(x,y)
        self._z = z
    def abs(self):
        _temp_x = self._srcVector.getComponents()[0]
        _temp_y = self._srcVector.getComponents()[1]
        return math.sqrt(_temp_x * _temp_x + _temp_y * _temp_y + self._z * self._z)

    def cdot(self, param):
        _temp_x = self._srcVector.getComponents()[0]
        _temp_y = self._srcVector.getComponents()[1]
        return _temp_x * param.getComponents()[0] + _temp_y * param.getComponents()[1] + self._z * 0

    def getComponents(self):
        return [self._srcVector.getComponents()[0], self._srcVector.getComponents()[1], self._z]

    def cross(self, param):
        _temp_x = self._srcVector.getComponents()[1] * 0 - self._z * param.getComponents()[1]
        _temp_y = self._srcVector.getComponents()[0] * 0 - self._z * param.getComponents()[0]
        _temp_z = self._srcVector.getComponents()[0] * param.getComponents()[1] - self._srcVector.getComponents()[1] * param.getComponents()[0]
        return Vector3DDecorator(_temp_x, _temp_y, _temp_z)

    def gerSrcV(self):
        return self._srcVector

class Vector3DInheritance(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    def abs(self):

        return math.sqrt(super().getComponents()[0] * super().getComponents()[0] + super().getComponents()[1] * super().getComponents()[1] + self._z * self._z)

    def cdot(self, param):
        return super().getComponents()[0] * param.getComponents()[0] + super().getComponents()[1] * param.getComponents()[1] + self._z * 0

    def getComponents(self):
        return [super().getComponents()[0], super().getComponents()[1], self._z]

    def cross(self, param):
        _temp_x = super().getComponents()[1] * 0 - self._z * param.getComponents()[1]
        _temp_y = super().getComponents()[0] * 0 - self._z * param.getComponents()[0]
        _temp_z = super().getComponents()[0] * param.getComponents()[1] - super().getComponents()[1] * param.getComponents()[0]
        return Vector3DInheritance(_temp_x, _temp_y, _temp_z)

    def gerSrcV(self):
        return self

class _2DPolarInheritance(Vector2D):
    def __init__(self, x, y):
        super().__init__(x, y)

    def getAngle(self):
        return math.atan(super().getComponents()[1] / super().getComponents()[0])

vector2d = _2DPolarInheritance(1, 2)
vector3ddecorator = Vector3DDecorator(1, 2, 3)
vector3dinheritance = Vector3DInheritance(11,10,9)

print("UKŁAD KARTEZJANSKI:")
print("Wektor 2d")
print(f"x: {vector2d.getComponents()[0]}, y: {vector2d.getComponents()[1]}")
print("Wektor 3d inheritance")
print(f"x: {vector3dinheritance.getComponents()[0]}, y: {vector3dinheritance.getComponents()[1]}, z: {vector3dinheritance.getComponents()[2]}")
print("Wektor 3d inheritance")
print(f"x: {vector3ddecorator.getComponents()[0]}, y: {vector3ddecorator.getComponents()[1]}, z: {vector3ddecorator.getComponents()[2]}")

print("\nUKŁAD BIEGUNOWY: ")
print("Wektor 2d ")
print(f"promien wodzacy: {vector2d.abs()}")
print(f"wartosc kata: {vector2d.getAngle()}")

print("\nILOCZYN WEKTOROWY")
tmp_vector3ddecorator = vector3ddecorator.cross(vector2d)
print("Wektor 3d decorator i wektor 2d: ")
print(f"x: {tmp_vector3ddecorator.getComponents()[0]}")
print(f"y: {tmp_vector3ddecorator.getComponents()[1]}")
print(f"z: {tmp_vector3ddecorator.getComponents()[2]}")
tmp_vector3dinheritance = vector3dinheritance.cross(vector2d)
print("Wektor 3d inheritance i wektor 2d: ")
print(f"x: {tmp_vector3dinheritance.getComponents()[0]}")
print(f"y: {tmp_vector3dinheritance.getComponents()[1]}")
print(f"z: {tmp_vector3dinheritance.getComponents()[2]}")

print("\nILOCZYN SKALARNY")
print(f"Wektor 2d z wektorem 2d: {vector2d.cdot(vector2d)}")
print(f"Wektor 3d inheritance z wektorem 2d: {vector3dinheritance.cdot(vector2d)}")
print(f"Wektor 3d decorator z wektorem 2d: {vector3ddecorator.cdot(vector2d)}")
