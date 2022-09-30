class payroll_deduction:
    def __init__(self,description,date,charge,id):
        self.__description = description
        self.__date = date
        self.__charge = charge
        self.__employee_id = id
    
    def set_description(self,description):
        self.__description = description
    
    def set_date(self,date):
        self.__date = date
    
    def set_charge(self,charge):
        self.__charge = charge
    
    def set_employee_id(self,id):
        self.__employee_id = id
    
    def get_employee_id(self):
        return self.__employee_id
    
    def get_charge(self):
        return self.__charge
    
    
        
