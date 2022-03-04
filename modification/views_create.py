from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

import modification.shemas as _sh
import services as _services_main
from modification import services_create as _services

app_create = APIRouter(prefix="/modific")


@app_create.post("/typestation/", response_model=_sh.TypeStation)
def create_type_station(ty_station: _sh.TypeStationCreate, db: Session = Depends(_services_main.get_db)):
    """
     Созданиe типа станции

    - **name_type_station**: название типа станции
    - **name_table_station**: таблица в которой находится дальнейшая информация о станции
    """
    return _services.create_type_station(db=db, ty_stat=ty_station)

@app_create.post("/station/", response_model=_sh.Station)
def create_station(station: _sh.StationCreate, db: Session = Depends(_services_main.get_db)):
    """
    Созданиe станции и её месторасположение

    - **name_station**: название станции
    - **city_station**: город нахождения станции
    - **ip_station**: IP адрес станции
    - **longitude**: долгота
    - **latitube**: широта
    - **id_type_station**: ид типа станции
    """
    return _services.create_station(db=db, station=station)

@app_create.post("/tablealarm/", response_model=_sh.TableAlarm)
def create_table_alarm(alarm: _sh.TableAlarmCreate, db: Session = Depends(_services_main.get_db)):
    """
    Создание аварии

    - **id_station**: ид станции
    - **id_type_message**: ид типа сообщения
    - **id_text_message**: ид текста сообщения
    - **is_active**: авария активна?
    - **is_acknowledge**: авария подтверждена?
    - **date_active**: дата и время прихода аварии
    - **date_out**: дата и время ухода аварии
    - **date_acknowledge**: дата подтверждения аварии
    """
    return _services.create_table_alarm(alarm=alarm, db=db)

@app_create.post("/driver/", response_model=_sh.ListDriver)
def create_driver(driver: _sh.ListDriverCreate, db: Session = Depends(_services_main.get_db)):
    """
    Создание драйвера

    - **name_driver**: имя драйвера
    """
    return _services.create_driver(driver=driver, db=db)

@app_create.post("/level/", response_model=_sh.ListLevel)
def create_level(level:_sh.ListLevelCreate, db: Session = Depends(_services_main.get_db)):
    """
    Создание датчика уровня и протечки

    - **number_level**: количество уровней
    - **is_level_dry_run**: наличие датчика сухого хода
    - **name_dry_level**: имя датчика сухого хода
    - **is_sensor_overflow**: наличие датчика перелива
    - **name_sensor_overflow**: имя датчика перелива
    - **is_sensor_submersion**: наличие датчика затопления машзала
    - **name_sensor_submersion**: имя датчика машзала
    - **is_analog_level**: наличие аналогового датчика уровней
    """
    return _services.create_level(db=db, level=level)

@app_create.post("/station_kns/", response_model=_sh.StationKNS)
def create_station_KNS(station_kns:_sh.StationKNSCreate, db: Session = Depends(_services_main.get_db)):
    """
    Создание КНС с ее параметрами

    - **id_station**: ид станции
    - **id_driver_connection**: ид драйвера
    - **number_pump**: количество насосов
    - **number_input**: количество вводов
    - **id_list_level**: ид листа уровней
    """
    return _services.crete_station_kns(db=db, station_kns=station_kns)

@app_create.post("/data_connection/", response_model=_sh.DataConnectionKNS)
def create_data_connection_kns(data_connection: _sh.DataConnectionKNSCreate, db: Session = Depends(_services_main.get_db)):
    """
    Создать запись для реальных онлайн данных

    - **id_kns_station**: ид кнс станции
    - **is_alarm**: наличие аварии на станции
    - **name_table_signal_xd**: имя таблицы с дискретными сигналами
    - **name_table_signal_xa**: имя таблицы с аналоговыми сигналами
    - **name_table_pump**: имя таблицы с данными насосов
    - **name_table_energo**: имя таблицы с данными входов
    - **name_table_level**: имя таблицы с уровнями
    - **is_auto**: станция в автоматическом режиме
    - **is_manual**: станция в ручном режиме
    - **is_only_read**: станция в режиме слежения
    - **is_distance_control**: станция в режиме дистанционного упправления
    - **is_nsd**: сработка нсд
    - **is_temperature**: имеется датчик температуры
    - **temperature**: текущая температура
    - **analog_level**: значение уровня жидкости в кнс в % от 0 до 100
    - **name_table_history_level**: имя таблицы с архивом значений уровня
    """
    return _services.create_data_connection_kns(db=db, data_connection=data_connection)

@app_create.post("/signal_xd/", response_model=_sh.TableSignalXD)
def create_signal_XD(signal_xd: _sh.TableSignalXDCreate, db: Session = Depends(_services_main.get_db)):
    """
    Создать значение дискретного сигнала контроллера 

    - **name_signal**: имя сигнала
    - **name_x**: обозначение сигнала
    - **state**: состояние сигнала
    """
    return _services.create_table_signal_xd(db=db, signal_xd=signal_xd)

@app_create.post("/signal_xa/", response_model= _sh.TableSignalXA)
def create_signal_XA(signal_xa: _sh.TableSignalXACreate, db: Session = Depends(_services_main.get_db)):
    """
    Создать значение аналогового сигнала контроллера

    - **name_signal**: 
    - **name_x**: 
    - **state**: 
    """
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
