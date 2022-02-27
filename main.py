import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from DataBase.models import engine
from DataBase.models import TypeStation, Station

app = FastAPI()

Session = sessionmaker(bind=engine)

@app.get("/")
def index():
    ses = Session()
    data = ses.query(Station).all()
    return data



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)