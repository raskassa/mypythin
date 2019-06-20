#creating my first python class
class myseconndclass:
    def __init__(self, fname, lname):
        self.f = fname
        self.l = lname
    def printing (self):
        print(self.f)
        print(self.l)

class myPyClass:
    def __init__ (self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printing (self, ffname, llname):
        print("your first name is: " + self.firstname + " and your last name is : " + self.lastname )
        print("your kids are: " + ffname + "and " + llname )

y = myseconndclass ("Liz", "Asmare")
y.printing()
x = myPyClass("Mekonnen", "Kassa")
x.printing("heron", "sarah")
