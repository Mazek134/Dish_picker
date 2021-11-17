from django.shortcuts import render, get_list_or_404
from django.shortcuts import redirect


def home_page (request):
    return render(request, 'Dish/home.html')