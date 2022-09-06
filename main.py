from fastapi import FastAPI
import router as router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/hello/{user}')
async def hello(user):
    return {'message': user}


app.include_router(router.router)
