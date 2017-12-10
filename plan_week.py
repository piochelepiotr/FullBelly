#! /usr/bin/python3

import os
import const
import manage_recipes
import random
import ingredient

def write_plan(txt):
    """Writes the plan in the file"""
    try:
        os.remove(const.plan_file)
    except:
        pass
    with open(const.plan_file,"w") as f:
        f.write(txt)

def generate_meals(recipes,number_meals):
    """Generates all the meals according to some rules :
    - never eat pasta two times in a row for instance"""
    n = len(recipes)
    meals = []
    for i in range(number_meals):
        j = random.randint(0,n-1)
        meals.append(list(recipes)[j])
    return meals

def shopping_list(recipes, meals):
    ingredients = []
    for meal in meals:
        ingredients.extend(recipes[meal].ingredients)
    simplified_list = ingredient.simplify_ingredients(ingredients)
    txt = "# Shopping list\n"
    for ingr in simplified_list:
        txt += "* " + str(ingr) + "\n"
    return txt

def plan_week(number_meals,day,time):
    """This function plans the next number_meals meals,
    it creates a file that will do a resume of the next meals and
    of what you need to buy."""
    recipes = manage_recipes.load_recipes()
    meals = generate_meals(recipes,number_meals)
    txt = ""
    for i in range(number_meals):
        txt += "# " + day + " " + time + "\n"
        txt += meals[i] + "\n"
        day,time = const.next_lunch(day,time)
    txt += "\n" + shopping_list(recipes,meals)
    write_plan(txt)

if __name__ == "__main__":
    plan_week(3,"Friday","lunch")
