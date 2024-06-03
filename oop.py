class Employee:
    def __init__(self, Name, ID, amountPaidThisMonth):
        self.__employeeName = Name
        self.__employeeID = ID
        self.__amountPaidThisMonth = amountPaidThisMonth

    def setEmployee(self, name):
        self.__employeeName = name

    def setEmployeeID(self, ID):
        self.__employeeID = ID

    def __del__(self):
        print("Object destroyed")

    def payment(self):
        return (
            self.__employeeName
            + " with ID: "
            + str(self.__employeeID)
            + " has been paid "
            + str(self.__amountPaidThisMonth)
            + " dollars this month."
        )


Employee1 = Employee("John", 123, 1000)
print(Employee1.payment())
del Employee1
# print(Employee1.payment())
