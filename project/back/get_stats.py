import pandas as pd
from api import get_currency_in_rur


def add_salaries_field(df: pd.DataFrame):
    df = (df.dropna(subset=["salary_currency"])
          .dropna(how="all", subset=["salary_from", "salary_to"]))
    df["salary"] = df[['salary_from', 'salary_to']].mean(axis=1)
    df["salary"] = df.apply(
        lambda row: row["salary"] * get_currency_in_rur(str(row["salary_currency"]), str(row["published_at"])), axis=1)
    df["published_year"] = pd.to_datetime(df["published_at"], utc=True).dt.year
    return df


file_name = "vacancies.csv"
profession_name = r"c\+\+|с\+\+"
data = pd.read_csv(file_name)
data_prof = data[data['name'].str.contains(profession_name, case=False, na=False)]

# Результаты в results.txt
# Страница Востребованность
# Динамика уровня зарплат по годам
salaries_dynamics = add_salaries_field(data).groupby("published_year")["salary"].mean().astype(int).to_dict()
print(salaries_dynamics)
# Динамика количества вакансий по годам
data["published_year"] = pd.to_datetime(data["published_at"], utc=True).dt.year
vacancies_dynamics = data['published_year'].value_counts().sort_index().astype(int).to_dict()
print(vacancies_dynamics)
# Динамика зарплат по годам для выбранной профессии
prof_salaries_dynamics = add_salaries_field(data_prof).groupby("published_year")["salary"].mean().astype(int).to_dict()
print(prof_salaries_dynamics)
# Доля вакансий по годам для выбранной профессии
data_prof["published_year"] = pd.to_datetime(data_prof["published_at"], utc=True).dt.year
prof_vacancies_dynamics = data_prof["published_year"].value_counts().sort_index().astype(int).to_dict()
print(prof_vacancies_dynamics)


# Страница География

