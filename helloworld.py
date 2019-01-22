print ("Hello world")
def add_twonumbers(x,y):
    print(x+y)
add_twonumbers(2,3)
#type hinting: helps to add data types to python program
def add_twonumbers_typedefined(a:int,b:int) ->int:
    print(a+b)
add_twonumbers_typedefined(5,6)
#add_twonumbers_typedefined(3,s)
pi=3.145789
d=int(pi)
e=2.567+d
print(e)
print(pi+2.56)
f=36;
print(float(f))
print("hello".capitalize())
print("""hello""".replace("l","v"))
print('hello'.isalpha(),'1234a'.isdigit())
print('i,am,good,girl'.split(','), 'i,am,good,girl'.split('/'))
lang='python'
feel='interesting'
feel2='excited$'
#string formatting and raw string
print('programming {0} is very {1}'.format(lang,feel), f'programming {lang} is very {feel} and {feel2}', r'programming {lang} is very {feel} and {feel2}')
unicode_string= u'\u03BC\u0394'
print(u'unicode string in python \u03BC\u0394', unicode_string,'type is',type(unicode_string),'length is',len(unicode_string)) #strings in python3 are unicode by default unlike in python2
kavya_isfemale= True; vinni_ismale= False; aliens_found= None
print(int(kavya_isfemale), int(vinni_ismale), str(aliens_found) ,str(kavya_isfemale),str(vinni_ismale))
#if and else statements both end with colon in python- sometimes no need to write else statement except in boolean and other conditions
number1=2; number2=0; number3=-1; number4= 'stringliteral'
string1= 'kavya'; good= True; bad= False
if number1:
    print('it is number')
if number2:
    print('it is number')
else: # goes into else part as it doesnt consider 0 as number
    print('it is not number')
if number3:
    print('printed as it is defined')
if number4:
    print('still printed as it is defined irrespective of its type',number4)
if string1:
    print(string1)
if good:
    print('prints good as it is true')
if not bad:
    print('prints even now as it is false and the condition not bad is satisfied')
if bad:
    print('doesnt print now')
else:
    print('prints in else part')
if number1 and good:
    print('print both number and text',number1, good)
if number1 and bad:
    print('jkjsdfh')
else:
    print('goes into else part')
#ternary operator
print('bigger' if number3> number1 else 'smaller')
#Lists in Python
student_names=['kavya','bhagi','sai']
student_names.append('kiran'); checking='sai' in student_names; checking2= 'bha' in student_names
print(student_names, len(student_names),checking, checking2)
student_names.append('bhagirath')
del student_names[3]
print(student_names, student_names[1:], student_names[1:2],student_names[1:-1]) #list slicing
#for loop examples
for name in student_names:
    print('student name is {0}'.format(name))
i=0; j=0;
for index in range(5):  # range specifies the number of iterations/number of loops
    i+=10;
    print('the value of i is {0}'.format(i))
for index in range(5,20,3):
    #j+=6;
    print('the value of j is {0}'.format(j))
print(range(5,10,2))
#break: doesnt execute any statements below it and reaches end of the code
#continue: doesnt execute any statements below it and reaches end of the block and executes statements after that block

#Dictionaries: Useful to store structured data-- dic are key value pairs
student={ 'name':'kavya', 'id':'105086527', 'course': 'MEng'}
print(student, student.keys(), student.values(), student.get('another', 'swarna'), student) # student.get- to specify a new key value pair
student['name']='swarna'; student['id']='104087528' # changing student key values
print(student)
del student['course']  # deleting specified the key- value pair completely from the dictionary
print(student)

#Exceptions: to avoid the crashing of the program or to make the program run amd display exception(error message) to user when an exception occurs
student['lastname']='bhagi'
try:
    lastname=student['lastname']
    lastname2=3+lastname
except KeyError: print('dsjkfh')
except TypeError as error:
    print('any user friendly message')
    print(error)
# "except Exception:" handles all the errors in the program

#other Data types in python:
#complex, byte and bytearray, tuple-similar to lists but are immutable, set and frozen set- removes redundant values, ITER tools to learn more about loops in Python

#to change drive: DriveName(Colon):,  to change directory cd(space)Directory/FolderName, mkdir- to create folder

def var_args(name,*args):
    print(name,args)
var_args('kavya','bhagi','sai','nimmi','babbu')
def var_argsfun(gender, **kwargs):   #to print various number of arguments in lists
    print(gender)
    print(kwargs['description'], kwargs['feedback'])
var_argsfun('Female', description='love python coding', feedback='good', feel='none')
double=lambda x:x*2   #Lambda function
print(double(5))

#class: logical group of functions and data or class is the blue print of the instances/building blocks
#'pass' keyword: used inside class or functions, it means do nothing
