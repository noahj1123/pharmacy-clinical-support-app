from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PatientCreate(BaseModel):
    first_name: str
    last_name: str

patients = [
    {"id": 1, "first_name": "John", "last_name": "Doe"},
    {"id": 2, "first_name": "Maria", "last_name": "Garcia"}
]

@app.get("/")
def home():
    return {"message": "Pharmacy Clinical Support API is running"}


@app.get("/patients")
def get_patients():
    return patients

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            return patient
    
    raise HTTPException(status_code=404, detail="Patient not found.")

@app.post("/patients")
def create_patient(patient: PatientCreate):
    new_id = len(patients) + 1
    new_patient = {
        "id":new_id,
        "first_name": patient.first_name,
        "last_name" : patient.last_name
        
        }
    patients.append(new_patient)

    return new_patient

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            return {"message": "Patient has been removed successfully"}
        
    raise HTTPException(status_code=404, detail= "Patient not found.")

@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, patient_update: PatientCreate):
    for patient in patients:
        if patient["id"] == patient_id:

            patient["first_name"] = patient_update.first_name
            patient["last_name"] = patient_update.last_name