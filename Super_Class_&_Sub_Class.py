# Super Class & Super Class

class car:
    superString = "Class value of car"
    def __init__(self):
        print("Intance object of Car is created")
    def superMethod(self):
        print("Method of Car is called")

class LuxeriousCar (car):
    subString = "Class variable of LuxeriousCar"
    def __init__(self):
        print("Intance object of LuxeriousCar is created")
    def subMethod(self):
        print("Method of LuxeriousCar is called")

class SubLexeriousCar (LuxeriousCar):
    def __init__(self):
        print("Intance object of SubLuxeriousCar is created")
    def subSubMethod(self):
        print("Method of SubLuxeriusCar is Called")

subSubcar = SubLexeriousCar()
subSubcar.superMethod()
subSubcar.subMethod()
subSubcar.subSubMethod()