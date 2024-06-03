mealoption1 = 0
mealoption2 = 0


def MealCount(Option):
    global mealoption1
    global mealoption2
    if Option == 1 or Option == 2:
        if Option == 1:
            mealoption1 = mealoption1 + 1
        else:
            mealoption2 += 1
        MealCount(int(input("Enter the meal option 1 or 2: ")))
    else:
        print(
            "The number of meal option 1 selected is",
            mealoption1,
            "The number of meal option 2 selected is ",
            mealoption2,
        )


optionselected = int(input("Enter the meal option 1 or 2: "))
MealCount(optionselected)
