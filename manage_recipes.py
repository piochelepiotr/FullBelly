#! /usr/bin/python3

from recipe import Recipe
import const
import os

def load_recipes():
    """Will load all the recipes present in the folder recipes,
    put them in a dict"""
    recipes = {}
    for filename in os.listdir(const.recipe_folder):
        recipe = Recipe(filename)
        recipes[recipe.name] = recipe
    return recipes
