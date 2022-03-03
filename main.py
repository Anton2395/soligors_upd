import uvicorn
from fastapi import FastAPI
from modification import views_create as _views_create
from modification import views_change as _views_change

app = FastAPI()
app.include_router(_views_create.app_create)
app.include_router(_views_change.app_change)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)