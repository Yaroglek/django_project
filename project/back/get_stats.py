import numpy as np
import pandas as pd
from api import get_currency_in_rur


def prepare_df(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(df[df["salary_currency"] == "GEL"].index)
    df["salary"] = df[['salary_from', 'salary_to']].mean(axis=1)
    df["salary"] = df.apply(
        lambda row: np.nan if (pd.isnull(row["salary_currency"])) else
        row["salary"] * get_currency_in_rur(str(row["salary_currency"]), str(row["published_at"])), axis=1
    )
    df = df.drop(df[df["salary"] >= 3000000.0].index)
    df["published_year"] = pd.to_datetime(df["published_at"], utc=True).dt.year
    return df


def get_top_cities_by_vacancies(cities: dict) -> dict:
    top_cities = dict(list(cities.items())[:10])
    other_cities_sum = 1 - sum(top_cities[city] for city in top_cities)
    top_cities["Другие"] = other_cities_sum
    return top_cities


def get_top_cities_by_salary(cities: dict) -> dict:
    top_cities = dict(list(cities.items())[:10])
    other_cities_sum = sum(cities[item] for item in cities if item not in top_cities) / (len(cities)) - 10
    top_cities["Другие"] = int(other_cities_sum)
    return top_cities


def get_demand_page_content(df: pd.DataFrame):
    # Страница Востребованность
    # Динамика уровня зарплат по годам
    salaries_dynamics = df.groupby("published_year")["salary"].mean().astype(int).to_dict()
    print(salaries_dynamics)

    # Динамика количества вакансий по годам
    vacancies_dynamics = df['published_year'].value_counts().sort_index().astype(int).to_dict()
    print(vacancies_dynamics)

    # Динамика зарплат по годам для выбранной профессии
    data_prof = df[df['name'].str.contains(profession_name, case=False, na=False)]
    prof_salaries_dynamics = data_prof.groupby("published_year")["salary"].mean().astype(int).to_dict()
    print(prof_salaries_dynamics)

    # Доля вакансий по годам для выбранной профессии
    prof_vacancies_dynamics = data_prof["published_year"].value_counts().sort_index().astype(int).to_dict()
    print(prof_vacancies_dynamics)


def get_geography_page_content(df: pd.DataFrame):
    # Страница География
    total_vacancies = df.shape[0]
    min_vacancies_threshold = total_vacancies * 0.01
    filtered_cities = df['area_name'].value_counts()
    filtered_cities = filtered_cities[filtered_cities >= min_vacancies_threshold]

    # Доля вакансий по городам (в порядке убывания)
    vacancies_by_area = df['area_name'].value_counts(normalize=True)
    vacancies_by_area = vacancies_by_area[
        vacancies_by_area.index.isin(filtered_cities.index)].to_dict()
    print(get_top_cities_by_vacancies(vacancies_by_area))

    # Доля вакансий по городам для выбранной профессии (в порядке убывания)
    data_prof = df[df['name'].str.contains(profession_name, case=False, na=False)]
    prof_vacancies_by_area = data_prof['area_name'].value_counts(normalize=True)
    prof_vacancies_by_area = prof_vacancies_by_area[
        prof_vacancies_by_area.index.isin(filtered_cities.index)].to_dict()
    print(get_top_cities_by_vacancies(prof_vacancies_by_area))

    # Уровень зарплат по городам (в порядке убывания)
    df = df.dropna(subset=["salary"])
    salaries_by_area = data.groupby('area_name')['salary'].mean().astype(int)
    salaries_by_area = salaries_by_area[
        salaries_by_area.index.isin(filtered_cities.index)].sort_values(ascending=False).to_dict()
    print(get_top_cities_by_salary(salaries_by_area))

    # Уровень зарплат по городам для выбранной профессии (в порядке убывания)
    data_prof = data[data['name'].str.contains(profession_name, case=False, na=False)]
    prof_salaries_by_area = data_prof.groupby('area_name')['salary'].mean().astype(int)
    prof_salaries_by_area = prof_salaries_by_area[
        prof_salaries_by_area.index.isin(filtered_cities.index)].sort_values(ascending=False).to_dict()
    print(get_top_cities_by_salary(prof_salaries_by_area))


file_name = "vacancies_with_salary.csv"
profession_name = r"c\+\+|с\+\+"
data = pd.read_csv(file_name)

# Подготовка данных из файла для аналитики. Запись обработанного файла в новый, чтобы больше не обращаться к API ЦБ
# data = prepare_df(data)
# data.to_csv("vacancies_with_salary.csv", index=False, encoding='utf-8')

# Результаты в results.txt
get_demand_page_content(data)
get_geography_page_content(data)




