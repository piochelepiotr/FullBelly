#! /usr/bin/python3

import os
import const
import manage_recipes

def plan_week(number_meals):
    """This function plans the next number_meals meals,
    it creates a file that will do a resume of the next meals and
    of what you need to buy."""
    manage_recipes.load_recipes()
    txt = ""
    try:
        os.remove(const.plan_file)
    except:
        pass
    with open(const.plan_file,"w") as f:
        f.write(txt)

if __name__ == "__main__":
    plan_week(3)
