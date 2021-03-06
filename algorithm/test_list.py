#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_list.py
# @Author: Wade Cheung
# @Date  : 2018/7/6
# @Desc  : 创建list的4个操作, 时间对比 . concatenation, append, comprehension, list range


from timeit import Timer
import time


# concatenation
def test1():
    l = []
    for i in range(1000):
        l = l + [i]


# append
def test2():
    l = []
    for i in range(1000):
        l.append(i)


# comprehension
def test3():
    l = [i for i in range(1000)]


# list range
def test4():
    l = list(range(1000))


start_time = time.time()
test1()
end_time = time.time()
print((end_time - start_time) * 1000)

start_time = time.time()
test2()
end_time = time.time()
print((end_time - start_time) * 1000)

start_time = time.time()
test3()
end_time = time.time()
print((end_time - start_time) * 1000)

start_time = time.time()
test4()
end_time = time.time()
print((end_time - start_time) * 1000)

t1 = Timer("test1()", "from __main__ import test1")
print("concatenation ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")
