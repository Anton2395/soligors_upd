import uvicorn
from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import sessionmaker, Session

from DataBase.models import engine
from DataBase.models import TypeStation, Station
import shemas as _sh
import services as _services

app = FastAPI()

Session = sessionmaker(bind=engine)


@app.post("/typestation/", response_model=_sh.TypeStation)
def create_type_station(ty_station: _sh.TypeStationCreate, db: Session = Depends(_services.get_db)):
    return _services.create_type_station(db=db, ty_stat=ty_station)

@app.post("/station/", response_model=_sh.Station)
def create_station(station: _sh.StationCreate, db: Session = Depends(_services.get_db)):
    return _services.create_station(db=db, station=station)

@app.post("/tablealarm/", response_model=_sh.TableAlarm)
def create_table_alarm(alarm: _sh.TableAlarmCreate, db: Session = Depends(_services.get_db)):
    return _services.create_table_alarm(alarm=alarm, db=db)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)