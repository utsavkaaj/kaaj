from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Investment(BaseModel):
    amount: int
    region: str
    industry: str

@app.get("/investment")
async def get_investment():
    # This would fetch real data from your database
    return Investment(amount=2000000, region="United States", industry="B2B SaaS")


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}