
#序列类型的学习


#序列类型是一种基本类型，具备先后顺序，衍生类型有：字符串类型、列表类型、元组类型

#连接两个序列用+号，复制一个序列n次用*
s1 = "python"
s2 = "3"
print(s1*3)
print(s1+s2)

#序列的切片操作s[n:m:k],表示的是从n到序号，以k为步长截取

print("python3"[::2])

#特殊的，当步长为-1的时候，就是反向的返回
print("python3"[::-1])

#常用方法，max，min，len，S.index(x)或S.index(x,i,j)(返回从i到j中，x第一次出现的位置)，S.count(x)(统计S中x的个数)



#元组类型（可以用小括号或者不用括号只用逗号来创建，或者用tuple创建）
T = "yin","xiao","fei"
T1 = (1,23,3)
T2 = tuple(T)
#元组类型一旦定义，将不可改变。元组类型不能改变，所以，其操作只有序列类型的操作即可


#列表类型
#知识点1：如果使用"="号将一个列表赋值给另一个列表，只是将两个指针指向了同一个对象（列表的创建只有使用list()或者[],其他操作都不创建列表）
ls = [1,23,3,3,4,23,3,3,4]
lt = ls
ls.append(1)
print(lt)
#知识点2：删除和修改列表元素
ls[1] = 0#修改第i个元素
print(ls)
ls[1:5:1] = lt
print(ls)
del ls[1]
print(ls)
del  ls[1:6:2]
print(ls)
#知识点3：ls.append(x)在列表最后加入一个元素,ls.clear()清除当前列表,ls.copy()复制当前列表,ls.insert(i,x)在位置i插入元素,ls.pop(i)表示删除位置i的元素
#ls.reverse()反转列表，ls.remove(x)删除列表中第一个出现的x