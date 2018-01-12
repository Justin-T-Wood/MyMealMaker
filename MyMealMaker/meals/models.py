from django.db import models

class Recipe(models.Model):
    meal_id = models.IntegerField()
    name = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    last_made = models.DateTimeField('date published')
    def __str__(self):
        return self.name



class Ingredient(models.Model):
    meal_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Direction(models.Model):
    meal_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    direction = models.CharField(max_length=1100)
    def __str__(self):
        return self.direction

