#! /usr/bin/python3

import os
import const

class Recipe:
    """Class that describes a recipe : 
    - the title
    - the ingredients
    - the recipe"""
    def __init__(self,filename):
        """Will initialize a recipe with the file filename"""
        with open(const.recipe_folder + os.sep + filename,"r") as f:
            lines = f.read().split("\n")
            for line in lines:
                print(line)
                print("new line")
