
#python的读写文件操作（打开--》操作-->关闭）


#open函数两个参数，一个是文件名称（包括路径），另一个是打开模式，
# （r:只读模式，如果文件不存在，返回FileNotFoundError
# w:覆盖写模式，文件不存在则创建，存在则完全覆盖
# x:创建写模式，存在则返回FileExistsError
# a:追加写模式，文件不存在则创建，存在则在文件最后追内容
#上述模式后面可以加一个符号+，表示在原有功能上增加同时读写的功能


# b:以二进制形式打开
# t：文件默认模式打开）
a = open("hamlet.txt","a+")

size = 2
a.read(2)#默认读取全部
a.readline(2)#读取一行（前2个字符）
a.readlines(2)#读最后2行

#写入一个字符串或者字节流
a.write("中国")
#写入一个字符串list
a.writelines(["中国","美国"])

#改变文件操作指针，参数值为0，1，2，其中0表示回到文件开头，1表示当前位置，2表示文件结尾
a.seek(0)

fo = open("test.txt","w+")
ls = ['中国',"美国"]
fo.writelines(ls)
fo.seek(0)#必须加这一句，否则无法读出来，因为写入以后，文件操作指针在文件的末尾，需要将操作指针返回文件开头
for i in fo:
    print(i)
fo.close()


#map函数，作用是将第一个参数，作用于第二个参数的每一个数
line = "1,2,3,4"
print(
    list(map(eval,line.split(",")))
)
