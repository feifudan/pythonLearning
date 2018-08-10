import jieba

def getText():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for i in '|"#$%&()*+,-./:;<=>?@[\\]^_{|}~':
        txt = txt.replace(i," ")

    return txt


hamlettxt = getText()

word = hamlettxt.split()#split方法，默认使用空格分开

count = {}

for i in set(word):
    count[i] = word.count(i)

#排序
items = list(count.items())
items.sort(key = lambda x:x[1],reverse = True)


for i in range(10):
    word,count = items[i]
    print("{:<10}{:>5}".format(word,count))


