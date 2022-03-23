"""Example of a class and object instantiation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str 
    toppings: int
    extra_chesse: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for intialization of attributes."""
        self.size = size
        self.toppings = toppings
        # implicit return statement here
        
    def price(self, tax: float) -> float:
        """Calculate price of a pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.00
        else:
            total += 8.0
        
        total += self.toppings * 0.75

        if self.extra_chesse is True:
            total += 1.0
        
        total *= tax

        return total


a_pizza: Pizza = Pizza("large", 3)

print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f'Price: ${a_pizza.price(1.05)}')
# .pizza() is a Method call; other method calls include .pop, .append, etc.

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_chesse = True

print(another_pizza.size)
print(f'Price: ${another_pizza.price(1.05)}')