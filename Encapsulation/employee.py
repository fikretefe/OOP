class Employee:

    def __init__(self, emp_id, salary):
        self.__emp_id = emp_id

        if salary > 0:
            self.__salary = salary
        else:
            print("Geçersiz maaş değeri.")
            self.__salary = 0

    def get_emp_id(self):
        return self.__emp_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Maaş 0'dan büyük olmalıdır.")

    def raise_salary(self, percentage):
        if 0 < percentage <= 10:
            self.__salary += self.__salary * (percentage / 100)
        else:
            print("Zam oranı %0 ile %10 arasında olmalıdır.")

    def calculate_bonus(self):
        return self.__salary * 0.10

    def get_status(self):
        if self.__salary >= 10000:
            return "Yüksek Maaşlı Çalışan"
        else:
            return "Standart Çalışan"


employee = Employee(1, 10000)

print("ID:", employee.get_emp_id())
print("Maaş:", employee.get_salary())
print("Durum:", employee.get_status())

employee.raise_salary(9)

print("Yeni Maaş:", employee.get_salary())
print("Bonus:", employee.calculate_bonus())
print("Durum:", employee.get_status())