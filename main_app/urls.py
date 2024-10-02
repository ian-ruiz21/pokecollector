from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for cats index
  path('pokemon/', views.index, name='cat-index'),
  path('pokemon/<int:poke_id>/', views.poke_detail, name='poke-detail'),
]
