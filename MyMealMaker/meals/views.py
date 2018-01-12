from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from meals.models import Recipe


def index(request):
    context = {
        'recipes': Recipe.objects.all(),
    }
    template = loader.get_template('meals/index.html')
    return HttpResponse(template.render(context, request))

def recipe(request, meal_id):
    context = {
        'recipe': Recipe.objects.get(meal_id=meal_id),
    }
    template = loader.get_template('meals/recipe.html')
    return HttpResponse(template.render(context, request))
