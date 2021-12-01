from collections import defaultdict

event_count = int(input())
event_list = [input().split() for i in range(event_count)]
event_dict = defaultdict(list)

for element in event_list:
    event_dict[element[1]].append([element[0], element[2]])

event_list = []
for key in event_dict.keys():
    event_dict[key].sort(key = lambda a : a[0])
    event_list.append([event_dict[key][0][0], key, event_dict[key][0][1]])
    for i in range(1, len(event_dict[key])):
        if event_dict[key][i][1] != event_dict[key][i-1][1]:
            event_list.append([event_dict[key][i][0], key, event_dict[key][i][1]])

event_list.sort(key = lambda a: a[0] + a[1])

for i in range(len(event_list)):
    print(event_list[i][0] + " " + event_list[i][1] + " " + event_list[i][2])

