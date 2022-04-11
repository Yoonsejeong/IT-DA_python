Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
True
True
False
False
4>5
False
5>4
True
3==3
True
3==4
False
10!=4
True
10!=10
False
python==python
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    python==python
NameError: name 'python' is not defined
Python==Python
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    Python==Python
NameError: name 'Python' is not defined
'Python'=='Python'
True
'python'=='Python'
False
'Python'=!'Python'
SyntaxError: cannot assign to literal
'python'=!'python'
SyntaxError: cannot assign to literal
'python'=!'Pyhton'
SyntaxError: cannot assign to literal
'python'!='Python'
True
10>=9
True
10<=8
False
1 is 1.0
False
1 is not 1.0
True
true and true
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    true and true
NameError: name 'true' is not defined. Did you mean: 'True'?
True and True
True
False and True
False
True and False
False
Ture or Ture
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    Ture or Ture
NameError: name 'Ture' is not defined
True or Ture
True
True of False
SyntaxError: invalid syntax
True or False
True
False or False
False
not True
False
not False
True
not False and False or not False
True
3==3 and 3!=4 #True and True
True
4==5 and 4!=5 #True and False
False
hello='Hello, world'
hello
'Hello, world'
hello='안녕하세요'
'안녕하세요'
'안녕하세요'
hello
'안녕하세요'
hello='''hello,world!
안녕하세요
Python입니다.'''
print(hello)
hello,world!
안녕하세요
Python입니다.
s="Python isn't difficult"
s
"Python isn't difficult"
s='He said "Python is easy"'
s
'He said "Python is easy"'
s='Python isn't difficult'
SyntaxError: unterminated string literal (detected at line 1)
s="He said "Python is easy""
SyntaxError: invalid syntax
'Python isn\'t difficult'
"Python isn't difficult"
a = [38, 21, 53, 62, 19]
a
[38, 21, 53, 62, 19]
a = [38, 21, 53, 62, 19]
a
[38, 21, 53, 62, 19]
person = ['james', 17, 175.3, True]
person
['james', 17, 175.3, True]
a=[]
a
[]
b=list()
b
[]
range(10)
range(0, 10)
a=list(range(10))
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b=list(range(5,12))
b
[5, 6, 7, 8, 9, 10, 11]
c=list(range(-4,10,2)
       c
       
SyntaxError: '(' was never closed
c=list(range(-4,10,2))
       
c
       
[-4, -2, 0, 2, 4, 6, 8]
d=list(range(10,0,-1))
       
d
       
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a=(38,21,53,62,19)
       
a
       
(38, 21, 53, 62, 19)
person=('james',17,175.3,True)
       
person
       
('james', 17, 175.3, True)
(38)
       
38
(38,)
       
(38,)
38,
       
(38,)
a=tuple(range(10))
       
a
       
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b=tuple(range(5,12))
       
b
       
(5, 6, 7, 8, 9, 10, 11)
c=tuple(range(5,12))
       
c
       
(5, 6, 7, 8, 9, 10, 11)
a=[1,2,3]
       
tuple(a)
       
(1, 2, 3)
b=(4,5,6)
       
list(b)
       
[4, 5, 6]
