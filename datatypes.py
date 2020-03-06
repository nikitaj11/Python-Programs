Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> b=4.5
>>> type(b)
<class 'float'>
>>> a=10
>>> a=5+9i
SyntaxError: invalid syntax
>>> a=5+9j
>>> type(a)
<class 'complex'>
>>> a=9.8
>>> b=int(a)
>>> b
9
>>> d=float(b)
>>> d
9.0
>>> f=complex(a,b)
>>> f
(9.8+9j)
>>> a>b
True
>>> f<b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f<b
TypeError: '<' not supported between instances of 'complex' and 'int'
>>> b>d
False
>>> d>b
False
>>> d=b
>>> d
9
>>> int(true)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined
>>> int(True)
1
>>> int(Flase)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(Flase)
NameError: name 'Flase' is not defined
>>> int(False)
0
>>> range(20)
range(0, 20)
>>> list(range(20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(3,20,2))
[3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> list(range(5,20,5))
[5, 10, 15]
>>> d={'abc':'tv','xyz':'moblile','pqr':'wifi'}
>>> d
{'abc': 'tv', 'xyz': 'moblile', 'pqr': 'wifi'}
>>> d.get('abc')
'tv'
>>> d.keys()
dict_keys(['abc', 'xyz', 'pqr'])
>>> d.values
<built-in method values of dict object at 0x000001C36DFD0948>
>>> d.values()
dict_values(['tv', 'moblile', 'wifi'])
>>> d.get('tv')
>>> d
{'abc': 'tv', 'xyz': 'moblile', 'pqr': 'wifi'}
>>> 
