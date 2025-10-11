####################################################
# CS 22, Prof. Muldrow
# Name: Polina Chetnikova
# Assignment: Week 3 HW
# Due Date: October 12 2025 
####################################################

class Employee:
    def __init__(self, name, num):
        self.__employee_name = name
        self.__employee_number = num

    #Setter Functions
    def set_employeeName(self, name):
        self.__employee_name = name
    
    def set_employeeNumber(self, num):
        self.__employee_number = num

    #Getter Functions
    def get_employeeName(self):
        return self.__employee_name
    
    def get_employeeNumber(self):
        return self.__employee_number

#Production Worker class inherits from Employee class
class ProductionWorker(Employee):
    def __init__(self, name, num, shift, pay):
        Employee.__init__(self, name, num)

        self.__shift_number = shift
        self.__hourly_pay_rate = pay

    #Setter functions for ProductionWorker Attributes
    def set_shiftNumber(self, shift):
        self.__shift_number = shift

    def set_hourlyPayRate(self, pay):
        self.__hourly_pay_rate = pay
    
    #Getter functions for ProductionWorker Attributes
    def get_shiftNumber(self):
        return self.__shift_number
    
    def get_hourlyPayRate(self):
        return self.__hourly_pay_rate
    
#Shift Supervisor class inherits from the Employee class
class ShiftSupervisor(Employee):
    def __init__(self, name, num, salary, bonus):
        super().__init__(name, num)

        self.__yearly_salary = salary
        self.__annual_bonus = bonus

    #Setter functions for ShiftSupervisor attributes
    def set_yearly_salary(self, salary):
        self.__yearly_salary = salary

    def set_annual_bonus(self, bonus):
        self.__annual_bonus = bonus
    
    #Getter function for ShifySupervisor attributes
    def get_yearly_salary(self):
        return self.__yearly_salary
    
    def get_annual_bonus(self):
        return self.__annual_bonus
    
def main():
    #Get user input for production worker
    #name = input("Enter name of production worker: ")
    #empNumber = input("Enter the employee number: ")
    #shiftNumber = input("Enter 1 for first shift, 2 for second shift, or 3 for third shift: ")
    #hourlyPay = input("Enter hourly pay rate: ")

    #Create instance of production worker with user input
    #worker = ProductionWorker(name, empNumber, shiftNumber, hourlyPay)
    #print(f"{worker.get_employeeName()} (employee #{worker.get_employeeNumber()}) works shift {worker.get_shiftNumber()} and makes ${worker.get_hourlyPayRate()} per hour.")


    #Get user input for shift supervisor
    supName = input("Enter name of supervisor: ")
    supNumber = input("Enter the employee number: ")
    salary = float(input("Enter yearly salary: "))
    bonus = float(input("Enter bonus amount: "))
    
    supervisor = ShiftSupervisor(supName, supNumber, salary, bonus)
    print(f"{supervisor.get_employeeName()} (employee #{supervisor.get_employeeNumber()})",
          f"makes ${supervisor.get_yearly_salary():.2f} per year",
          f"and could get a bonus of ${supervisor.get_annual_bonus():.2f}")

main()
        