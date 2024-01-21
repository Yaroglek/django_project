from matplotlib import pyplot as plt


def print_demand_image():
    # Словарь, который надо отрисовать. Все словари в results.txt
    d = {2003: 25, 2004: 64, 2005: 247, 2006: 617, 2007: 912, 2008: 1225, 2009: 924, 2010: 1569, 2011: 2404, 2012: 3241,
         2013: 4765, 2014: 4073, 2015: 3918, 2016: 4659, 2017: 5474, 2018: 6387, 2019: 5862, 2020: 6173, 2021: 8042,
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
    plt.savefig('graphics/demand_4.png')


def print_geography_image_salary():
    # Словарь, который надо отрисовать. Все словари в results.txt
    d = {'Астана': 190653, 'Сочи': 176914, 'Нур-Султан': 169609, 'Ульяновск': 138426, 'Киев': 138256, 'Хабаровск': 133831,
     'Москва': 131880, 'Краснодар': 130870, 'Калининград': 120414, 'Тюмень': 115972, 'Владивосток': 115403,
     'Екатеринбург': 112964, 'Харьков': 112249, 'Санкт-Петербург': 112148, 'Уфа': 112001, 'Другие': 90356}

    plt.figure(figsize=(12, 6))
    plt.barh(list(d.keys()), list(d.values()))
    plt.title("Уровень зарплат по городам для выбранной профессии")
    plt.xlabel("Уровень зарплат")
    plt.grid(True, axis='x')
    plt.gca().invert_yaxis()
    plt.savefig('graphics/geography_3.png')


def print_geography_image_vacancy():
    # Словарь, который надо отрисовать. Все словари в results.txt
    d = {'Москва': 0.3420345744680851, 'Санкт-Петербург': 0.1672473404255319, 'Минск': 0.05158244680851064,
     'Новосибирск': 0.040372340425531915, 'Нижний Новгород': 0.03738031914893617, 'Киев': 0.03730053191489362,
     'Воронеж': 0.026289893617021276, 'Казань': 0.019906914893617022, 'Екатеринбург': 0.017247340425531915,
     'Томск': 0.013882978723404256, 'Ростов-на-Дону': 0.012553191489361702, 'Самара': 0.008816489361702127,
     'Краснодар': 0.00726063829787234, 'Пермь': 0.007047872340425532, 'Тверь': 0.006635638297872341,
     'Другие': 0.20444148936170203}

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'darkgreen',
              'yellow', 'grey', 'violet', 'magenta', 'cyan', "darkred", "green", "pink", "red", "darkblue"]

    plt.figure(figsize=(10, 5))
    plt.pie(list(d.values()), colors=colors)
    plt.legend(d.keys(), bbox_to_anchor=(-0.1, 1.))
    plt.title("Доля вакансий по городам для выбранной профессии")
    plt.savefig('graphics/geography_4.png')


