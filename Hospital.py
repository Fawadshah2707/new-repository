import json

class Hospital():
    
    def __init__(self, name : str , age, cnic, number, sex : str):
        self.number = number
        self.sex = sex
        self.age = age
        self.cnic = cnic
        self.name = name
        self.hospital_name = "HEALTH CARE HOSPITAL"
        self.location = "NOWHERE"
        self.capacity = "BED : 500 "
        self.doctors_list = {}
        self.patient_list = {}
        
        

        
    def add_doctor(self):
        self.doctors_list.append({self.name:{"name": self.name,"sex": self.sex,"disease ": self.disease,"contact": self.contact}})
                                    

        
    def remove_doctor(self):
        self.doctors_list.remove(self.name)

        
    def add_patient(self):
        self.patient_list.append({self.name:{"name": self.name,"sex": self.sex,"disease ": self.disease,
                                    "contact": self.contact}})
    def patient_detail(self):
        self.patient_list[self.name]
    
    def patient_detail(self):
        self.doctors_list[self.name]
        



    def remove_patient(self):
            self.patient_list.remove(self.name)
   
   


   #---------------------------PATIENT-----------------------------------#
 
    
    
    
    
class Patient(Hospital):
    def __init__(self, disease,reffered_doctor ) :
        super().__init__(self)
        self.disease = disease
        self.previous_record = []
        self.reffered_to_doctor = reffered_doctor   
            



#--------------------------------DOCTOR----------------------------------#



class Doctor(Hospital):
    def __init__(self, speciality : str , availability:str):
        super().__init__(self)
        
        self.specility = speciality
        self.availability = availability
    

    def access_data(self):
        print(f"Name : {self.name} ,speciality : {self.specility},Availability : {self.availability}")


    def update_data(self):
        self.name = input("name : ")
        self.specility = input("speciality : ")
        self.availability = input("availibility : ")

    
    def get_speciality(self):
        return print(f"speciality {self.specility}")  
    




#---------------------------APPOINTMENT--------------------------------#
    


class Appointment(Hospital):
    def __init__(self) :
        super().__init(self )
             

        

    def print_reciept():
        print(f"""Patient Name : {Patient.__name}
                  Age : {Patient.age}
                  Sex : {Patient.sex}
                  Cnic : {Patient.cnic}
                  Contact Number :{Patient.number}  
                  Disease : {Patient.disease}
                  Reffered To : Dr.{Doctor.name}
                  Previous Record : {(Hospital.patient_list[Patient.name])}
                  

        





""")              

 

        