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

@app.post("/driver/", response_model=_sh.ListDriver)
def create_driver(driver: _sh.ListDriverCreate, db: Session = Depends(_services.get_db)):
    return _services.create_driver(driver=driver, db=db)

@app.post("/level/", response_model=_sh.ListLevel)
def create_level(level:_sh.ListLevelCreate, db: Session = Depends(_services.get_db)):
    return _services.create_level(db=db, level=level)

@app.post("/station_kns/", response_model=_sh.StationKNS)
def create_station_KNS(station_kns:_sh.StationKNSCreate, db: Session = Depends(_services.get_db)):
    return _services.crete_station_kns(db=db, station_kns=station_kns)

@app.post("/data_connection/", response_model=_sh.DataConnectionKNS)
def create_data_connection_kns(data_connection: _sh.DataConnectionKNSCreate, db: Session = Depends(_services.get_db)):
    return _services.create_data_connection_kns(db=db, data_connection=data_connection)

@app.post("/signal_xd/", response_model=_sh.TableSignalXD)
def create_signal_XD(signal_xd: _sh.TableSignalXDCreate, db: Session = Depends(_services.get_db)):
    return _services.create_table_signal_xd(db=db, signal_xd=signal_xd)

@app.post("/signal_xa/", response_model= _sh.TableSignalXA)
def create_signal_XA(signal_xa: _sh.TableSignalXACreate, db: Session = Depends(_services.get_db)):
    return _services.create_table_signal_xa(db=db, signal_xa=signal_xa)

@app.post("/pump/", response_model=_sh.TablePump)
def create_pump(pump: _sh.TablePumpCreate, db: Session = Depends(_services.get_db)):
    return _services.create_table_pump(db=db, pump=pump)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)