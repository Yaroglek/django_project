from django.shortcuts import render
from .models import Image
from back.api import get_latest_vacancies


def main(request):
    return render(request, "main.html")


def demand(request):
    img = Image.objects.all()[0]
    return render(request, "demand.html", {"graphic": img})


def geography(request):
    return render(request, "geography.html")


def skills(request):
    return render(request, "skills.html")


def latest_vacancies(request):
    return render(request, "latest_vacancies.html", {"vacancies": get_latest_vacancies()})
