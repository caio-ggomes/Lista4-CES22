from __future__ import annotations
from abc import ABC, abstractmethod

# Classe de abstração veículo mais geral

class Vehicle(ABC):

    def __init__(self, engine: Engine) -> None:
        self.engine = engine
    
    def get_engine(self) -> Engine:
        return self.engine

    @abstractmethod
    def get_vehicleType(self) -> str:
        pass

# Classes refinadas da abstração veículo, sendo especificado o seu tipo

class Car(Vehicle):
    def get_vehicleType(self) -> str:
        return "Car"

class Truck(Vehicle):
    def get_vehicleType(self) -> str:
        return "Truck"

class Bus(Vehicle):
    def get_vehicleType(self) -> str:
        return "Bus"

# Implementação do Motor, que está em ponte com a classe mais abstrata Veículo

class Engine(ABC):

    @abstractmethod
    def get_motorization(self) -> str:
        pass

# Implementações concretas dos Motores, especificando seus tipos

class ElectricEngine(Engine):
    def get_motorization(self) -> str:
        return "Electric"

class HibridEngine(Engine):
    def get_motorization(self) -> str:
        return "Hibrid"

class CombustionEngine(Engine):
    def get_motorization(self) -> str:
        return "Combustion"

# Testes

if __name__ == "__main__":
    Car1 = Car(CombustionEngine())
    Car2 = Car(HibridEngine())
    Truck1 = Truck(CombustionEngine())
    print(Car1.get_vehicleType())
    print(Truck1.get_engine().get_motorization())