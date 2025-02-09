from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)  # <--- Добавлено request.FILES
        if form.is_valid():
            form.save()
            return redirect('show_films')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

def show_films(request):
    films = Film.objects.all()
    return render(request, 'films/show_films.html', {'films': films})
