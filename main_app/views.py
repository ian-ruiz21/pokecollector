from django.shortcuts import render
from django.http import HttpResponse

class Pokemon:
    def __init__(self, name, type_, description, level):
        self.name = name
        self.type_ = type_
        self.description = description
        self.level = level

pokemon = [
    Pokemon('Pikachu', 'electric', 'Kinda rude.', 3),
    Pokemon('Bulbasaur', 'grass/poison', 'Looks like a turtle.', 0),
    Pokemon('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Pokemon('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon })