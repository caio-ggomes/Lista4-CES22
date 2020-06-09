# Pizza ingredients using decorators

class PizzaIngredient:
    cost = None
    def getDescription(self) -> str:
        return self.__class__.__name__
    def getTotalCost(self) -> float:
        return self.__class__.cost

# Pizza Dough, costs nothing

class Dough(PizzaIngredient):
    cost = 0.0

# Decorator implementation

class Decorator(PizzaIngredient):
    def __init__(self, pizzaIngredient):
        self.ingredient = pizzaIngredient
    def getTotalCost(self):
        return self.ingredient.getTotalCost() + PizzaIngredient.getTotalCost(self)
    def getDescription(self):
        return self.ingredient.getDescription() + ' ' + PizzaIngredient.getDescription(self)

# Possible Ingredients

class Tomatoes(Decorator):
    cost = 0.5
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class Olives(Decorator):
    cost = 0.25
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class Onion(Decorator):
    cost = 0.5
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class Mussarela(Decorator):
    cost = 1.0
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class Parmesan(Decorator):
    cost = 0.5
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class Chicken(Decorator):
    cost = 1.5
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class Bacon(Decorator):
    cost = 1.0
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class CreamCheese(Decorator):
    cost = 0.75
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class Pepperoni(Decorator):
    cost = 0.75
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)
class CreamCheeseStuffedEdge(Decorator):
    cost = 1.0
    def __init__(self, pizzaIngredient):
        Decorator.__init__(self, pizzaIngredient)

# Tests

if __name__ == "__main__":
    order1 = CreamCheeseStuffedEdge(Pepperoni(Mussarela(Dough())))
    order2 = CreamCheese(Chicken(Bacon(Olives(Dough()))))
    order3 = CreamCheese(Parmesan(Mussarela(Onion(Tomatoes(Dough())))))
    print(order1.getDescription() + ": $" + str(order1.getTotalCost()))
    print(order2.getDescription() + ": $" + str(order2.getTotalCost()))
    print(order3.getDescription() + ": $" + str(order3.getTotalCost()))