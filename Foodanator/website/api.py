
import requests
# 200 ok
"""https://www.thecocktaildb.com/api.php
;.
"""


def getCustomMeal(calories, protein, carbs, caffeine, include, exclude):
    results = 1
    #response = "https://api.spoonacular.com/recipes/complexSearch?apiKey=983b9961cc2c423d8afdacedd5f37895&fillIngredients=True&addRecipeInformation=True"
    response = "https://api.spoonacular.com/recipes/complexSearch?apiKey=a87688d55b0d42d5975c72e2afd35492&fillIngredients=True&addRecipeInformation=True"
    #response = "https://api.spoonacular.com/recipes/complexSearch?apiKey=68ba04c3aa7242b995a97d71abf0f511&&fillIngredients=True&addRecipeInformation=True"
    if calories != "":
        response += "&maxCalories="+str(calories)
    if protein != "":
        response += "&minProtein="+str(protein)
    if carbs != "":
        response += "&maxCarbs="+str(carbs)
    if caffeine != "":
        response += "&maxCaffeine="+str(caffeine)
    if include != None and include != "" and include != "undefined":
        response += "&cuisine="+str(include)
    if exclude != None and exclude != "" and exclude != "undefined":
        response += "&excludeCuisine="+str(exclude)
    print(response)
    return requests.get(response).json()
