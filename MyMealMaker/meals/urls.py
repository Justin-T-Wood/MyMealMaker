from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:meal_id>/', views.recipe, name='recipe'),
]