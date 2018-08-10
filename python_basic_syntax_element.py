#本章基本语法

#计算机雨程序设计
#编译和解释
#程序的基本编写方法

TempStr = input("请输入带有符号的温度值:")

if TempStr[-1] in ["F","f"]:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("转换以后的温度是{:.2f}C".format(C))
    pass
elif TempStr[-1] in ["C","c"]:
    F = (eval(TempStr[0:-1]))*1.8 + 32
    print("转换以后的温度是{:.2f}F".format(F))
    pass
else:
    print("输入格式错误")


print(eval("32"))

#其中eval函数的功能是去掉字符串最外边的引号，然后执行剩下的字符语句