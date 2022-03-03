from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

import modification.shemas as _sh
import services as _services_main
from modification import services_create as _services

app_create = APIRouter(prefix="/modific")


@app_create.post("/typestation/", response_model=_sh.TypeStation)
def create_type_station(ty_station: _sh.TypeStationCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_type_station(db=db, ty_stat=ty_station)

@app_create.post("/station/", response_model=_sh.Station)
def create_station(station: _sh.StationCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_station(db=db, station=station)

@app_create.post("/tablealarm/", response_model=_sh.TableAlarm)
def create_table_alarm(alarm: _sh.TableAlarmCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_table_alarm(alarm=alarm, db=db)

@app_create.post("/driver/", response_model=_sh.ListDriver)
def create_driver(driver: _sh.ListDriverCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_driver(driver=driver, db=db)

@app_create.post("/level/", response_model=_sh.ListLevel)
def create_level(level:_sh.ListLevelCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_level(db=db, level=level)

@app_create.post("/station_kns/", response_model=_sh.StationKNS)
def create_station_KNS(station_kns:_sh.StationKNSCreate, db: Session = Depends(_services_main.get_db)):
    return _services.crete_station_kns(db=db, station_kns=station_kns)

@app_create.post("/data_connection/", response_model=_sh.DataConnectionKNS)
def create_data_connection_kns(data_connection: _sh.DataConnectionKNSCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_data_connection_kns(db=db, data_connection=data_connection)

@app_create.post("/signal_xd/", response_model=_sh.TableSignalXD)
def create_signal_XD(signal_xd: _sh.TableSignalXDCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_table_signal_xd(db=db, signal_xd=signal_xd)

@app_create.post("/signal_xa/", response_model= _sh.TableSignalXA)
def create_signal_XA(signal_xa: _sh.TableSignalXACreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_table_signal_xa(db=db, signal_xa=signal_xa)

@app_create.post("/pump/", response_model=_sh.TablePump)
def create_pump(pump: _sh.TablePumpCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_table_pump(db=db, pump=pump)

@app_create.post("/table_level/", response_model=_sh.TableLevel)
def create_level(level:_sh.TableLevelCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_table_level(db=db, level=level)

@app_create.post("/level_kns/", response_model=_sh.NameLevelKNS)
def create_name_level_kns(level_kns:_sh.NameLevelKNSCreate, db: Session = Depends(_services_main.get_db)):
    return _services.create_name_level_kns(db=db, level_kns=level_kns)
