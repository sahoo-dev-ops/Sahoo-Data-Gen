from fastapi import FastAPI, Query
from faker import Faker

app = FastAPI()

# Welcome endpoint
@app.get('/')
def root():
    return {"message": "Welcome to QuantFuel Backend"}

faker = Faker()

# Data generation endpoint
@app.get('/generate-data')
def generate_data(record_count: int = Query(10, description="Number of records to generate")):
    data = [{"name": faker.name(), "email": faker.email(), "address": faker.address()} for _ in range(record_count)]
    return {"data": data}