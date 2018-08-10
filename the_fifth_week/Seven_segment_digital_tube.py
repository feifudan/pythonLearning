import turtle
import time

strTime = time.gmtime()
year = strTime[0]
mounth = strTime[1]
day = strTime[2]
hour = strTime[3]
min = strTime[4]
sec = strTime[5]


def drawNumb(X,Y,Num = 8):
    turtle.setup(650, 350, 200, 200)  # 设置窗体的其实位置和宽高，四个参数，宽，高，开始x，开始y，默认位置是在中间
    turtle.penup()
    #turtle.fd(-250)
    turtle.pendown()

    turtle.pensize(5)
    turtle.pencolor("purple")
    turtle.seth(0)

    if Num == 8:
        turtle.penup()
        turtle.set
        turtle.pendown()
        turtle.fd(40)
        turtle.fd(40)
        turtle.fd(40)

    turtle.done()

#字符串的反转实现方法，可以使用切片，将步长设置为-1
s = "yinxiaofei"
print(s[::-1])
