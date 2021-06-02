from fastapi import FastAPI
import uvicorn
from regression_logistique import *

# init
app = FastAPI(debug = True)

#data

#route
@app.get('/api/v1/sentiments')
async def get_sentiment():
    return {'$entiment': 'happyness'}

@app.get('/api/v1/sentiments/sentiments[]')
async def get_sentiment_sentiment():
    
    return


if __name__ == '__main__':
    uvicorn.run(app, host= '127.0.0.1', port= '8000')
#@app.post("/")
#async def message_post() :
#    message = input('veuilez entrer une phrase')
#    return message
#
#@app.get("/")
#async def root():
#    return {"message": "happyness"}