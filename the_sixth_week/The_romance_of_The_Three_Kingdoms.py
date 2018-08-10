import jieba

def getText():
    txt = open("three.txt","r",encoding="utf-8").read()

    return jieba.lcut(txt)


txt = getText()

words = {}

for i in set(txt):
    if len(i) == 1:
        continue
    words[i] = txt.count(i)

items = list(words.items())
items.sort(key = lambda x:x[1],reverse=True)

for i in range(10):
    print("{:<20}{:>10}".format(items[i][0],items[i][1]))

