class Student:
    def __init__(self, name, age, grade, subscribed_course):
        self.name = name
        self.age = age
        self.grade = grade
        self.subscribed_course = subscribed_course
        self.homeworks = []

    def addHomework(self, homework):
        self.homeworks.append(homework)

    def changeHomeworkStatus(self, homework, status):
        for hwork in self.homeworks:
            if hwork.name == homework.name:
                hwork.status = status

    def showStudentInfo(self):
        strInfo = ""
        strInfo += f"{self.name} ---> age: {self.age}---> grade: {self.grade}---> subscribed_course: {self.subscribed_course}\n"
        for hwork in self.homeworks:
            strInfo += hwork.showHomeworkInfo()
        return strInfo


class Homework:
    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status

    def showHomeworkInfo(self):
        return f"{self.name} ---> description: {self.description}---> complexity: {self.complexity}---> status: {self.status}\n"


class Table:

    def __init__(self):
        self.students = []

    def addStudent(self, student):
        self.students.append(student)

    def showStudentInfoFromTable(self):
        strInfo = ""
        for student in self.students:
            strInfo += f"{student.name}---> age: {student.age}\n"
            for hwork in student.homeworks:
                strInfo += hwork.showHomeworkInfo()
        return strInfo


tableOfStudents = Table()
arr_students = []
student_1 = Student("Corey", 31, "A", "Math")
student_2 = Student("Shawn", 32, "B", "C++")
student_3 = Student("Craig", 33, "A", "Python")
student_4 = Student("Mick", 34, "C", "Math")
student_5 = Student("Sid", 35, "A", "Design")


arr_students.append(student_1)
arr_students.append(student_2)
arr_students.append(student_3)
arr_students.append(student_4)
arr_students.append(student_5)

homework_1 = Homework("Math", "Math", "easy", "not")
homework_2 = Homework("C++", "C++", "easy", "not")

for stud in arr_students:
    stud.addHomework(homework_1)
    stud.addHomework(homework_2)


#Change homework status
print(student_1.showStudentInfo())
student_1.changeHomeworkStatus(homework_1, "passed")
print(student_1.showStudentInfo())


for stud in arr_students:
    tableOfStudents.addStudent(stud)

print(tableOfStudents.showStudentInfoFromTable())
print("_________________________________________")


student_6 = Student("James", 33, "A", "Math")
student_7 = Student("Joey", 31, "D", "C#")


student_6.addHomework(homework_1)
student_7.addHomework(homework_2)

tableOfStudents.addStudent(student_6)
tableOfStudents.addStudent(student_7)
print(tableOfStudents.showStudentInfoFromTable())