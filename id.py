Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=10
>>> id(num)
140712809915504
>>> a=5
>>> id(a)
140712809915344
>>> a=5
>>> n=a
>>> id(a)
140712809915344
>>> id(n)
140712809915344
>>> name="Nikita"
>>> id(name)
2948882637856
>>> k=3
>>> a=k
>>> id(k)
140712809915280
>>> id(a)
140712809915280
>>> a=9
>>> id(a)
140712809915472
>>> id(n)
140712809915344
>>> pi=3.14
>>> pi
3.14
>>> pi=3.15
>>> pi
3.15
>>> PI=3.12
>>> PI
3.12
>>> type(pi)
<class 'float'>
>>> type(a)
<class 'int'>
>>> 
