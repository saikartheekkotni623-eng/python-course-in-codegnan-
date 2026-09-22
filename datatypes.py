Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=3
type(a)
<class 'int'>
b=5.6
type(b)
<class 'float'>
c='code'
type(c)
<class 'str'>
d="python"
type(d)
<class 'str'>
e='''codegnan'''
type(e)
<class 'str'>
f=5+9j
type(j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    type(j)
NameError: name 'j' is not defined
type(f)
<class 'complex'>
g=3j+5
type(g)
<class 'complex'>
>>> i=6j
>>> type(i)
<class 'complex'>
>>> k=5+8i
SyntaxError: invalid decimal literal
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> c="true"
>>> type(c)
<class 'str'>
