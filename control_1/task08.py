event_count = int(input())
command_list = [input().split() for i in range(event_count)]
call_count = int(input())
command_list.extend([input().split() for i in range(call_count)])
command_list.sort(key = lambda a: int(a[0])*10 + len(a))

d = { }
for command in command_list:
    if(len(command) > 1):
        if(command[1] == "SET"):
            d[command[2]] = command[3]
        else:
            d.pop(command[2])
    elif len(d) == 0:
        print("(none)")
    else:
        l = sorted(d.items(), key = lambda a : a[0])
        print(", ".join([str(el[0]) + " : " + str(el[1]) for el in l]))