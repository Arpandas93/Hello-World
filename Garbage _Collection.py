class Person:
    totalperson=0
    def __init__(self, name, age, mobilenumber):
        Person.totalperson+=1
        self.name= name
        self.age= age
        self.mobilenumber= mobilenumber
        print("Person Count :", Person.totalperson)

    def __del__(self):
        Person.totalperson-=1


    def displayparameters (self):
        print("Person Name :", self.name)
        print("Person Age :", self.age)
        print("Person Mobile Number :", self.mobilenumber)
        print()

Person1 = Person("Arpan", "27", 9593953513)
Person1.displayparameters()

Person2 = Person("Hiranmoy Biswas", "27", 7001841674)
Person2.displayparameters()

Person3= Person("sham", "32", 9002306685)
Person3.displayparameters()

Person4 = Person("Rose", "29", 8759637130)
Person4.displayparameters()

print("Total number before del", Person.totalperson)
del Person4
print("Total number after del", Person.totalperson)
