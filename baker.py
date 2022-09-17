#!/usr/bin/env python
# https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe: dict, available: dict) -> int:
    return int(all(key in available for key in recipe.keys())) and min(
        available[key] // recipe[key] for key in recipe.keys()
    )
