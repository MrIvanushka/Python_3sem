usr_count = int(input())
usr_list = [input().split() for i in range(usr_count)]
server_count = int(input())
server_list = [input().split() for i in range(server_count)]
target = int(input())

usr_set = set()
for server_data in server_list:
    server_contains_target = False
    for i in range(2, len(server_data)):
        if int(server_data[i]) == target:
            server_contains_target = True
    if server_contains_target:
        for i in range(2, len(server_data)):
            if int(server_data[i]) != target:
                usr_set.add(int(server_data[i]))
exp = []
for el in usr_set:
    for usr in usr_list:
        if int(usr[0]) == el:
            exp.append(usr[1])
for el in sorted(exp):
    print(el)