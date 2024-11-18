import pandas
import matplotlib.pyplot as pyplot

data1 = pandas.read_excel('students_info.xlsx')
data2 = pandas.read_html('results_ejudge.html')
data1 = data1.rename(columns={"login": "User"})
data2 = data2[0].drop(columns=['Place'])
data = pandas.merge(data1, data2, on='User')
data = data.rename(
    columns={"group_faculty": "Учебная_группа", "group_out": "Группа_информатики", "Solved": "Решенные_задачи",
             "Score": "Результат"})
print(data)

Mean_by_study_group = data.loc[:, ["Учебная_группа", "Решенные_задачи"]].groupby('Учебная_группа').mean()
Mean_by_IT_group = data.loc[:, ["Группа_информатики", "Решенные_задачи"]].groupby('Группа_информатики').mean()

graph1 = {
    'Учебная_группа': list(Mean_by_study_group.index),
    'Решенные_задачи': list(Mean_by_study_group.loc[:, "Решенные_задачи"])
}
graph1 = pandas.DataFrame(graph1)

graph1.plot(kind='bar', x='Учебная_группа', y='Решенные_задачи', color='purple')

pyplot.title('Гистограмма решенных задач по учебным группам (факультет)')
pyplot.xlabel('Учебная группа')
pyplot.ylabel('Решенные задачи')

pyplot.savefig('faculty.png')

graph2 = {
    'Группа_информатики': list(Mean_by_IT_group.index),
    'Решенные_задачи': list(Mean_by_IT_group.loc[:, "Решенные_задачи"])
}
graph2 = pandas.DataFrame(graph2)

graph2.plot(kind='bar', x='Группа_информатики', y='Решенные_задачи', color='purple')

pyplot.title('Гистограмма решенных задач по учебным группам (информатика)')
pyplot.xlabel('Учебная группа')
pyplot.ylabel('Решенные задачи')

pyplot.savefig('informatics.png')

a = 10  # Минимальный балл, чтобы задача G считалась решенной
b = 10  # Минимальный балл, чтобы задача H считалась решенной
Result3 = data.loc[(data['G'] > a) | (data['H'] > b)]
print("Ребята, которые решили хотя бы одну из последних двух задач:")
for i in list(Result3.index):
    print(
        f"{Result3.loc[i, "User"]} из учебной группы № {Result3.loc[i, "Учебная_группа"]} попал в группу по информатике № {Result3.loc[i, "Группа_информатики"]}")
