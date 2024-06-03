class Employee:
    def __init__(self, hourlyrateP, EmployeeNoP, jobtitleP):
        self.HourlyPay = hourlyrateP  # REAL
        self.EmployeeNumber = EmployeeNoP  # STRING
        self.JobTitle = jobtitleP  # STRING
        self.Payyear2022 = [0.0] * 52  # ARRAY[0:51] OF REAL

    def GetEmployeeNumber(self):
        return self.EmployeeNumber

    def SetPay(self, weeknumberp, hoursworkedp):
        pay = self.HourlyPay * hoursworkedp
        self.Payyear2022[weeknumberp] = pay

    def GetTotalPay(self):
        total = 0
        for x in range(len(self.Payyear2022)):
            total += self.Payyear2022[x]
        return int(total)


class Manager(Employee):

    def __init__(self, HourlyPay, EmployeeNumber, JobTitle, BonusValuep):
        super().__init__(HourlyPay, EmployeeNumber, JobTitle)
        self.Bonusvalue = BonusValuep  # STRING

    def SetPay(self, weeknump, hoursworkedp):
        newhours = hoursworkedp * self.Bonusvalue
        return super().SetPay(weeknump, newhours)


EmployeeArray = [] * 8
file = open("Employees.txt", "r")
for x in range(8):
    hourrate = float(file.readline().strip())
    EmployeeNo = int(file.readline().strip())
    temp1 = file.readline().strip()
    try:
        temp = float(temp1)
        JobTitle = file.readline().strip()
        # print(JobTitle)
        EmployeeArray.append(Manager(hourrate, EmployeeNo, JobTitle, temp))
    except:
        EmployeeArray.append(Employee(hourrate, EmployeeNo, temp1))
        # print("here")
file.close()


def EnterHours():
    file = open("HoursWeek1.txt", "r")
    for x in range(8):
        ID = int(file.readline().strip())
        hours = float(file.readline().strip())
        x = 0
        for i in range(8):
            if ID == EmployeeArray[i].GetEmployeeNumber():
                EmployeeArray[i].SetPay(0, hours)
                print("Added")

    file.close()


EnterHours()
for i in range(8):
    print(
        str(EmployeeArray[i].GetEmployeeNumber())
        + " "
        + str(EmployeeArray[i].GetTotalPay())
    )
