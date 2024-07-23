### Code:

```
class DreamCake:
    # Measurements are defined in grams or units
    eggs = 4
    sugar = 300
    milk = 200
    butter = 50
    flour = 250
    baking_soda = 20
    vanilla = 10

    topping = None
    garnish = None

    is_baked = False

    def __init__(self, topping='No topping', garnish='No garnish'):
        self.topping = topping
        self.garnish = garnish

    def bake(self):
        self.is_baked = True

    def is_cake_ready(self):
        return self.is_baked
```

_Things to consider in above code for a cake class_

- classes are defined using the class keyword
- "\_\_init\_\_" function is a so-called "Magic Method". This function automatically gets called by Python once a new instance of a class is requested.
- Python is designed to require a "self" parameter in the first position of the function signature so that classe functions get a way to refer to their own variables and functions.
