Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[0]
'v'
a[0]
'v'
a[1]
'i'
a[2]
'j'
a[3]
'a'
a[4]
'y'
a[5]
'a'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
a="I am in class"
a[8]
KeyboardInterrupt
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[4]
' '
a[7]
' '
a[1]+a[4]+a[7]
'   '
a="I am learning python fullstack"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[6]a[7]a[8]a[9]+a[10]
SyntaxError: invalid syntax
a[6]+a[7]+a[8]+a[9]+a[10]
'earni'
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
a[21]+a[22]+a[23]+a[24]+a[25]a[26]+a[27]+a[28]+a[29]
SyntaxError: invalid syntax
a[21]+a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]+a[29]

'fullstack'
a[3]+a[4]
'm '
a[2]+a[3]
'am'
a="Time is Precious"
a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'Precious'
a[-16]+a[-15]+a[-14]+a[-13]
'Time'
a="vijayawada is a royal city"
a[-4]+a[-3]+a[-2]+a[-1]+
SyntaxError: invalid syntax
>>> a[-4]+a[-3]+a[-2]+a[-1]
'city'
>>> a[-4]+a[-3]+a[-2]+a[-1]+a[-8]+
SyntaxError: invalid syntax
>>> a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
>>> a[-8]+a[-8]+a[-8]+a[-8]+a[-8]+
KeyboardInterrupt
>>> a[-26]+a[-25]+a[-24]+a[-23]+a[-22]+a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+
SyntaxError: invalid syntax
>>> a[-26]+a[-25]+a[-24]+a[-23]+a[-22]+a[-21]+a[-20]+a[-19]+a[-18]+a[-17]
'vijayawada'
