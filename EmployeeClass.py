class Employee:
    def __init__(self,name,id,department,job,salary):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__job = job
        self.__salary = salary
    
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id
    
    def set_department(self, department):
        self.__department = department

    def set_job(self, job):
        self.__job = job

    def set_salary(self, salary):
        self.__salary = salary
    
    def get_id(self):
        return self.__id
    
    def get_salary(self):
        return self.__salary

    def print_employee(self):

        print('Name:',self.__name)
        print('ID Number:',self.__id)
        print('Department:',self.__department)
        print('Gross Pay:',self.__salary)
    
    