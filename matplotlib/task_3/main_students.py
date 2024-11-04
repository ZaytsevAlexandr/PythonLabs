import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

data = []
label = []

with open('students.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        a = str(*row).split(";")
        name = a[0]
        group = int(a[1])
        grade = int(a[2])
        strok = [name, group, grade]
        data.append(strok)

data = sorted(data, key=lambda e: e[1])
current = data[0][1]
label.append(current)
for i in data:
    if current != i[1]:
        current = i[1]
        label.append(current)

grades = [3, 4, 5, 6, 7, 8, 9, 10]
quantity = np.zeros((len(label), len(grades)), dtype=int)
k = 0
current = data[0][1]
for i in data:
    if (i[1] == current):
        quantity[k][i[2] - 3] += 1
    else:
        current = i[1]
        k += 1
        quantity[k][i[2] - 3] += 1

category_names = list(map(str, grades))
results = {}

for i, m in enumerate(label):
    results[str(m)] = quantity[i]

def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.set_ylabel('Количество студентов')
    ax.set_xlabel('Группы')
    ax.set_xticks(np.arange(len(labels)))
    ax.set_xticklabels(labels)

    bottom = np.zeros(len(labels))
    colormap = plt.get_cmap('RdYlGn')

    for i, colname in enumerate(category_names):
        color = colormap((i) / (len(category_names) - 1))
        ax.bar(labels, data[:, i], bottom=bottom, label=colname, color=color)
        bottom += data[:, i]

    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1), loc='lower left', fontsize='small')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    return fig, ax

survey(results, category_names)
plt.title('Оценки по студентам', pad=30)
plt.savefig("task3_students.png")
plt.show()
