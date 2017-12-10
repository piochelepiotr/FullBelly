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
    done_meals = []
    prev_starchies = []
    for i in range(number_meals):
        forbidden_recipes = manage_recipes.recipes_with_starchies(recipes,prev_starchies)
        j = const.randint_not_in_L(0,n-1,list(set(done_meals + forbidden_recipes)))
        meals.append(list(recipes)[j])
        #done_meals.append(j)
        prev_starchies = recipes[list(recipes)[j]].starchies()
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
        txt += meals[i] + "\n\n"
        day,time = const.next_lunch(day,time)
    txt += shopping_list(recipes,meals)
    write_plan(txt)

if __name__ == "__main__":
    plan_week(100,"Friday","lunch")
