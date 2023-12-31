import Hospital

class Doctor(Hospital):
    def __init__(self, speciality, availability):
        super().__init__(self)
        
        self.specility = speciality
        self.availability = availability
    

    def access_data(self):
        print(f"Name : {self.name} ,
              speciality : {self.specility},
              Availability : {self.availability}")


    def update_data(self):
        self.name = input("name : ")
        self.specility = input("speciality : ")
        self.availability = input("availibility : ")

    

    def get_speciality(self):
        return print(f"speciality {self.specility}")   