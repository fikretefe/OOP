class Student:

    def __init__(self, student_id, gpa):
        self.__student_id = student_id

        if 0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            print("Geçersiz GPA değeri.")
            self.__gpa = 0

    def get_student_id(self):
        return self.__student_id

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if 0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            print("GPA değeri 0 ile 4 arasında olmalıdır.")

    def is_successful(self):
        return self.__gpa >= 2.0

    def get_status(self):
        if self.__gpa >= 2.0:
            return "Başarılı"
        else:
            return "Başarısız"


student = Student("34Academy001", 3.1)

print("Öğrenci No:", student.get_student_id())

student.set_gpa(4.0)

print("Yeni GPA:", student.get_gpa())
print("Durum:", student.get_status())