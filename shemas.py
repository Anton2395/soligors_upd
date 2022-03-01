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
    date_active: _dt.date
    date_out: _dt.date
    date_acknowledge: _dt.date

    class Config:
        orm_mode = True


class TableAlarm(TableAlarmCreate):
    id_message: int



