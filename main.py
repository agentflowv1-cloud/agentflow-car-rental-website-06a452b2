import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Car(BaseModel):
    id: int
    name: str
    description: str

cars = [
    Car(id=1, name='Toyota', description='Toyota is a Japanese car manufacturer'),
    Car(id=2, name='Ford', description='Ford is an American car manufacturer'),
    Car(id=3, name='Honda', description='Honda is a Japanese car manufacturer')
]

@app.get('/api/cars/')
async def read_cars():
    return JSONResponse(content=[car.dict() for car in cars], media_type='application/json')

@app.get('/api/cars/{car_id}')
async def read_car(car_id: int):
    car = next((car for car in cars if car.id == car_id), None)
    if car is None:
        return JSONResponse(content={'error': 'Car not found'}, status_code=404, media_type='application/json')
    return JSONResponse(content=car.dict(), media_type='application/json')

if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get('PORT', 8080))
    uvicorn.run(app, host='0.0.0.0', port=port)