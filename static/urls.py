from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('liquor/', views.liquor_list, name='liquor'),
    path('cocktail/', views.cocktail_list, name='cocktail'),
    path('bot/', views.bot, name='bot'),
    path('store-locator/', views.store_locator, name='store_locator'),
    path('profile/', views.profile, name='profile'),
]
