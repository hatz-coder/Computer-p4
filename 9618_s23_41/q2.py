class Vehicle:
    def __init__(self, ID1, maxSpeed1, increaseAmount1):
        self.__Id = ID1  # DECLARE Id: STRING
        self.__maxSpeed = maxSpeed1  # DECLARE maxSpeed:INTEGER
        self.__increaseAmount = increaseAmount1  # DECLARE increaseAmount:INTEGER
        self.__currentSpeed = 0
        self.__horizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.__currentSpeed

    def GetIncreaseAmount(self):
        return self.__increaseAmount

    def GetMaxSpeed(self):
        return self.__maxSpeed

    def GetHorizontalPosition(self):
        return self.__horizontalPosition

    def SetCurrentSpeed(self, Speed):
        self.__currentSpeed = Speed

    def SetHorizontalPosition(self, Position):
        self.__horizontalPosition = Position

    def IncreaseSpeed(self):

        Vehicle.SetCurrentSpeed(
            self, Vehicle.GetCurrentSpeed(self) + self.__increaseAmount
        )
        if Vehicle.GetCurrentSpeed(self) > self.__maxSpeed:
            Vehicle.SetCurrentSpeed(self, self.__maxSpeed)
        Vehicle.SetHorizontalPosition(
            self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self)
        )

        # if self.__currentSpeed + self.__increaseAmount <= self.__maxSpeed:
        #     self.__currentSpeed += self.__increaseAmount
        #     self.__horizontalPosition += self.__currentSpeed

    def Output(self):
        print("The speed of car is ", self.__currentSpeed)
        print("The position of car is ", self.__horizontalPosition)
        return self.__currentSpeed
        return self.__horizontalPosition


class Helicopter(Vehicle):
    def __init__(self, ID1, maxSpeed1, increaseAmount1, verticalChange1, maxHeight1):
        super().__init__(ID1, maxSpeed1, increaseAmount1)
        self.__Id = ID1  # DECLARE Id: STRING
        self.__maxSpeed = maxSpeed1  # DECLARE maxSpeed:INTEGER
        self.__increaseAmount = increaseAmount1  # DECLARE increaseAmount:INTEGER
        self.__verticalChange = verticalChange1  # DECLARE verticalChange:INTEGER
        self.__maxHeight = maxHeight1  # DECLARE maxHeight:INTEGER
        self.__verticalPosition = 0

    def GetVerticalPosition(self):
        return self.__verticalPosition

    def IncreaseSpeed(self):
        Vehicle.SetCurrentSpeed(
            self, Vehicle.GetCurrentSpeed(self) + self.__increaseAmount
        )
        if Vehicle.GetCurrentSpeed(self) > self.__maxSpeed:
            Vehicle.SetCurrentSpeed(self, self.__maxSpeed)

        Vehicle.SetHorizontalPosition(
            self, Vehicle.GetHorizontalPosition(self) + Vehicle.GetCurrentSpeed(self)
        )
        if (
            Helicopter.GetVerticalPosition(self) + self.__verticalChange
        ) > self.__maxHeight:
            self.__verticalPosition = self.__maxHeight
        else:
            self.__verticalPosition = self.__verticalPosition + self.__verticalChange

    def Output(self):
        print("The vertical position of heli is ", self.__verticalPosition)
        print("The speed of heli is ", Vehicle.GetCurrentSpeed(self))
        print(
            "The horizontal position of heli is ", Vehicle.GetHorizontalPosition(self)
        )


Car = Vehicle("Tiger", 100, 20)
Helicopter1 = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.Output()
Helicopter1.IncreaseSpeed()
Helicopter1.IncreaseSpeed()
Helicopter1.Output()
