#!/usr/bin/python
# -*- coding:utf-8 -*-

#企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万
# 元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

# 1, profit $lte 10   get:10%
# 2, profit $gt 10 and profit $lte 20   get: + 7.5%
# 3, profit (20, 40] get: + 5%
# 4, profit (40, 60] get: + 3%
# 5, profit (60, 100] get: + 1.5%
# 6, profit (100, ...) get + 1%

i = int(raw_input('净利润:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0

for idx in range(0, 6):
    if i > arr[idx]:
        r+=(i - arr[idx]) * rat[idx]
        print (i - arr[idx]) * rat[idx]
        i=arr[idx]
print r























