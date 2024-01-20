import json
import locale
import re
import requests
from datetime import datetime
import xml.etree.ElementTree as ET


# API HH.ru
def get_latest_vacancies():
    latest_vacancies = []
    url = "https://api.hh.ru/vacancies?text=c%2b%2b&search_field=name&period=1"
    response = requests.get(url, headers={'User-Agent': 'api-test-agent'})

    if response.status_code == 200:
        response = json.loads(response.text)['items']
        vacancies = list(sorted(response, key=lambda x: datetime.fromisoformat(x["published_at"]), reverse=True))[:10]

        # Получить только необходимые поля у каждой вакансии
        for vacancy in vacancies:
            id = vacancy["id"]
            vacancy_url = f"https://api.hh.ru/vacancies/{id}"
            response = requests.get(vacancy_url, headers={'User-Agent': 'api-test-agent'})

            if response.status_code == 200:
                answer = json.loads(response.text)
                fields_needed = {
                    "name": answer["name"],
                    "description": re.sub("<.*?>", "", answer["description"]),
                    "key_skills": get_skills_from_vac([i["name"] for i in answer["key_skills"]]),
                    "company": answer["employer"]["name"],
                    "salary": get_salary_from_hh_vacancy(answer["salary"], answer["published_at"]),
                    "area_name": answer["area"]["name"],
                    "published_at": get_date_from_vac(answer["published_at"]),
                    "url": answer["alternate_url"]
                }
                latest_vacancies.append(fields_needed)

    return latest_vacancies


def get_salary_from_hh_vacancy(salary: dict, published_at: str) -> str:
    if salary is None:
        return "не указана"

    salary_from = salary["from"] if salary["from"] is not None else 0
    salary_to = salary["to"] if salary["to"] is not None else 0
    salary_currency = salary["currency"] if salary["currency"] is not None else "RUR"

    avg_salary = int((salary_from + salary_to) / 2 * get_currency_in_rur(salary_currency, published_at))
    return f"{str(avg_salary)} {salary_currency}"


def get_date_from_vac(published_at: str) -> str:
    date = datetime.fromisoformat(published_at)
    return f"{date.day}.{date.month}.{date.year}"


def get_skills_from_vac(skills: list) -> str:
    if len(skills) == 0:
        return "не указаны"

    skills = ", ".join(skills)
    return skills


# API Центробанка
def get_currency_in_rur(currency: str, published_at: str):
    if currency == "RUR":
        return 1.0

    matcher = re.match(r"^(\d{4})-(\d{2})", published_at)
    year = matcher.group(1)
    month = matcher.group(2)

    if year <= "2016" and month <= "06" and currency == "BYN":
        currency = "BYR"
    if (year == "2016" and month > "06" or year >= "2017") and currency == "BYR":
        currency = "BYN"

    if year not in currencies_by_date:
        currencies_by_date[year] = {
            month: {
                currency: get_multiplier(currency, month, year)
            }
        }

    if month not in currencies_by_date[year]:
        currencies_by_date[year][month] = {
            currency: get_multiplier(currency, month, year)
        }

    if currency not in currencies_by_date[year][month]:
        currencies_by_date[year][month][currency] = get_multiplier(currency, month, year)

    return currencies_by_date[year][month][currency]


def get_multiplier(currency, month, year):
    print(currency, month, year)
    date = f"01/{month}/{year}"
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        valute = root.find(f".//Valute[CharCode='{currency}']")

        if valute is not None:
            locale.setlocale(locale.LC_NUMERIC, 'ru_RU.UTF-8')
            multiplier = locale.atof(valute.find('VunitRate').text)
            return multiplier


currencies_by_date = {}
