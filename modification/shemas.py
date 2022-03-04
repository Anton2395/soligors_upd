from pydantic import BaseModel
import datetime as _dt


class TypeStationCreate(BaseModel):
    name_type_station: str
    name_table_station: str

    class Config:
        orm_mode = True


class TypeStation(TypeStationCreate):
    id_type_station: int


class StationCreate(BaseModel):
    name_station: str
    city_station: str
    ip_station: str
    longitude: float
    latitube: float
    id_type_station: int

    class Config:
        orm_mode = True

class Station(StationCreate):
    id_station: int


class TableAlarmCreate(BaseModel):
    id_station: int
    id_type_message: int
    id_text_message: int
    is_active: bool
    is_acknowledge: bool
    date_active: _dt.datetime
    date_out: _dt.datetime
    date_acknowledge: _dt.datetime

    class Config:
        orm_mode = True


class TableAlarm(TableAlarmCreate):
    id_message: int


class ListDriverCreate(BaseModel):
    name_driver: str

    class Config:
        orm_mode = True


class ListDriver(ListDriverCreate):
    id_driver_connection: int


class ListLevelCreate(BaseModel):
    number_level: int
    is_level_dry_run: bool
    name_dry_level: str
    is_sensor_overflow: bool
    name_sensor_overflow: str
    is_sensor_submersion: bool
    name_sensor_submersion: str
    is_analog_level: bool

    class Config:
        orm_mode = True

class ListLevel(ListLevelCreate):
    id_list_level: int


class StationKNSCreate(BaseModel):
    id_station: int
    id_driver_connection: int
    number_pump: int
    number_input: int
    id_list_level: int

    class Config:
        orm_mode = True

class StationKNS(StationKNSCreate):
    id_kns_station: int


class DataConnectionKNSCreate(BaseModel):
    id_kns_station: int
    is_alarm: bool
    name_table_signal_xd: str
    name_table_signal_xa: str
    name_table_pump: str
    name_table_energo: str
    name_table_level: str
    is_auto: bool
    is_manual: bool
    is_only_read: bool
    is_distance_control: bool
    is_nsd: bool
    is_temperature: bool
    temperature: float
    analog_level: float
    name_table_history_level: str

    class Config:
        orm_mode = True

class DataConnectionKNS(DataConnectionKNSCreate):
    id: int


class TableSignalXDCreate(BaseModel):
    name_signal: str
    name_x: str
    state: bool

    class Config:
        orm_mode = True

class TableSignalXD(TableSignalXDCreate):
    id_signal: int


class TableSignalXACreate(BaseModel):
    name_signal: str
    name_x: str
    state: int

    class Config:
        orm_mode = True

class TableSignalXA(TableSignalXACreate):
    id_signal: int


class TablePumpCreate(BaseModel):
    no_pump: int
    auto_mode: int
    is_starter: bool
    name_starter: str
    is_wash: bool
    is_enable_bypass: bool
    is_enable_rotation: bool
    no_priority: int
    enable_run: bool
    current: float
    name_table_history_current: str
    nominal_current: float
    mototime: float
    state_pump: int
    name_table_history_state: str
    block_upp: bool
    block_bypass: bool

    class Config:
        orm_mode = True

class TablePump(TablePumpCreate):
    id: int


class TableLevelCreate(BaseModel):
    id_name_level: int
    state: bool

    class Config:
        orm_mode = True

class TableLevel(TableLevelCreate):
    id: int


class NameLevelKNSCreate(BaseModel):
    name_level: str
    no_nc: bool
    hierarchy: int

    class Config:
        orm_mode = True

class NameLevelKNS(NameLevelKNSCreate):
    id_name_level: int