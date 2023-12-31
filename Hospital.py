import json

class Hospital():
    
    def __init__(self, name, age, cnic, number,sex) :
        self.number = number
        self.sex = sex
        self.age = age
        self.cnic = cnic
        self.name=name
        self.hospital_name = "HEALTH CARE HOSPITAL"
        self.location = "NOWHERE"
        self.capacity = "BED : 500 "
        self.doctors_list = []
        self.patient_list = []
        
        
        def set___location(self):
            self.__location = input("location")

        
        def get__location(self):
            print(f"LOCATION : {self.__location}" )

        
        def add_doctor(self):
            self.name = input("name : ")
            doctors_list.append(name)

        
        def remove_doctor(self):
            pass

        
        def doctors_list(self):
            print(self.doctors_list)
        

        def doctor_detail(self):
            print(self.name)

 
        
          