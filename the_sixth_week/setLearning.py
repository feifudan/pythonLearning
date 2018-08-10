
#集合的常用三个操作
#集合不存在先后顺序


S = set("python123")
for i in S:
    print("{}".format(i),end=" ")


#删除一个元素
#remove移除一个元素，如果不存在这个元素，则报错
S.remove("p")
print()
for i in S:
    print("{}".format(i),end=" ")

#discard移除一个元素，如果不存在这个元素，则忽略，不报错
S.discard("3")
print()
for i in S:
    print("{}".format(i),end=" ")

#随机返回一个元素，并更新S，如果S为空，则KeyError异常
print()
print(S.pop())
for i in S:
    print("{}".format(i),end=" ")

#添加一个元素
S.add("A")
print()
for i in S:
    print("{}".format(i),end=" ")
print()


#集合之间的操作运算
#交（&）、并（|）、差（-）、补（^）、比较（>=<）
