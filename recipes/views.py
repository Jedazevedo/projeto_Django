from django.shortcuts import render
from django.urls import path
from util.recipes.factory import make_recipe
from .models import Recipe
# Create your views here.

def home(request):
     recipes = Recipe.objects.all().order_by('-id')
     return render(request, 'recipes/pages/home.html', context={
          'recipes':recipes,
     })


def recipe(request, id):
     return render(request, 'recipes/pages/recipe-views.html', context={
          'recipe':make_recipe(),
          'is_detail_page': True,
     })