import sqlalchemy.orm as _orm
from DataBase import models as _models

from modification import shemas as _sh


def change_type_station(db:_orm.Session, id_type_station:int, type_station:_sh.TypeStationCreate):
    record_type = db.query(_models.TypeStation).filter(_models.TypeStation.id_type_station==id_type_station).first()
    record_type.name_type_station = type_station.name_type_station
    record_type.name_table_station = type_station.name_table_station
    db.commit()
    db.refresh(record_type)
    return record_type

def change_station(db:_orm.Session, station:_sh.StationCreate, id_station=int):
    record_station = db.query(_models.Station).filter(_models.Station.id_station==id_station).first()
    record_station.name_station = station.name_station
    record_station.city_station = station.city_station
    record_station.ip_station = station.ip_station
    record_station.longitude = station.longitude
    record_station.latitube = station.latitube
    record_station.id_type_station = station.id_type_station
    db.commit()
    db.refresh(record_station)
    return record_station

def change_table_alarm(db:_orm.Session, alarm:_sh.TableAlarmCreate, id_message:int):
    record_alarm = db.query(_models.TableAlarm).filter(_models.TableAlarm.id_message==id_message).first()
    record_alarm.id_station = alarm.id_station
    record_alarm.id_type_message = alarm.id_type_message
    record_alarm.id_text_message = alarm.id_text_message
    record_alarm.is_active = alarm.is_active
    record_alarm.is_acknowledge = alarm.is_acknowledge
    record_alarm.date_active = alarm.date_active
    record_alarm.date_out = alarm.date_out
    record_alarm.date_acknowledge = alarm.date_acknowledge
    db.commit()
    db.refresh(record_alarm)
    return record_alarm

def change_list_driver(list_driver:_sh.ListDriverCreate, db:_orm.Session, id_driver_connection:int):
    record_driver = db.query(_models.ListDriver).filter(_models.ListDriver.id_driver_connection==id_driver_connection).first()
    record_driver.name_driver = list_driver.name_driver
    db.commit()
    db.refresh(record_driver)
    return record_driver

def change_list_level(list_level:_sh.ListLevelCreate, id_list_level:int, db:_orm.Session):
    record_level = db.query(_models.ListLevel).filter(_models.ListLevel.id_list_level==id_list_level).first()
    record_level.number_level = list_level.number_level
    record_level.is_level_dry_run = list_level.is_level_dry_run
    record_level.name_dry_level = list_level.name_dry_level
    record_level.is_sensor_overflow = list_level.is_sensor_overflow
    record_level.name_sensor_overflow = list_level.name_sensor_overflow
    record_level.is_sensor_submersion = list_level.is_sensor_submersion
    record_level.name_sensor_submersion = list_level.name_sensor_submersion
    record_level.is_analog_level = list_level.is_analog_level
    db.commit()
    db.refresh(record_level)
    return record_level

def change_station_kns(station_kns:_sh.StationKNSCreate, id_kns_station:int, db:_orm.Session):
    record_station = db.query(_models.StationKNS).filter(_models.StationKNS.id_kns_station==id_kns_station).first()
    record_station.id_station = station_kns.id_station
    record_station.id_driver_connection = station_kns.id_driver_connection
    record_station.number_pump = station_kns.number_pump
    record_station.number_input = station_kns.number_input
    record_station.id_list_level = station_kns.id_list_level
    db.commit()
    db.refresh(record_station)
    return record_station