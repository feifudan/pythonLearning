import time

#换行进度条
print("开始执行".center(20,"="))

scale = 10

for i in range(scale):
    a = (i/scale)*100
    b = i*"*"
    c = (scale-i)*"*"
    print("{:>3.0f}%[{}->{}]".format(a,b,c))
    time.sleep(0.1)

print("{:=^20}".format("结束执行"))


#不换行进度条,单行刷新功能的完成，第一，不换行(使用"end=''")，第二，光标回到行首（使用"\r"）,第三，加入计时功能

print("开始执行".center(20,"="))
scale = 10
start = time.perf_counter()
for i in range(scale+1):
    a = (i/scale)*100
    b = i*"*"
    c = (scale-i)*"*"
    dur = time.perf_counter() - start
    print("\r{:>3.0f}%[{}->{}] {:.2f}s".format(a,b,c, dur),end="")
    time.sleep(0.1)

print("\n{:=^20}".format("结束执行"))