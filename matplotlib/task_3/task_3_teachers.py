import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

data = []
teachers = []

with open('students.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        a = str(*row).split(";")
        teacher = a[0]
        group = int(a[1])
        grade = int(a[2])
        strok = [teacher, group, grade]
        data.append(strok)

teachers = sorted(set(item[0] for item in data))
grades = [3, 4, 5, 6, 7, 8, 9, 10]
quantity = np.zeros((len(teachers), len(grades)), dtype=int)

for entry in data:
    teacher = entry[0]
    grade = entry[2]
    teacher_index = teachers.index(teacher)
    quantity[teacher_index][grade - 3] += 1

category_names = list(map(str, grades))
results = {teacher: quantity[i] for i, teacher in enumerate(teachers)}

def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.set_ylabel('Количество студентов')
    ax.set_xlabel('Преподаватели')
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    bottom = np.zeros(len(labels))
    colormap = plt.get_cmap('RdYlGn') # Gradient

    for i, colname in enumerate(category_names):
        color = colormap((i) / (len(category_names) - 1)) # From red to green
        ax.bar(labels, data[:, i], bottom=bottom, label=colname, color=color)
        bottom += data[:, i]

    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    return fig, ax

survey(results, category_names)
plt.title('Оценки по преподавателям', pad=30)
plt.savefig("task3_teachers.png")
plt.show()
