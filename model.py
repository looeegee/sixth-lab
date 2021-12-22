from datetime import date, datetime
class User:
    def __init__(self, name, last_name, address, gender, birth_date, start_date=date.today()):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.gender = gender
        self.birth_date = birth_date
        self.start_date = start_date
    def __str__(self):
        return f"{self.name} {self.last_name} {self.address[0]} {self.address[1]} {self.address[2]} {self.gender} {self.birth_date} {self.age()} y.o."
    def age(self):
        return ((self.start_date - self.birth_date).days)//365

