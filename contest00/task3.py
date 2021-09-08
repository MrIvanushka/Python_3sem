data = input().split(" ")
start_floor, target_floor, lift_floor = [int(data[i]) for i in range(0, 3)]
lift_up_time, opening_time, character_up_time = [float(data[i]) for i in range(3, 6)]

if abs(start_floor - target_floor) * character_up_time < \
        lift_up_time * (abs(start_floor - target_floor) + abs(start_floor - lift_floor)) + 3 * opening_time:
    print("stairs")
else:
    print("elevator")
