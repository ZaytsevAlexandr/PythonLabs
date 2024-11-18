import pandas
import matplotlib.pyplot as pyplot

data = pandas.read_csv('flights.csv', sep=',')
table = data.loc[:, 'CARGO'].value_counts()

print(f"Количество выполненных рейсов:")
for i in range(len(table)):
    print(f"Компания {table.index[i]} совершила {list(table)[i]} рейсов")

df = data.groupby('CARGO').sum()
table1 = df.loc[:, 'PRICE']
print(f"Полная стоимость билетов:")
for i in range(len(df)):
    print(f"Компания {df.index[i]} совершила перелетов на сумму билетов {df.loc[df.index[i], 'PRICE']} денежных единиц")

print(f"Общая масса багажа:")
table2 = df.loc[:, 'WEIGHT']
for i in range(len(df)):
    print(f"Компания {df.index[i]} перевезла в общем {df.loc[df.index[i], 'WEIGHT']} единиц массы груза")

a = pandas.DataFrame({'Авиакомпания': list(table.index), 'Совершенные полеты': list(table)})
b = pandas.DataFrame({'Авиакомпания': list(table1.index), 'Денег в сумме': list(table1)})
c = pandas.DataFrame({'Авиакомпания': list(table2.index), 'Масса в сумме': list(table2)})

a.set_index('Авиакомпания')['Совершенные полеты'].plot(kind='bar', figsize=(10, 6), color='skyblue')
pyplot.title('Совершенные полеты по авиакомпаниям')
pyplot.xlabel('Авиакомпания')
pyplot.ylabel('Совершенные полеты')
pyplot.xticks(rotation=45)
pyplot.tight_layout()
pyplot.savefig('flight_amount.png')

b.set_index('Авиакомпания')['Денег в сумме'].plot(kind='bar', figsize=(10, 6), color='skyblue')
pyplot.title('Сумма за продажи всех представленных билетов')
pyplot.xlabel('Авиакомпания')
pyplot.ylabel('Денежных единиц')
pyplot.xticks(rotation=45)
pyplot.tight_layout()
pyplot.savefig('ticket_amount.png')

c.set_index('Авиакомпания')['Масса в сумме'].plot(kind='bar', figsize=(10, 6), color='skyblue')
pyplot.title('Общая масса всех перевезенных грузов')
pyplot.xlabel('Авиакомпания')
pyplot.ylabel('Единиц массы')
pyplot.xticks(rotation=45)
pyplot.tight_layout()
pyplot.savefig('mass_amount.png')


