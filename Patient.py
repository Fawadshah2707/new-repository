import Hospital

class Patient(Hospital):
    def __init__(self , disease , previous_record) :
        self.disease = disease
        self.previous_record = previous_record


    def set__disease(self):
        self.disease = input("Disease : ")   



        


            