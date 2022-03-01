from DataBase.models import SessionLocal
import sqlalchemy.orm as _orm
import shemas as _sh
import DataBase.models as _models



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_type_station(db: _orm.Session, ty_stat: _sh.TypeStationCreate):
    db_type_station = _models.TypeStation(name_type_station=ty_stat.name_type_station, name_table_station=ty_stat.name_table_station)
    db.add(db_type_station)
    db.commit()
    db.refresh(db_type_station)
    return db_type_station

def create_station(db: _orm.Session, station: _sh.StationCreate):
    db_station = _models.Station(
        name_station=station.name_station,
        city_station=station.city_station,
        ip_station=station.ip_station,
        longitude=station.longitude,
        latitube=station.latitube,
        id_type_station=station.id_type_station
        )
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station

def create_table_alarm(db: _orm.Session, alarm: _sh.TableAlarmCreate):
    db_alarm = _models.TableAlarm(
        id_station=alarm.id_station,
        id_type_message=alarm.id_type_message,
        id_text_message=alarm.id_text_message,
        is_active=alarm.is_active,
        is_acknowledge=alarm.is_acknowledge,
        date_active=alarm.date_active,
        date_out=alarm.date_out,
        date_acknowledge=alarm.date_acknowledge
    )
    db.add(db_alarm)
    db.commit()
    db.refresh(db_alarm)
    return db_alarm