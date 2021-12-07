array = sorted((list(map(int, input().split()))), reverse=True)

rep_element = -100000

for i in range(0, len(array)):
    if(array[i] != array[i+1] and array[i] != rep_element):
        print(array[i])
        break
    else:
        rep_element = array[i]