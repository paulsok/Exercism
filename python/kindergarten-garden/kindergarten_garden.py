students_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                 "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

plant_dict = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


class Garden:
    def __init__(self, diagram, students=students_list):
        self.diagram = diagram.split()
        self.students = sorted(students)
        self.student_plant = {}

        for student in self.students:
            stud_index = self.students.index(student) * 2
            for i in self.diagram[0][stud_index:stud_index + 2] + self.diagram[1][stud_index:stud_index + 2]:
                self.student_plant.setdefault(student, []).append(plant_dict[i])

    def plants(self, student_name):
        return self.student_plant[student_name]
