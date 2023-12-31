import Hospital
import Patient
import Doctor
import Record
import datetime
import json

class Appointment(Hospital):
    def __init__(self) :
        super().__init(self )
        with open("record.json","r") as record:
            previous_record =  json.load(record)
            print(previous_record)

    def print_reciept():
        print(f"""Patient Name : {Patient.__name}
                  Age : {Patient.age}
                  Sex : {Patient.sex}
                  Cnic : {Patient.cnic}
                  Contact Number :{Patient.number}  
                  Disease : {Patient.disease}
                  Referred To : Dr.{Doctor.name}
                  Previous Record: {previous_record}
                  

        





""")              

 

        
