from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('starters/',views.starters, name="starters"),
    path('starters/chosen/',views.starter_chosen, name="chosen"),

    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('info/', views.info, name='info'),

    path('explore/', views.explore, name='explore'),
    path('explore/<str:where>/', views.explore, name='explore'),

    path('pokemons/<int:pokemon_id>/', views.pokemon_page, name="pokemon_page"),
    path('pokemons/<int:pokemon_id>/who/', views.who_that_pokemon, name="who"),

    path('pokedex/', views.pokedex, name="pokedex"),


]