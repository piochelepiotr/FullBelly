#! /usr/bin/python3

import os
import const
from ingredient import Ingredient

class Recipe:
    """Class that describes a recipe : 
    - the title
    - the ingredients
    - the recipe"""
    def __init__(self,filename):
        """Will initialize a recipe with the file filename"""
        with open(const.recipe_folder + os.sep + filename,"r") as f:
            try:
                self.name = f.readline().strip().replace("#","")
                self.period = f.readline()
                line = f.readline()
                self.ingredients = []
                line = f.readline().replace("#","").replace("*","").strip()
                while line.strip() != "Cooking":
                    ingredient = line.split(":")
                    self.ingredients.append(Ingredient(
                        ingredient[0].strip(),
                        float(ingredient[1].strip()),
                        ingredient[2].strip()))
                    line = f.readline().replace("#","").replace("*","").strip()
                self.recipe = f.read().strip()
            except:
                print(filename," has an error.")
    def __repr__(self):
        """Method to display the recipe in human readable form."""
        s = "{}\n".format(self.name)
        for ing in self.ingredients:
            s += str(ing) + "\n"
        s += self.recipe
        return s
