import random

def generate_points_abnormal(point_1, point_2):
    num_points = random.choices([1, 2, 3], weights=[60, 20, 20], k=1)[0]
    points = []

    for _ in range(num_points):
        x = random.randint(min(point_1[0], point_2[0]), max(point_1[0], point_2[0]))
        y = random.randint(min(point_1[1], point_2[1]), max(point_1[1], point_2[1]))
        point = (x, y)
        points.append(point)

    return points


def generate_points_normal(point_1, point_2):
    num_points = random.choices([1, 2, 3], weights=[60, 20, 20], k=1)[0]
    points = []

    last_point = point_1
    for _ in range(num_points):
        x = random.randint(
            min(last_point[0] + 1, point_2[0]), max(last_point[0] + 1, point_2[0])
        )
        y = random.randint(
            min(last_point[1] + 1, point_2[1]), max(last_point[1] + 1, point_2[1])
        )
        point = (x, y)
        points.append(point)
        last_point = point

    return points


print(generate_points_normal((1000, 200), (1200, 1800)))
