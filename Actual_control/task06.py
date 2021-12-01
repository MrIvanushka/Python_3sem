path = input()
target_class, target_power = input().split()
target_power = int(target_power)

data = [i.split() for i in open(path, 'r').read().split('\n')]
cleared_data = []
for el in data:
    el_class = el[1].split(",")
    compared = False
    for cl in el_class:
        if cl == target_class:
            compared = True
    if compared and int(el[2]) >= target_power:
        cleared_data.append([el[0], el[2]])
cleared_data.sort(reverse=True, key=lambda a: int(a[1]))
for el in cleared_data:
    print(el[0])