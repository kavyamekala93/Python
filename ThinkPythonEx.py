#exercise 3.3
def right_justify1(s):
    snew =(' '*14).join(s)
    print(snew)
right_justify1('allen');
def right_justify(s):
    n=len(s)
    a=int(70.0/n)
    snew=(' '*a).join(s)
    print(snew)
right_justify('allen')

#exercise 3.4
#1:
def do_twice(f):
    f()
    f()
def print_spam():
    print('spam')
do_twice(print_spam)
#2:
def do_twice(f,a):
    f(a)
    f(a)
def print_spam(a):
    print(a)
do_twice(print_spam,5)
#3:
def do_twice(f,b):
    f(b)
    f(b)
def print_twice(b):
    print(b)
do_twice(print_twice,'kavya')
#4:
def do_twice(f,b):
    f(b)
    f(b)
def print_twice(b):
    print(b)
do_twice(print_twice,'spam')
#5:
def do_four(f,c):
    f(c)
    f(c)
def f1(b):
    print(b)
    print(b)
do_four(f1,'kavya')

#Exercise 3.5
print('+','-')
print(1, end=' ') # default value of `end` is '\n'
print(2)
print('''
+----+----+----+----+
|         |         |
|         |         |
|         |         |
|         |         |
+----+----+----+----+
|         |         |
|         |         |
|         |         |
|         |         |
+----+----+----+----+''')
print('''new line
new line2
new line3
''')

#interface design
# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 1
#     length = circumference / n
#     polygon(t, n, length)
# print(circle(7,2))
# print(polygon(7,10,5))
