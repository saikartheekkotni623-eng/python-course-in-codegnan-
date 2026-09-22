Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
a[::3]
'Dacn'
a="Machine Learning"
a[::2]
'McieLann'
a[::4]
'MiLn'
a[5:9]
'ne L'
a[6:]
'e Learning'
a[:11]
'Machine Lea'
>>> a[::8]
'ML'
>>> a="cloud computing"
>>> a[1:8:2]
'lu o'
>>> a[2:12:4]
'ocu'
>>> a[1:14:5]
'lct'
>>> a[1:13:3]
'ldou'
>>> a[3:9:4]
'uo'
