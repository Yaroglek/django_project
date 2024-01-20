from django.shortcuts import render
from .models import *
from back.api import get_latest_vacancies


def main(request):
    return render(request, "main.html")


def demand(request):
    img = Image.objects.all()[len(Image.objects.all()) - 1]
    slovar = {2003: 41304, 2004: 42967, 2005: 44939, 2006: 41317, 2007: 44323, 2008: 48411, 2009: 44811, 2010: 44385, 2011: 46202, 2012: 46972, 2013: 46480, 2014: 48132, 2015: 50389, 2016: 54614, 2017: 59408, 2018: 64052, 2019: 68875, 2020: 71815, 2021: 82056, 2022: 90525, 2023: 97730}

    return render(request, "demand.html", {"graphic": img, "dict": slovar})


def geography(request):
    return render(request, "geography.html")


def skills(request):
    return render(request, "skills.html")


def latest_vacancies(request):
    return render(request, "latest_vacancies.html", {"vacancies": get_latest_vacancies()})
