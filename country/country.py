#!/usr/bin/python3
# -*- coding: UTF-8 -*-

file = open("1.txt", "r", encoding='utf-8')

for line in file.readlines(): # 读取所有行
    print(line.split('\t'))

file.close()
# Countries and Regions	国家或地区	国际域名缩写	电话代码	时差