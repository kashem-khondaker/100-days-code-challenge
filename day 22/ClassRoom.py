class ClassRoom:
    def __init__(self , name):
        self.name = name
        self.students = []
        self.subjects = []
        
        
    def add_student(self , student):
        roll_no = f'{self.name} - {len(self.students)+1}'
        student.id = roll_no
        self.students.append(student)
    
    
    def add_subject(self , subject):
        self.subjects.append(subject)
        
        
    def take_semester_final_exam(self):
        
        for subject in self.subjects:  # protita subject a exam dibe protita student
            subject.exam(self.students)
        
        for student in self.students: # protita student er er final grade calculate kora hobe
            student.calculate_final_grade()
        
    