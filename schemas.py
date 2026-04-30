from pydantic import BaseModel

class NutritionResult(BaseModel):
    calories: int
    protein_g: int
    carbs_g: int
    fats_g: int
    summary: str
