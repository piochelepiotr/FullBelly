#! /usr/bin/python3

class Ingredient:
    """class represents an ingredient,
    - name
    - quantity (float)
    - unit can be g, kg, L, cL, u
    - unit
    """
    def __init__(self,name,quantity,unit):
        """initialize an ingredient"""
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.simplify()

    def simplify(self):
        if self.unit == "g":
            self.unit = "kg"
            self.quantity /= 1000
        elif self.unit == "cL":
            self.unit = "L"
            self.quantity /= 100

    def __repr__(self):
        """Method to display the ingredient in human readable form."""
        return "{} : {}{}".format(self.name,self.quantity,self.unit)

def simplify_ingredients(ingredients):
    """Groups the ingredients by name"""
    ingredients_dict = {}
    for ingredient in ingredients:
        if ingredient.name in ingredients_dict:
            ingredients_dict[ingredient.name].quantity = ingredient.quantity + ingredients_dict[ingredient.name].quantity
        else:
            ingredients_dict[ingredient.name] = Ingredient(ingredient.name,ingredient.quantity,ingredient.unit)
    return [ingredients_dict[name] for name in ingredients_dict]
