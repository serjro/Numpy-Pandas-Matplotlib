class Worker:
    def __init__(self, name, surname,position,wage,bonus):
        self.name = name
        self.surname = surname
        self.position=position
        self._income={"profit":wage,"bonus":bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name+" "+self.surname
    def get_total_income(self):
        return self._income.get("profit")+self._income.get("bonus")

salary=Position("Ivan","Ivanov","seller",30000,5000)
print(f"{salary.get_full_name()} {salary.position} {salary.get_total_income()}")

