Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#int
int(5)
5
int(7.7)
7
int("hi")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
int(4+6j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(4+6j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(5)
5.0
float(6.7)
6.7
print("pooja")
pooja
print(6+5j)
(6+5j)
float("pooja")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("pooja")
ValueError: could not convert string to float: 'pooja'
float(4+5j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#str
str(4)
'4'
str(4.3)
'4.3'
str(3+4j)
'(3+4j)'
str("hello")
'hello'
str(True)
'True'
str(False)
'False'
#complex
complex(9)
(9+0j)
complex(3+4j)
(3+4j)
complex(7.5)
(7.5+0j)
complex("hi")
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complex("hi")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
>>> #bool
>>> bool(7)
True
>>> bool(5.6)
True
>>> bool(3+4j)
True
>>> bool(True)
True
>>> bool("hello")
True
>>> bool(False)
False
