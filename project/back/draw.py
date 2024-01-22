from matplotlib import pyplot as plt


# Данные для графика вводить напрямую в функции
def print_demand_image():
    d = {2003: 25, 2004: 64, 2005: 247, 2006: 617, 2007: 912, 2008: 1225, 2009: 924, 2010: 1569, 2011: 2404, 2012: 3241, 2013: 4765, 2014: 4073, 2015: 3918, 2016: 4659, 2017: 5474, 2018: 6387, 2019: 5862, 2020: 6173, 2021: 8042, 2022: 7861, 2023: 6758}

    lists = d.items()

    x, y = zip(*lists)

    plt.figure(figsize=(12, 6))
    plt.bar(x, y)
    plt.title("Динамика количества вакансий по годам для выбранной профессии")
    plt.xlabel("Год")
    plt.xticks(x)
    plt.ylabel("Количество вакансий")
    plt.grid()
    plt.savefig('graphics/demand_4.png')


def print_geography_image_salary():
    d = {}

    plt.figure(figsize=(12, 6))
    plt.barh(list(d.keys()), list(d.values()))
    plt.title("Уровень зарплат по городам для выбранной профессии")
    plt.xlabel("Уровень зарплат")
    plt.grid(True, axis='x')
    plt.gca().invert_yaxis()
    plt.savefig('graphics/geography_3.png')


def print_geography_image_vacancy():
    d = {}

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'darkgreen',
              'yellow', 'grey', 'violet', 'magenta', 'cyan', "darkred", "green", "pink", "red", "darkblue"]

    plt.figure(figsize=(10, 5))
    plt.pie(list(d.values()), colors=colors)
    plt.legend(d.keys(), bbox_to_anchor=(-0.1, 1.))
    plt.title("Доля вакансий по городам для выбранной профессии")
    plt.savefig('graphics/geography_4.png')


def print_skills_image():
    d = {}

    for year in d:
        x = d[year][0]
        y = d[year][1]

        plt.figure(figsize=(20, 6))
        plt.barh(x, y)
        plt.title(f"ТОП-20 навыков за {year}")
        plt.xlabel("Частотность")
        plt.grid(True, axis='x')
        plt.gca().invert_yaxis()
        plt.savefig(f'graphics/skills_prof_{year}.png')


print_demand_image()