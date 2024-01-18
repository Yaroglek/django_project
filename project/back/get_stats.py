import pandas as pd
from api import get_currency_in_rur


def get_prepared_df(data: pd.DataFrame):
    data.fillna(0)
    data['salary'] = (data['salary_from'] + data['salary_to']) / 2
    data['salary'] = data.apply(lambda row: row['salary'] * get_currency_in_rur(row["salary_currency"], row["published_at"]), axis=1)
    data["published_year"] = pd.to_datetime(data["published_at"]).dt.year
    return data


def print_dynamics(data):
    salaries_dynamics = data.groupby('published_year')['salary'].mean().astype(int)
    vacancies_dynamics = data['published_year'].value_counts().sort_index().astype(int)

    # Оставляем вакансии с нужным именем
    data_prof = data[data['name'].str.contains(profession_name, case=False, na=False)]
    prof_salaries_dynamics = data_prof.groupby('published_year')['salary'].mean().astype(int)
    prof_salaries_dynamics = prof_salaries_dynamics.reindex(range(2017, 2024), fill_value=0)

    prof_vacancies_dynamics = data_prof['published_year'].value_counts().sort_index().astype(int)
    prof_vacancies_dynamics = prof_vacancies_dynamics.reindex(range(2017, 2024), fill_value=0)


    # Отсекаем города
    total_vacancies = data_prof.shape[0]
    min_vacancies_threshold = total_vacancies * 0.01
    filtered_cities = data_prof['area_name'].value_counts()
    filtered_cities = filtered_cities[filtered_cities >= min_vacancies_threshold]

    top_prof_salaries_by_area = data_prof.groupby('area_name')['salary'].mean().astype(int)
    top_prof_salaries_by_area = top_prof_salaries_by_area[
        top_prof_salaries_by_area.index.isin(filtered_cities.index)].nlargest(10)

    top_prof_vacancy_by_area = data_prof['area_name'].value_counts(normalize=True)
    top_prof_vacancy_by_area = top_prof_vacancy_by_area[
        top_prof_vacancy_by_area.index.isin(filtered_cities.index)].sort_index().nlargest(10)

    print(f"Динамика уровня зарплат по годам: {salaries_dynamics.to_dict()}")
    print(f"Динамика количества вакансий по годам: {vacancies_dynamics.to_dict()}")
    print(f"Динамика уровня зарплат по годам для выбранной профессии: {prof_salaries_dynamics.to_dict()}")
    print(f"Динамика количества вакансий по годам для выбранной профессии: {prof_vacancies_dynamics.to_dict()}")
    print(
        f"Уровень зарплат по городам для выбранной профессии (в порядке убывания): {top_prof_salaries_by_area.to_dict()}")
    print(
        f"Доля вакансий по городам для выбранной профессии (в порядке убывания): {top_prof_vacancy_by_area.round(4).to_dict()}")


file_name = "C:\\Users\kreml\PycharmProjects\django_project\\ulearn_project\\back\\test.csv"
profession_name = ["c++", "с++"]

df = pd.read_csv(file_name)
df = get_prepared_df(df)
print_dynamics(df)
