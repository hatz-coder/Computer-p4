# TYPE Student
# DECLARE Stname: STRING
# DECLARE Age: INTEGER
# DECLARE Id : INTEGER
# ENDTYPE


class Student:
    def __init__(self, Stname, Age, ID):
        self.Stname = Stname
        self.Age = Age
        self.ID = ID


Cedar = [Student("", 0, 0) for i in range(4)]
# for x in range(len(Cedar)):
#     Cedar[x].Stname = input("enter name of student")
#     Cedar[x].ID = int(input("enter id of student"))
#     Cedar[x].Age = int(input("enter age of student"))

Cedar[0].Stname = "hatz editz"
Cedar[0].Age = 49
Cedar[0].ID = 2001

Cedar[1].Stname = "gello mello"
Cedar[1].Age = 42
Cedar[1].ID = 2002

Cedar[2].Stname = "aka editz"
Cedar[2].Age = 48
Cedar[2].ID = 2003

Cedar[3].Stname = "han editz"
Cedar[3].Age = 49
Cedar[3].ID = 2004


SearchID = int(input("enter id to be searched:"))
found = False
Index = 0
while found == False and Index < len(Cedar):
    if Cedar[Index].ID == SearchID:
        print("Name: ", Cedar[Index].Stname)
        print("Age of Student: ", Cedar[Index].Age)
        found = True
    else:
        Index = Index + 1
if found == False:
    print("ID not found")
