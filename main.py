from fastapi import FastAPI
from fake_db import fake_prices_db

app = FastAPI()

@app.get("/all")
async def read_stocks():
    return {"message" : fake_prices_db}

@app.get("/stocks/{symbol}")
async def get_stock(symbol: str):
    # we are going to return the symbol of the stock price
    # search through our database and look for the 
    return "todo"