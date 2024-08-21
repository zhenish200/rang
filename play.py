class Employees:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def get_info(self):
        return f"'{self.name}', {self.age}, '{self.country}'"

class Manager(Employees):
    def __init__(self, name, age, country, department):
        super().__init__(name, age, country)
        self.department = department

    def get_info(self):
        return f"'{self.name}', {self.age}, '{self.country}', '{self.department}'"

    def check_dep(self):
        if self.department == 'IT':
            return "Cool"
        else:
            return "No cool"

class Intern(Manager):
    def __init__(self, name, age, country, department, salary, experience):
        super().__init__(name, age, country, department)
        self.salary = salary
        self.experience = experience

    def get_info(self):
        return f"'{self.name}', {self.age}, '{self.country}', '{self.department}', {self.salary}, {self.experience}"

    def total_salary(self):
        som_conversion_rate = 36
        return self.salary * som_conversion_rate * self.experience


empl1 = Employees('Aidana', 44, 'KG')
print(empl1.get_info())

manag1 = Manager('Asel', 22, 'KZ', 'Marketing')
print(manag1.get_info())
print(manag1.check_dep())

intern1 = Intern('Bektur', 22, 'USA', 'Marketing', 45000, 3)
print(intern1.get_info())
print(intern1.check_dep())
print(intern1.total_salary())
