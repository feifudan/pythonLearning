import time


#time中，最常用的获取时间的三个函数，time，gmtime，ctime

#time.time()表示从1970 年1月1日，0点0分开始，到当前这一个时刻开始的时间（以秒为单位）
print(time.time())
#获取人类易读时间的最简单的函数
print(time.ctime())
#获取计算机容易处理的格式时间
print(time.gmtime())




#time时间的格式化,strftime函数，strftime(tpl,ts),tpl是格式化模版,ts时间类型变量
t = time.gmtime()
strTime = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(strTime)
t = time.strptime(strTime,"%Y-%m-%d %H:%M:%S")



#程序计时,返回CPU级别的精准时间，单位为秒，连续调用才有意义（调用第一次以后，所有的时间都是从第一次开始计算）
start = time.perf_counter()
time.sleep(2)
end = time.perf_counter()
print(round(end - start,3))


 