def print_skills_image():
    d = {2015: (['C++', 'STL', 'Design Patterns', 'Linux', 'C/C++', 'ООП', 'best-practices', 'Git', 'Qt', 'Boost', 'Python', 'SVN', 'MS Visual Studio', 'JavaScript', 'Java', 'SQL', 'TCP/IP', 'C#', 'Unit Testing', 'С++11'], [435, 217, 143, 124, 97, 88, 73, 69, 64, 56, 45, 43, 34, 30, 29, 29, 24, 23, 23, 21]), 2016: (['C++', 'Linux', 'C/C++', 'ООП', 'Qt', 'Git', 'STL', 'Boost', 'SQL', 'Python', 'C#', 'Java', 'SVN', 'MS Visual Studio', 'Unreal Engine 4', 'TCP/IP', 'JavaScript', 'OpenGL', 'MySQL', 'PostgreSQL'], [1055, 480, 379, 332, 291, 274, 224, 155, 155, 133, 125, 100, 87, 80, 77, 74, 72, 64, 59, 55]), 2017: (['C++', 'Linux', 'C/C++', 'Qt', 'Git', 'ООП', 'STL', 'Boost', 'SQL', 'Python', 'C#', 'MS Visual Studio', 'TCP/IP', 'SVN', 'Java', 'OpenGL', 'PostgreSQL', 'С++', 'JavaScript', 'Android'], [1534, 701, 639, 445, 432, 431, 369, 225, 211, 183, 181, 151, 138, 123, 112, 108, 101, 93, 82, 80]), 2018: (['C++', 'Linux', 'C/C++', 'Git', 'Qt', 'ООП', 'STL', 'Python', 'Boost', 'SQL', 'C#', 'MS Visual Studio', 'Java', 'PostgreSQL', 'JavaScript', 'TCP/IP', 'MySQL', 'SVN', 'Английский язык', 'OpenGL'], [2367, 969, 870, 684, 639, 593, 550, 390, 328, 320, 300, 190, 188, 184, 180, 157, 152, 147, 122, 108]), 2019: (['C++', 'Linux', 'C/C++', 'Git', 'Qt', 'ООП', 'STL', 'Python', 'SQL', 'Boost', 'C#', 'MS Visual Studio', 'TCP/IP', 'PostgreSQL', 'Английский язык', 'Java', 'OpenGL', 'SVN', 'MySQL', 'JavaScript'], [2631, 1190, 890, 755, 697, 570, 548, 500, 342, 262, 217, 217, 206, 154, 146, 142, 134, 131, 112, 107]), 2020: (['C++', 'Linux', 'Qt', 'Git', 'C/C++', 'ООП', 'STL', 'Python', 'SQL', 'Английский язык', 'TCP/IP', 'MS Visual Studio', 'PostgreSQL', 'Boost', 'C#', 'Android', 'Java', 'SVN', 'Разработка ПО', 'OpenGL'], [3823, 1953, 1128, 1103, 1095, 984, 811, 669, 472, 448, 348, 285, 273, 257, 243, 202, 186, 177, 166, 125]), 2021: (['C++', 'Linux', 'Git', 'C/C++', 'ООП', 'Qt', 'Python', 'STL', 'Английский язык', 'SQL', 'C#', 'MS Visual Studio', 'PostgreSQL', 'Boost', 'TCP/IP', 'Java', 'Game Programming', 'MySQL', 'Android', 'Разработка ПО'], [5241, 2708, 1801, 1797, 1551, 1391, 1239, 1092, 955, 597, 451, 384, 331, 329, 323, 298, 273, 215, 206, 202]), 2022: (['C++', 'Linux', 'C/C++', 'Git', 'ООП', 'Qt', 'Python', 'Английский язык', 'STL', 'SQL', 'Boost', 'C#', 'MS Visual Studio', 'PostgreSQL', 'Game Programming', 'Java', 'TCP/IP', 'Bash', 'С++', 'Разработка ПО'], [4920, 2931, 2340, 1847, 1711, 1382, 1172, 1134, 1105, 734, 456, 400, 393, 392, 333, 325, 312, 256, 229, 203]), 2023: (['C++', 'Linux', 'C/C++', 'Git', 'Qt', 'STL', 'ООП', 'Python', 'Boost', 'SQL', 'PostgreSQL', 'Английский язык', 'TCP/IP', 'MS Visual Studio', 'CMake', 'Bash', 'Разработка ПО', 'С++', 'Multithread Programming', 'C#'], [3964, 2439, 1629, 1378, 1167, 989, 880, 863, 618, 540, 432, 395, 342, 254, 231, 228, 201, 200, 174, 170])}

    for year in d:
        x = d[year][0]
        y = d[year][1]

        plt.figure(figsize=(20, 6))
        plt.barh(x, y)
        plt.title(f"ТОП-20 навыков за {year} для выбранной профессии")
        plt.xlabel("Частотность")
        plt.grid(True, axis='x')
        plt.gca().invert_yaxis()
        plt.savefig(f'graphics/skills_prof_{year}.png')


print_skills_image()