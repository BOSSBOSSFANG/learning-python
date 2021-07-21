import matplotlib.pyplot as plt
import random

random.seed(1)
complete_time = {(0, 0, 0, 1): (8, 9, 1), (1, 0, 0, 1): (5, 8, 3), (3, 0, 0, 0): (8, 10, 2), (0, 1, 0, 1): (1, 2, 1),
                 (1, 1, 0, 1): (0, 1, 1), (3, 1, 0, 0): (1, 2, 1), (0, 2, 0, 1): (3, 5, 2), (1, 2, 0, 1): (2, 3, 1),
                 (3, 2, 0, 0): (3, 5, 2), (2, 0, 1, 0): (10, 11, 1), (4, 0, 1, 0): (11, 13, 2),
                 (5, 0, 1, 1): (10, 13, 3), (2, 1, 1, 0): (2, 4, 2), (4, 1, 1, 0): (4, 5, 1), (5, 1, 1, 1): (2, 4, 2),
                 (2, 2, 1, 0): (5, 6, 1), (4, 2, 1, 0): (6, 9, 3), (5, 2, 1, 1): (5, 6, 1), (6, 0, 2, 1): (13, 14, 1),
                 (7, 0, 2, 0): (13, 15, 2), (8, 0, 2, 1): (15, 16, 1), (6, 1, 2, 1): (5, 6, 1), (7, 1, 2, 0): (5, 7, 2),
                 (8, 1, 2, 1): (7, 9, 2), (6, 2, 2, 1): (9, 11, 2), (7, 2, 2, 0): (9, 10, 1), (8, 2, 2, 1): (11, 13, 2)}

flights = 'CA4511 CA4373 TV9819 3U8741 8L9671 CA4193 EU2287 3U8911 8L9669 CA4031 MU6387 3U8861 CA4529 CA4187 3U8467 EU2211 3U8857 3U8711 CA4029 MU2471'.split(
    ' ')
len_flights = len(flights)
complete_time1 = {}

patrol_time = [random.randint(25, 40) for i in range(len_flights)]
car_time = [random.randint(15, 35) for i in range(len_flights)]

interval_co = [random.randint(5, 15) for i in range(len_flights)]
interval_single = [random.randint(20, 30) for i in range(len_flights)]
intervals = [interval_co, interval_single]
car_to_car_time = 5


#  complete_time的key表示的是任务、产品、工作站等信息，value第一个值表示的是任务开始时间，第二个值表示结束时间，第三个值表示加工时间


# complete_time=complete_time[:len(flights)]


def plt_gantt(complete_time, mode):
    last_patrol = 0
    last_car = 0
    for i in range(len_flights):
        key_patrol = (i, 0)
        key_car = (i, 1)
        patrol_end = last_patrol + patrol_time[i]
        complete_time1[key_patrol] = (last_patrol, patrol_end, patrol_time[i])
        car_end = patrol_end + interval_co[i] + car_time[i]
        complete_time1[key_car] = (patrol_end + intervals[mode][i], car_end, car_time[i])
        if i % 5 == 0:
            last_patrol = patrol_end
            last_car = car_end
        else:
            last_patrol = last_patrol + car_to_car_time
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 显示中文标签
    font_dict_task = {
        "family": "Microsoft YaHei",
        "style": "oblique",
        "weight": "bold",
        "color": "white",
        "size": 14
    }
    font_dict_time = {
        "family": "Microsoft YaHei",
        "style": "oblique",
        "color": "white",
        "size": 12
    }
    color = ['b', 'g']
    for k, v in complete_time.items():
        plt.barh(y=k[0], width=v[2], left=v[0], edgecolor="black", color=color[k[1]])
    ylabels = []  # 生成y轴标签
    for i in range(len_flights):
        ylabels.append(flights[i])
    titles = ["协同调度甘特图", "单独调度甘特图"]
    plt.yticks(range(len_flights), ylabels, rotation=45)
    plt.title(titles[mode])
    plt.xlabel("时间 /min")
    plt.ylabel("航班号")

    plt.show()


if __name__ == '__main__':
    plt_gantt(complete_time1, 1)
