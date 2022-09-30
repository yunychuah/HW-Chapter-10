import EmployeeClass as a
import PayrollDeductionClass as b

def main():

    employee = a.Employee('Jimmy Smith','58475','Information Systems','Developer',6800)
    deductions = [b.payroll_deduction('food court','8/14/2022',22.50,'39119') 
    ,b.payroll_deduction('gift contribution','8/12/2022',25.00,'58475')
    ,b.payroll_deduction('food court','8/17/2022',15.25,'21547')
    ,b.payroll_deduction('vending machine','8/22/2022',3.00,'58475')
    ,b.payroll_deduction('vending machine','8/5/2022',2.75,'58475')]
   
    print('***Employee Pay***')
    employee.print_employee()
    
    balance = employee.get_salary()
    for i in deductions:
        employee_id = employee.get_id()
        if employee_id == i.get_employee_id(): 
            balance = balance - i.get_charge()         
    print('Net Pay:','$', balance)
main()