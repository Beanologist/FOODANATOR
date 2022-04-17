from flask import Blueprint, render_template, request
from .food import loadRecipie
from .api import getCustomMeal

page = Blueprint('page', __name__, template_folder="templates",
                 static_folder="static")


@page.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        calories = request.form.get("calories")
        protein = request.form.get("protein")
        carbs = request.form.get("carbs")
        caffeine = request.form.get("caffeine")
        results = request.form.get("results")
        include = request.form.get("include")
        exclude = request.form.get("exclude")
        meal = getCustomMeal(calories, protein, carbs,
                             caffeine, include, exclude)
        ingredients = []
        curr = ""
        for i in range(len(meal["results"])):
            for ingred in range(len(meal["results"][i]["missedIngredients"])):
                # split ingredients in list with ;
                curr += meal["results"][i]["missedIngredients"][ingred]['original'] + ";      "
            ingredients.append(curr)
            curr = ""
        curr = ""
        recipie = []

        for i in range(len(meal["results"])):
            if(meal["results"][i]["analyzedInstructions"] != []):
                for j in range(len(meal["results"][i]["analyzedInstructions"][0]["steps"])):
                    curr+= "    "+ str(j+1) + ".    " + meal["results"][i]["analyzedInstructions"][0]["steps"][j]['step']
                recipie.append(curr)
                curr=""
            else:
                recipie.append(" ")


        return render_template("index.html", meal=meal, mealLength=len(meal["results"]), ingredients=ingredients, recipie=recipie)

    else:

        return render_template("index.html", meal=loadRecipie(), mealLength=1, ingredients=[], recipie=[])


"""   """


@ page.route("/thanks")
def thanks():
    return render_template("thanks.html", nuts=";ldlk")
