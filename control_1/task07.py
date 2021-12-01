wlist = []
n = int(input())
for i in range(n):
    istream = input().split()
    for word in istream:
        word_is_connected = False
        for wset in wlist:
            if word.lower() == list(wset)[0].lower():
                wset.add(word)
                word_is_connected = True
        if word_is_connected == False:
            wlist.append(set([word]))
wlist.sort(key=lambda a: str(100000 - len(a)*100)+list(a)[0].lower())
for wset in wlist:
    if len(wset) > 1:
        print(list(wset)[0].lower())