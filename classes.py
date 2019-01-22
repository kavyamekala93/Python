students=[]

#class name starts with capital letter and instance starts with small letter
#self keyword in the function argument:to call the function from the same function,is is used to refer our class from the class, it is the first parameter of the method in class
# when an instance is created for the class, in the background constructor method is called which is hidden
#purpose of constructor: to create custom class initialization
#class and instance attributes: these are the data that can be accessed by all the methods inside the class
#python does not have access modifiers (private, public,protected) , in general all methods in Python are public by default but some developers mention method name starting with
# underscore indicating that method cannot be
#overridden or used directly
#Python does not have interfaces either
#Python can implement multi class inheritance
# "Super" keyword in derived class functionality: explained below

class Student:
    school_name= "University"   #class attribute

    def __init__(self,name,student_id=332):    # if we don't specify a particular value to id, it becomes optional
        #student={"name": name, "student_id": student_id}  # student dictionary
        #students.append(student)

        self.name=name
        self.student_id= student_id
        students.append(self)


    def __str__(self):     # it is called every time an instance is created for the class just like the constructor
        return "Student1" + self.name  # 'str' method is used to print the actual name instead of memory reference

    def get_name_capitalize(self):
        return self.name.capitalize()
        # self.get_name_Capitalize()   # to call function from the same function

    def get_School_name(self):
        return self.school_name



kavya=Student("kavya","105086527")   #Student=Student("kavya")
print(kavya)
print(students)    # if we print students without 'str' method along with student dictionary(instead of self.name) then memory reference is printed.
print(Student.school_name)   # to access the class attribute using class name

print("Below outputs are for Inheritance functionality:")
print("kavya")
#Inheritance and polymorphism:
class HighSchoolStudent(Student):    # 'HighSchoolStudent' derived class inherits from parent class-'Student'
     HighSchool_name= "XYZ uni"      # 'HighSchoolStudent'- derived class attribute
     school_name = "Parent school name"   #overriding parent class attribute

     def get_School_name2(self):     # different method not the method of parent class
         return self.school_name     #accessing Parent class attribute
         #return "Parent class high school name"

     def get_name_capitalize(self):      # override method (method of derived class) and is indicated with blue circle sign in python
         original_value = super().get_name_capitalize()   # "Super" keyword refers to parent class, it looks for 'get_name_capitalize' method in the parent class and access it
         return original_value + "HighSchool Student"

falgun = HighSchoolStudent("falgun")    #falgun is HighSchool student

print(falgun.get_name_capitalize())    # accessing override method or the method of parent class through the derived class instance- falgun
print(falgun.get_School_name())        # accessing override method or the method of parent class through the derived class instance- falgun
print(falgun.get_School_name2())       # accessing derived class method
print(falgun.school_name)              # accessing parent class attribute
print(falgun.HighSchool_name)          # accessing derived class attribute

