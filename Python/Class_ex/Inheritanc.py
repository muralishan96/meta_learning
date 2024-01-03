class Employess:
    def __init__(self,name,last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employess):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employess):
    def leave_request(self,days):
        return "May I take a leave for "+ str(days) +" days"
    
murali = Supervisors('Murali','A','apple')

suganya = Chefs('Suganya',"E")
amma = Chefs("Amma",'J')
print(suganya.leave_request(4))
print(murali.password)
print(suganya.name)