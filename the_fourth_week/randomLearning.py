import random

#random标准库，是采用梅森旋转算法生成的w伪随机序列



#基本随机函数

#seed函数，初始化给定的随机数种子，默认为当前系统的时间（如果不调用seed函数，则使用当前系统时间来作为随机数种子）
random.seed()
random.random()
#例子，如果给定随机数种子，那么，将要产生的随机数序列就唯一确定了,(random函数生成一个从0到1之间的一个随机小数)
random.seed(10)
print(random.random())
print(random.random())
random.seed(10)
print(random.random())
print(random.random())


#扩展随机函数
a = random.randint(10,100)#生成一个【10，100】之间到一个整数
b = random.randrange(10,100,8)#生成一个【10，100）之间，以8为步长，的一个随机数
c = random.uniform(10,100)#生成一个【10,100】之间的随机小数（python中的小数取的是小数点后的十六位）
d = random.getrandbits(8)#获得一个k比特长的随机整数

s = [2,3,4,7,5,1]
e = random.choice(s)#从序列中随机选取一个元素
random.shuffle(s)#打乱一个序列

print(a,b,c,d,e,s)