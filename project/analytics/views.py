from django.shortcuts import render
from back.api import get_latest_vacancies


def main(request):
    return render(request, "main.html")


def demand(request):
    return render(request, "demand.html")


def geography(request):
    return render(request, "geography.html")


def skills(request):
    return render(request, "skills.html")


def latest_vacancies(request):
    return render(request, "latest_vacancies.html", {"vacancies": get_latest_vacancies()})
