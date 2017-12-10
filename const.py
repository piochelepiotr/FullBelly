#! /usr/bin/python3

import random

recipe_folder = "recipes"
plan_file = "plan.md"
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
starchies = ["pasta","rice","quinoa","patatoes"]

def next_day(day):
    """returns next day"""
    ind = days.index(day)
    return days[(ind+1) % len(days)]

def next_lunch(day,time):
    if time == "evening":
        return next_day(day),"lunch"
    else:
        return day,"evening"

def randint_not_in_L(m,M,L):
    """generates a random number between m and M that is not in L"""
    if (len(L) >= M-m+1):
        print("Impossible to prepare next meal, too much constraints")
        exit(-1)
    while True:
        r = random.randint(m,M)
        if not r in L:
            return r

