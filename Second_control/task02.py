all_words = input().split()

dict = { }

for word in all_words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

list = sorted([(dict[key], key) for key in dict], key=lambda a:  str((1000 - a[0])*1000)+ a[1])

for element in list:
    print(str(element[0]) + " " + element[1])