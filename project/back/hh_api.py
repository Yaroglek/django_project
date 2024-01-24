import re
import time
import aiohttp
import asyncio
import dateutil.parser
from back.cb_api import get_currency_in_rur


# API HH.ru
async def get_latest_vacancies_async():
    url = "https://api.hh.ru/vacancies?text=c%2b%2b&search_field=name&period=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={'User-Agent': 'api-test-agent'}) as response:
            if response.status == 200:
                response_json = await response.json()
                vacancies = sorted(response_json['items'], key=lambda x: dateutil.parser.isoparse(x["published_at"]), reverse=True)[:10]

                tasks = [get_vacancy_details(session, vacancy["id"]) for vacancy in vacancies]
                results = await asyncio.gather(*tasks)

                latest_vacancies = [vacancy for vacancy in results if vacancy is not None]
                return latest_vacancies
            else:
                return []


async def get_vacancy_details(session, vacancy_id):
    async with session.get(f'https://api.hh.ru/vacancies/{vacancy_id}', headers={'User-Agent': 'api-test-agent'}) as response:
        if response.status == 200:
            answer = await response.json()
            fields_needed = {
                "name": answer["name"],
                "description": re.sub("<.*?>", "", answer["description"])[:500] + "...",
                "key_skills": get_skills_from_vac([i["name"] for i in answer["key_skills"]]),
                "company": answer["employer"]["name"],
                "salary": get_salary_from_hh_vacancy(answer["salary"], answer["published_at"]),
                "area_name": answer["area"]["name"],
                "published_at": get_date_from_vac(answer["published_at"]),
                "url": answer["alternate_url"]
            }
            return fields_needed
        else:
            return None


def get_salary_from_hh_vacancy(salary: dict, published_at: str) -> str:
    if salary is None:
        return "не указана"

    salary_from = salary["from"] if salary["from"] is not None else 0
    salary_to = salary["to"] if salary["to"] is not None else 0
    salary_currency = salary["currency"] if salary["currency"] is not None else "RUR"

    avg_salary = int((salary_from + salary_to) / 2 * get_currency_in_rur(salary_currency, published_at))
    return f"{str(avg_salary)} {salary_currency}"


def get_date_from_vac(published_at: str) -> str:
    date = dateutil.parser.isoparse(published_at)
    return f"{date.day}.{date.month}.{date.year}"


def get_skills_from_vac(skills: list) -> str:
    if len(skills) == 0:
        return "не указаны"

    skills = ", ".join(skills)
    return skills