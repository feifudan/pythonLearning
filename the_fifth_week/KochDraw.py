import turtle

def koch(size,n):
    if n == 0:
        turtle.fd(size)
    else:
        for i in [0,60,-120,60]:
            turtle.left(i)
            koch(size/3,n-1)


def main():
    turtle.setup(800,800)
    turtle.penup()
    turtle.goto(-300,-50)
    turtle.pendown()
    turtle.pensize(2)

    level = 3
    koch(400,3)
    turtle.right(120)
    koch(400, 3)
    turtle.right(120)
    koch(400, 3)
    turtle.right(120)
    turtle.done()

main()