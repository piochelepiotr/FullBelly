#! /usr/bin/python3

recipe_folder = "recipes"
plan_file = "plan.md"
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def next_day(day):
    """returns next day"""
    ind = days.index(day)
    return days[(ind+1) % len(days)]

def next_lunch(day,time):
    if time == "evening":
        return next_day(day),"lunch"
    else:
        return day,"evening"
