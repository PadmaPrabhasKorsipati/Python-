
class student:

    year=2024

    num_students=0


    def __init__(self,name,age):
        
        self.name=name
        self.age=age

        self.num_students+=1

    
student1=student("Spongebob",23)
student2=student("patrick",27)
student3=student("squidward",31)
student4=student("sandy",33)

print(f" My Graduating class of {student.year} year has {student.num_students} students.")

    













