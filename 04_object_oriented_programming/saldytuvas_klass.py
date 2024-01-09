class Fridge:
    content = []

    def add_product():
        pass
    
    def remove_product():
        pass


class Product:
    def __init__(self, name: str, quantity: float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"
    

class Recipe:
    ingridiens = []
    instructions = []
    