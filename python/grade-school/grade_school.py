class School:
    def __init__(self):
        self.grades = {}
        self.journal = []

    def add_student(self, name, grade):
        self.grades.setdefault(grade, []).append(name)

    def roster(self):
        for grades in sorted(self.grades.keys()):
            self.journal += self.grade(grades)

        return self.journal

    def grade(self, grade_number):
        return sorted(self.grades.setdefault(grade_number, []))
