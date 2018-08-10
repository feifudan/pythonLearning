
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))


#lambda函数
f = lambda x,y:x+y
print(f(4,5))

#函数的三种参数方式：可选参数需要加初始值，可变参数需要加一个星号，名称传值