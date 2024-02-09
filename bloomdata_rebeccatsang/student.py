import random
"""
This is the parent class.
"""
class Student:
    """
    These are the attributes.
    """
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    """
    These are the methods.
    """
    def years_in_school(self, start_age):
        return self.age - start_age
    
    def encouragement(self):
        return "You can do it!"
    

"""
This is the child class.
"""
class BloomTechStudent(Student):
    """
    Attribute
    """
    def __init__(self, name, age, school, track, cohort):
        super().__init__(name, age, school)
        self.track = track
        self.cohort = cohort

    """
    Method
    """
    def welcome(self, name):
        return f"Hi, {name}, welcome to the {self.cohort} cohort."

    def __repr__(self):
        return f"{self.name}, {self.age} year old from {self.school} in the {self.track} {self.cohort} cohort"


    def student_generator(num_students=30):
        """
        write a function called student_generator that will 
        randomly generate values for your Bloomtech student's attributes. 
        Create 30 different randomly generated Bloomtech students and add them to a list.
        """
        first_names = ['Arthur', 'Becky', 'Darrel', 'Eric', 'Francine', 'Gary']
        last_names = ['Adams', 'Brown', 'Douglas', 'Evans', 'Farnsworth', 'Gunderson']

        random_first_name = random.choice(first_names)
        random_last_name = random.choice(last_names)

        random_name = random_first_name + ' ' + random_last_name

        age = random.randint(18, 100)

        school = 'BloomTech'
        
        track = random.choice(['WEB', 'DS', 'Backend'])

        cohort = random.randint(1, 50)

        students = []
        for _ in range(num_students):
            students.append(BloomTechStudent(random_name, age, school, track, cohort))
        return students

    student_list = student_generator(2)
        
if __name__ == '__main__':
    my_student = BloomTechStudent("Reb Tsang", "39", "BloomTech", "DS", "9")
    print(my_student)
    print(my_student.name)
    print(my_student.age)
    print(my_student.school)
    print(my_student.track)
    print(my_student.cohort)
    print(my_student.encouragement())
    print(my_student.welcome("Rebecca"))
    print(student_list)