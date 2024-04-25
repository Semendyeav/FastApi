from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class MlModelInput(BaseModel):
    year: float
    mileage: float
    brand: str
    model: str
    color: str
    state: str
