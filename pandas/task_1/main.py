import pandas

data = pandas.read_csv('transactions.csv', sep=',')
print(data)
OK_status = data.loc[data["STATUS"] == "OK"].sort_values(by='SUM', ascending=False)
print("Топ-3 самых дорогих закупок")
for i in range(3):
    print(
        f"{i + 1}. Заказ №{OK_status.iloc[i]['Unnamed: 0']} компании {OK_status.iloc[i]['CONTRACTOR']} на сумму {OK_status.iloc[i]['SUM']}")

df = OK_status.groupby('CONTRACTOR').sum()
print(f"Сумма реально проведенных платежей кампании Umbrella, Inc составляет {df.loc['Umbrella, Inc', 'SUM']}")
