from DataBase.models import SessionLocal
import sqlalchemy.orm as _orm
import modification.shemas as _sh
import DataBase.models as _models

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


def create_driver(db: _orm.Session, driver: _sh.ListDriverCreate):
    db_driver = _models.ListDriver(
        name_driver=driver.name_driver
    )
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def create_level(db: _orm.Session, level: _sh.ListLevelCreate):
    db_level = _models.ListLevel(
        number_level=level.number_level,
        is_level_dry_run=level.is_level_dry_run,
        name_dry_level=level.name_dry_level,
        is_sensor_overflow=level.is_sensor_overflow,
        name_sensor_overflow=level.name_sensor_overflow,
        is_sensor_submersion=level.is_sensor_submersion,
        name_sensor_submersion=level.name_sensor_submersion,
        is_analog_level=level.is_analog_level
    )
    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    return db_level

def crete_station_kns(db: _orm.Session, station_kns: _sh.StationKNSCreate):
    db_station_kns = _models.StationKNS(
        id_station=station_kns.id_station,
        id_driver_connection=station_kns.id_driver_connection,
        number_pump=station_kns.number_pump,
        number_input=station_kns.number_input,
        id_list_level=station_kns.id_list_level
    )
    db.add(db_station_kns)
    db.commit()
    db.refresh(db_station_kns)
    return db_station_kns

def create_data_connection_kns(db: _orm.Session, data_connection: _sh.DataConnectionKNSCreate):
    db_data_connection = _models.DataConnectionKNS(
        id_kns_station=data_connection.id_kns_station,
        is_alarm=data_connection.is_alarm,
        name_table_signal_xd=data_connection.name_table_signal_xd,
        name_table_signal_xa=data_connection.name_table_signal_xa,
        name_table_pump=data_connection.name_table_pump,
        name_table_energo=data_connection.name_table_energo,
        name_table_level=data_connection.name_table_level,
        is_auto=data_connection.is_auto,
        is_manual=data_connection.is_manual,
        is_only_read=data_connection.is_only_read,
        set_auto=data_connection.set_auto,
        set_manual=data_connection.set_manual,
        is_distance_control=data_connection.is_distance_control,
        is_nsd=data_connection.is_nsd,
        is_temperature=data_connection.is_temperature,
        temperature=data_connection.temperature,
        analog_level=data_connection.analog_level,
        name_table_history_level=data_connection.name_table_history_level
    )
    db.add(db_data_connection)
    db.commit()
    db.refresh(db_data_connection)
    return db_data_connection

def create_table_signal_xd(db: _orm.Session, signal_xd: _sh.TableSignalXDCreate):
    db_signal_xd = _models.TableSignalXD(
        name_signal=signal_xd.name_signal,
        name_x=signal_xd.name_x,
        state=signal_xd.state
    )
    db.add(db_signal_xd)
    db.commit()
    db.refresh(db_signal_xd)
    return db_signal_xd

def create_table_signal_xa(db: _orm.Session, signal_xa: _sh.TableSignalXACreate):
    db_signal_xa = _models.TableSignalXA(
        name_signal=signal_xa.name_signal,
        name_x=signal_xa.name_x,
        state=signal_xa.state
    )
    db.add(db_signal_xa)
    db.commit()
    db.refresh(db_signal_xa)
    return db_signal_xa

def create_table_pump(db: _orm.Session, pump: _sh.TablePumpCreate):
    db_pump = _models.TablePump(
        no_pump=pump.no_pump,
        reset_alarm=pump.reset_alarm,
        manual_start=pump.manual_start,
        manual_stop=pump.manual_stop,
        auto_mode=pump.auto_mode,
        is_starter=pump.is_starter,
        name_starter=pump.name_starter,
        is_wash=pump.is_wash,
        is_enable_bypass=pump.is_enable_bypass,
        is_enable_rotation=pump.is_enable_rotation,
        no_priority=pump.no_priority,
        enable_run=pump.enable_run,
        current=pump.current,
        name_table_history_current=pump.name_table_history_current,
        nominal_current=pump.nominal_current,
        mototime=pump.mototime,
        reset_mototime=pump.reset_mototime,
        state_pump=pump.state_pump,
        name_table_history_state=pump.name_table_history_state,
        block_upp=pump.block_upp,
        block_bypass=pump.block_bypass,
    )
    db.add(db_pump)
    db.commit()
    db.refresh(db_pump)
    return db_pump

def create_table_level(db: _orm.Session, level: _sh.TableLevelCreate):
    db_level = _models.TableLevel(
        id_name_level=level.id_name_level,
        state=level.state
    )
    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    return db_level

def create_name_level_kns(db:_orm.Session, level_kns:_sh.NameLevelKNSCreate):
    db_level_kns = _models.NameLevelKNS(
        name_level=level_kns.name_level,
        no_nc=level_kns.no_nc,
        hierarchy=level_kns.hierarchy
    )
    db.add(db_level_kns)
    db.commit()
    db.refresh(db_level_kns)
    return db_level_kns