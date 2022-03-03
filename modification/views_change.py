from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

import services as _services_main
from modification import service_change as _services
from modification import shemas as _sh

app_change = APIRouter(prefix="/modific")

@app_change.put("/typestation/{id_type_station}", response_model=_sh.TypeStation)
def change_type_station(
    type_station:_sh.TypeStationCreate,
    id_type_station:int,
    db: Session = Depends(_services_main.get_db)
):
    return _services.change_type_station(db=db, type_station=type_station, id_type_station=id_type_station)

@app_change.put("/station/{id_station}", response_model=_sh.Station)
def change_station(
    station:_sh.StationCreate,
    id_station:int,
    db:Session = Depends(_services_main.get_db)
):
    return _services.change_station(db=db, id_station=id_station, station=station)

@app_change.put("/tablealarm/{id_message}", response_model=_sh.TableAlarm)
def change_table_alarm(
    alarm:_sh.TableAlarm,
    id_message:int,
    db:Session = Depends(_services_main.get_db)
):
    return _services.change_table_alarm(db=db, id_message=id_message, alarm=alarm)

@app_change.put("/driver/{id_driver_connection}", response_model=_sh.ListDriver)
def change_list_driver(
    list_driver:_sh.ListDriverCreate,
    id_driver_connection:int,
    db: Session = Depends(_services_main.get_db)
):
    return _services.change_list_driver(db=db, list_driver=list_driver, id_driver_connection=id_driver_connection)

@app_change.put("/level'/{id_list_level}", response_model=_sh.ListLevel)
def change_list_level(
    list_level:_sh.ListDriverCreate,
    id_list_level=int,
    db: Session = Depends(_services_main.get_db)
):
    return _services.change_list_level(db=db, list_level=list_level, id_list_level=id_list_level)

@app_change.put("/station_kns/{id_kns_station}", response_model=_sh.StationKNS)
def change_station_kns(
    id_kns_station:int,
    station_kns:_sh.StationKNSCreate,
    db: Session = Depends(_services_main.get_db)
):
    return _services.change_station_kns(db=db, id_kns_station=id_kns_station, station_kns=station_kns)