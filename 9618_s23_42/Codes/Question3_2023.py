class Employee():
    #PRIVATE HourlyPay : REAL
    #PRIVATE EmployeeNumber : STRING
    #PRIVATE JobTitle : STRING
    #PRIVATE PayYear2022 : ARRAY[0:51] OF REAl
    def __init__(self, HourlyPayP, EmployeeNumberP, JobTitleP):
        self.__HourlyPay = HourlyPayP
        self.__EmployeeNumber = EmployeeNumberP
        self.__JobTitle = JobTitleP
        self.__PayYear2022 = [0.0] * 52

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, WeekNumber, Hourworked):
        Pay = self.__HourlyPay * Hourworked
        self.__PayYear2022[WeekNumber - 1] = Pay

    def GetTotalPay(self):
        Total = 0
        for x in range(52):
            Total = Total + self.__PayYear2022[x]

        return Total

class Manager(Employee):
    #PRIVATE BonusValue : REAL
    def __init__(self, HourlyPayP, EmployeeNumberP, JobTitleP, BonusValueP ):
        super().__init__(HourlyPayP, EmployeeNumberP, JobTitleP)
        self.__BonusValue = BonusValueP

    def SetPay(self, WeekNumber, Hourworked):
        NewHours = Hourworked + (Hourworked * (self.__BonusValue/100))
        super().SetPay(WeekNumber, NewHours)

#DECALRE EmplyeeArray : ARRAY[0:7] OF Employee
EmployeeArray = [Employee(0.0, "", "")] * 8

MaybeBonus = "" # Junior Developer
JobTitle = ""
try:
    Employeefile = open("Employees.txt", "r")
    for x in range(8):
        HourlyPay = float(Employeefile.readline().strip())
        EmployeeNumber = Employeefile.readline().strip()
        MaybeBonus = Employeefile.readline().strip()
        try:
            Bonus = float(MaybeBonus) # float("Junior Developer")
            JobTitle = Employeefile.readline().strip()
            EmployeeArray[x] = Manager(HourlyPay, EmployeeNumber, JobTitle, Bonus)
        except:
            JobTitle = MaybeBonus
            EmployeeArray[x] = Employee(HourlyPay, EmployeeNumber, JobTitle)

    Employeefile.close()
except IOError:
    print("File Not Found")

def EnterHours():
    try:
        HoursFile = open("HoursWeek1.txt", "r")
        for x in range(8):
            EmployeeID = HoursFile.readline().strip()
            Hoursworked = float(HoursFile.readline().strip())
            for y in range(8):
                if EmployeeArray[y].GetEmployeeNumber() == EmployeeID:
                    EmployeeArray[y].SetPay(1, Hoursworked)
        HoursFile.close()
    except IOError:
        print("File Does Not Exist")

EnterHours()
for x in range(8):
    EmployeeNumber = EmployeeArray[x].GetEmployeeNumber()
    TotalPay = EmployeeArray[x].GetTotalPay()
    print(EmployeeNumber + " "  + str(TotalPay))






