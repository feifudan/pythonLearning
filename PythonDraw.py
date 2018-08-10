import turtle

turtle.setup(650,350,200,200)#设置窗体的其实位置和宽高，四个参数，宽，高，开始x，开始y，默认位置是在中间
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in  range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)

turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
#turtle.done()



print("python".center(20,"="))#用于打印规则
print("{:=^20}".format("python"))#填充、对齐、宽度