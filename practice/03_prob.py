# create student class that takes name and marks of 3 subjects as argumrents in cnstructer
# then create a method to print the averege 
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum = sum +i
        print("hi", self.name, "your average is", sum/3 )


s1=student("karan",[99,40,80])
s1.get_avg()
s1.name = "ironman"
s1.get_avg()
# we can able to maniout=let the clases and objects
