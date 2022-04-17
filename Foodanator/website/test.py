import random
import requests
# 200 ok
"""https://www.thecocktaildb.com/api.php"""


def getCustomMeal():
    response = requests.get(
        "https://api.spoonacular.com/recipes/complexSearch?apiKey=68ba04c3aa7242b995a97d71abf0f511&&fillIngredients=True&addRecipeInformation=True")
    return response.json()


print(getCustomMeal())
