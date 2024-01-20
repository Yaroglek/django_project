from matplotlib import pyplot as plt


def get_demand_image():
    # Словарь, который надо отрисовать. Все словари в results.txt
    d = {2003: 25, 2004: 64, 2005: 247, 2006: 617, 2007: 912, 2008: 1225, 2009: 924, 2010: 1569, 2011: 2404, 2012: 3241,
         2013: 4765, 2014: 4073, 2015: 3918, 2016: 4659, 2017: 5474, 2018: 6386, 2019: 5862, 2020: 6173, 2021: 8042,
         2022: 7861, 2023: 6758}

    lists = d.items()

    x, y = zip(*lists)

    plt.figure(figsize=(12, 6))
    plt.bar(x, y)
    plt.title("Динамика количества вакансий по годам для выбранной профессии")
    plt.xlabel("Количество вакансий")
    plt.xticks(x)
    plt.ylabel("Год")
    plt.grid()
    plt.savefig('demand_4.png')


def get_geography_image_salary():
    # Словарь, который надо отрисовать. Все словари в results.txt
    d = {'Москва': 131880, 'Краснодар': 130870, 'Киев': 129549, 'Екатеринбург': 112964, 'Санкт-Петербург': 112148,
         'Минск': 110913, 'Казань': 109204, 'Самара': 106359, 'Новосибирск': 106080, 'Нижний Новгород': 99243,
         'Другие': 25044}

    plt.figure(figsize=(12, 6))
    plt.barh(list(d.keys()), list(d.values()))
    plt.title("Уровень зарплат по городам для выбранной профессии")
    plt.xlabel("Уровень зарплат")
    plt.ylabel("Города")
    plt.grid(True, axis='x')
    plt.gca().invert_yaxis()
    plt.savefig('geography_1.png')


def get_geography_image_vacancy():
    # Словарь, который надо отрисовать. Все словари в results.txt
    d = {'Москва': 0.34203912286067634, 'Санкт-Петербург': 0.16724956448888947, 'Минск': 0.05158313275442493,
         'Новосибирск': 0.04037287729890025, 'Нижний Новгород': 0.037380816234258436, 'Киев': 0.037287729890025136,
         'Воронеж': 0.026290243221319433, 'Казань': 0.019907179616750224, 'Екатеринбург': 0.017247569781513053,
         'Ростов-на-Дону': 0.012553358422319446, 'Другие': 0.24808840543092314}

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'darkgreen',
              'yellow', 'grey', 'violet', 'magenta', 'cyan']

    plt.figure(figsize=(10, 5))
    plt.pie(list(d.values()), colors=colors)
    plt.legend(d.keys(), bbox_to_anchor=(-0.1, 1.))
    plt.title("Доля вакансий по городам для выбранной профессии")
    plt.savefig('geography_2.png')
