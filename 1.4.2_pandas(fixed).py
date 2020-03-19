import pandas as pd
from datetime import time

flag = True
while flag:

    # информация  поездах
    a = [{'train_code': '887B', 'station': 'Lipki', 'time_arrive': time(12, 00)},
         {'train_code': '411C', 'station': 'Kyiv   ', 'time_arrive': time(10, 00)},
         {'train_code': '743L', 'station': 'Lipki', 'time_arrive': time(12, 00)},
         {'train_code': '113F', 'station': 'Rivne', 'time_arrive': time(11, 00)}]

    # вводим диапазон времени приходящих поездов

    while True:
        try:
            start_time = time(hour=int(input("Enter start hours: ")), minute=int(input("Enter start minutes: ")))
            end_time = time(hour=int(input("Enter last hours: ")), minute=int(input("Enter last minutes: ")))
            break
        except ValueError:
            print('Enter an integers!')
    s = sorted(a, key=lambda x: x['time_arrive'])

    # проверяем прибытие каких поездов совпадает с заданым нами диапазоном

    for train in s:
        if start_time <= train.get('time_arrive') <= end_time:
            print(train)
            df = pd.DataFrame(a)
            res = df.groupby(["time_arrive", "station"]).filter(lambda x: len(x) > 1)
            count = len(res)

    # если среди маршрутов есть такие, что приходят на одну станцию в одно и то же время, выводим ошибку и просим ввести новые данные

    for i in res["time_arrive"].to_list():

        if (start_time <= i <= end_time) and (count >= 2):
            print(f'There are {count} wrong destinations')
            print('Accident error. Choose the other time range please.')
            break

        # если "ошибочных маршрутов" нет, прекращаем работу программы

        else:
            flag = False
            break
