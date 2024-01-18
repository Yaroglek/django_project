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
                    "key_skills": [i["name"] for i in answer["key_skills"]],
                    "company": answer["employer"]["name"],
                    "salary": answer["salary"],
                    "area_name": answer["area"]["name"],
                    "published_at": answer["published_at"]
                }
                latest_vacancies.append(fields_needed)

    return latest_vacancies


# API Центробанка
def get_currency_in_rur(currency: str, published_at: str):
    date = datetime.fromisoformat(published_at)
    date = f"01/0{date.month}/{date.year}"
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        valute = root.find(f".//Valute[CharCode='{currency}']")

        if valute is not None:
            locale.setlocale(locale.LC_NUMERIC, 'ru_RU.UTF-8')
            return locale.atof(valute.find('Value').text)
