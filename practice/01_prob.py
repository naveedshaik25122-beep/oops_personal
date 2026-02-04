# creating a class for student names
class Student:
    #default contructors
    def __init_subclass__(self):
        pass
    # paramterized contructors
    def __init__(self, name, marks):
        # self is a variable that is used to tag the object at the time it is used
        # we can write anything in the place of self
        self.name = name
        self.marks=marks
        print("adding a new student")
s1= Student("mubashir", 39)
print(s1.name,s1.marks)
s2 = Student("sohail", 85)
print(s2.name,s1.marks)
a1 = Student("arshad shaik", 40)
print(a1.name, s1.marks)

# the self parameter is a reference to the current
# instace of the class, and is used to access variables 
#that belongs to the class.
