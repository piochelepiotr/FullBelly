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

def recipes_with_starchies(recipes,starchies):
    """returns all the recipes that have some of the starchies"""
    L_recipes = list(recipes)
    L_nums = []
    for recipe in recipes:
        for starchy in starchies:
            if recipes[recipe].has_starchy(starchy):
                L_nums.append(L_recipes.index(recipe))
                break
    return L_nums
