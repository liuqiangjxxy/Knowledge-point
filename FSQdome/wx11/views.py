# coding:utf-8

# @csrf_exempt
def home(request):
	print "你好";
#输出结果
print "你还"

#if 判断
if True:
	print "True"
else:
	print "False"

if True:
	print "Answer"
	print "True"
else:
	print "Answer"
	#没有严格缩进,执行时会报错

#赋值
item_one = "one"
item_two = "two"
item_three = "three" 
total = item_one + \
		item_two + \
		item_three
print total

#数组
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]

print days

word ='word'
sentence ="这是一个句子."
paragraph ="这是一个段落"

print word
print sentence

# raw_input("\n\nPress the enter key to exit.")
import sys; x ="runoob"; sys.stdout.write( x + "\n")

#赋值
x="a"
y="b"
print "----- 换行 -----"
print x
print y
print "--------不换行----"
print x,
print y,
print "\n"
print "---- a ---- b ----- c -----"
a = b = c = 1
a, b, c="a","b","liu"
print a
print b
print c
suite="none"
if a==1 :
	suite="a"
	print suite
	print a
if b==1 :
	suite="b"
	print suite
	print b
if c==1 :
	suite="c"
	print suite
	print c

print "suite --" + suite
print suite
var1 = 1
var2 = 10
del var1

# python字符串
counter = 100 #赋值整型变量
minles = 1000.1 #浮点型
name = "John" #字符串
print counter 
print minles
print name

s="abcdefg"
s1="Ilovepython"
s1_result=s1[1:5]
print s1_result
print s1[0],
print s1[1],
print s1[2],
print s1[3],
print s1[4],
print s1[5]

#python 列表 ---> 数组
list =["runoob",789,2.64,"John","70.2"]
tinylist = [123,"john"]
print list
print list[0]
print list[1:3] #包含1 不包含3
print list[2:]
print list[:2]
print tinylist * 2
print list + tinylist
print tinylist + list


#元组
tuple = ("runoob",789,2.35,"john",70.3)
print tuple
print list
list[2] = 1000
print list
print tuple[0]
print tuple[1]
print tuple[1:3]

#字典
dict={}
dict["one"] = "This is one"
dict[2] = "This is two"
dict["two"] = "[{name:'刘'},{age:'25[{lir:1}]'}]"
print dict

dict2={'name':'zara','Age':7}

cmp(dict2,dict) #比较两个字典元素
len(dict2) #计算字典元素个数,即键的总数.
str(dict2) #输出字典可打印的字符串表示.
type(dict2)
print dict2
print len(dict2)
print str(dict2)
print type(list)
