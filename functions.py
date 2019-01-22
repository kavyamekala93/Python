students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title)
#         students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id):
    student = {"name": name, "student_id": student_id}
    students.append(student)

def save_file(student,student_id):
    try:
        f = open("students.txt", "a")
        f.write(student+ '-'+ student_id+ "\n")
        f.close()
    except Exception:
        print("could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("could not read file")


#student_list = get_students_titlecase()
read_file()
print_students_titlecase()

"""student1= Student("bhagi","1050")
student2= Student("nimmi")
print('memory location is different as both of these are different instances:',student1,student2)
print(Students) """

student_name = input("Enter Student Name:")
student_id = input("Enter Student Id:")

add_student(student_name, student_id)
save_file(student_name, student_id)



