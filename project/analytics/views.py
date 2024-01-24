import asyncio

from django.shortcuts import render
from .models import *
from back.hh_api import get_latest_vacancies_async


def main(request):
    return render(request, "main.html")


def demand(request):
    all_demands = DemandContent.objects.all()
    return render(request, "demand.html", {"all_demands": all_demands})


def geography(request):
    all_geography = GeographyContent.objects.all()
    return render(request, "geography.html", {"all_geography": all_geography})


def skills(request):
    all_skills = SkillsContent.objects.all()
    return render(request, "skills.html", {"all_skills": all_skills})


def latest_vacancies(request):
    return render(request, "latest_vacancies.html", {"vacancies": asyncio.run(get_latest_vacancies_async())})
