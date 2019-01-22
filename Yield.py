#Yield- generator function : used instead of 'return' in generator functions unlike regular functions(where we use 'range' for
# iterating the 'for' loop), purpose- generally used while performing I/O operations (ex: file open, read) to save processor(CPU) time
#In the given example in course, 'yield line' is used   it iterates over the file that we pass as function arguments 'f', during every single iteration 'red_students'fn
# yields a single line from that file to its caller

students=[]


def read_file():
    try:
        f = open("students.txt", "r")
        for student in read_students(f):
            students.append(student)
            f.close()
    except Exception:
        print("could not read file")


def read_students(f):
    for line in f:
        yield line


read_file()
print(students)
