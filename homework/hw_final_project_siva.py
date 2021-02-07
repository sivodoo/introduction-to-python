# Final Project - Sivakumar
#
class Employee():
  def __init__(self, Name, Age):
    self.name = Name
    self.age = Age
    self.lang = []

  def print_lang(self):
    print("Employee :", self.name, " can speak the following languagers:")
    for i in self.lang:
        print(i)

  def add_lang(self, nlang):
    self.lang.append(nlang)

class Manager(Employee):
   pass    


Emp1 =Employee("Joe", 40)
Emp1.add_lang("Spanish")
Emp1.add_lang("English")
Emp2 = Employee("Jack", 35)
Emp2.add_lang("French")
Emp3 = Employee("Frank", 50)
Emp3.add_lang("English")
Emp3.add_lang("Taglog")
Mgr1 = Manager("Jim", 45)
Mgr1.add_lang("English")
Mgr1.add_lang("Spanish")
Mgr1.add_lang("French")

Emp1.print_lang()
Emp2.print_lang()
Emp3.print_lang()
Mgr1.print_lang()
