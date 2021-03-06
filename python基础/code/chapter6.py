# -*- coding: utf-8 -*-
# @Author: cbbfcd
# @Date:   2017-08-28 15:19:03
# @Last Modified by:   cbbfcd
# @Last Modified time: 2017-09-18 21:16:12

# IO操作



## 字符串格式化
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现
#  repr() 函数可以转义字符串中的特殊字符
# repr() 的参数可以是 Python 的任何对象
print(repr('hello world\n')) # 'hello world\n'
print(str('hello world\n')) # hello world

# 字符串格式化输出，str.format()

# 1. 确定位数
for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('{0:.3f}'.format(3.1415926)) # 3.142

# 2. 带关键字参数
print('{x:.{d}f}'.format(x=3.1415926,d=4)) # 3.1416

# 3. '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化
print('{!r}'.format('3.1415\n')) # '3.1415\n'

# 4. 格式化字典
dic = {'name':'jack', 'age':25}
print('name: {name:s}, age: {age:d}'.format(**dic)) # name: jack, age: 25





## 读写文件

# 读文件

with open(r'E:\Python\PythonNotes\python基础\files\test.txt', 'r') as f:
	print(f.read())
# 上面的with其实就是try...catch的替代，这样我们就不用写close()了，不然是这样的：
try:
	f=open(r'E:\Python\PythonNotes\python基础\files\test.txt', 'r')
	print(f.read())
except Exception as e:
	print('error')
finally:
	if f:
		f.close()
# f.read(size) 如果不指定参数的话是一次性读取,文件大就会影响效率了。
# f.readline() 读一行
# f.readlines() 读取所有行,文件大就会影响效率了。

# 优化一下
with open(r'E:\Python\PythonNotes\python基础\files\test.txt', 'r') as f:
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		print(line.strip(),end=' ') # hello world 欢迎你



## 写入文件

### api

# 1. f.write(string) 将 string 写入到文件中, 然后返回写入的字符数
# 2. f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
# 3. 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数,
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
str = "\n welcome to china! \n 欢迎来中国啊"
with open(r'E:\Python\PythonNotes\python基础\files\test.txt', 'a') as f:
	f.write(str)
# 这里的模式是'a'就是文件末尾添加，如果要在开头添加的话可以使用f.seek(0)
# 'w'的模式，如果文件存在的会覆盖，不存在会创建一个新的
# open()函数可以接受两个关键字参数，encoding表示编码格式，errors 参数，表示如果遇到编码错误后如何处理
with open(r'E:\Python\PythonNotes\python基础\files\test2.txt', 'r+', encoding='utf-8',errors='ignore') as f:
	f.read()
	str = 'oooo...!  '+f.read()
	f.seek(0)
	f.write(str)


## pickle模块

import pickle

def make_pickle_file():
	grades = {
		'a':[1,2,3,4+1j],
		'b':'hello world',
		'c':None
	}

	with open(r'E:\Python\PythonNotes\python基础\files\grades.dat','wb') as outfile:
		pickle.dump(grades, outfile)

def get_pickle_file():
	with open(r'E:\Python\PythonNotes\python基础\files\grades.dat', 'rb') as infile:
		grades = pickle.load(infile)
		print(grades)

make_pickle_file()
get_pickle_file() # {'a': [1, 2, 3, (4+1j)], 'c': None, 'b': 'hello world'}


## OS

import os

# 获取当前文件夹下所有以.py结尾的文件
def getAllPy(path=None):
	if path == None:
		path = os.getcwd()
		return [f for f in os.listdir(path) if os.path.isfile(f) if f.endswith('.py')]
print(getAllPy())
 # ['chapter1.py', 'chapter2.py', 'chapter3.py', 'chapter4.py', 'chapter5.py', 'chapter6.py', 'hello.py', '__init__.py

#返回当前文件夹下所有文件的大小总和
def size_in_file(fname):
	return os.stat(fname).st_size

def getAllSize(path=None):
	return sum( size_in_file(f) for f in os.listdir(os.getcwd()) ) # 生成器
print('size:{}'.format(getAllSize())) # size:28109

## 获取网页信息

import urllib.request
page = urllib.request.urlopen('http://www.baidu.com')
html = page.read()
print(html)


# 用代码打开网页
import webbrowser
webbrowser.open('http://www.baidu.com')


# StringIO
from io import StringIO
ff = StringIO()
ff.write('hello wolrd')
print(ff.getvalue()) # hello wolrd

# BytesIO
from io import BytesIO
bb = BytesIO()
bb.write('你好'.encode('utf-8'))
print(bb.getvalue().decode('utf-8')) # 你好
