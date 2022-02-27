from ast import Str
from cgitb import reset
from doctest import FAIL_FAST
import string
from xml.etree.ElementInclude import default_loader
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean, Date
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = create_engine("postgresql+psycopg2://mvlab:z1x2c3@0.0.0.0:5432/db1")


base = declarative_base()

class TypeStation(base):
    __tablename__ = "typestation"
    id_type_station = Column(Integer, primary_key=True, nullable=False, unique=True)
    name_type_station = Column(String, nullable=False, default="No set name type")
    name_table_station = Column(String)
    station = relationship("Station")

class Station(base):
    __tablename__ = "station"
    id_station = Column(Integer, primary_key=True, unique=True, nullable=False)
    name_station = Column(String, nullable=False, default='No name')
    city_station = Column(String, nullable=True, default="No set city")
    ip_station = Column(String, nullable=True, default="No set ip")
    longitude = Column(Float, nullable=True)
    latitube = Column(Float, nullable=True)
    id_type_station = Column(Integer, ForeignKey("typestation.id_type_station"))
    tablealarm = relationship("TableAlarm")
    stationkns = relationship("StationKNS")


class TableAlarm(base):
    __tablename__ = "tablealarm"
    id_message = Column(Integer, primary_key=True, unique=True)
    id_station = Column(Integer, ForeignKey("station.id_station"))
    id_type_message = Column(Integer)
    id_text_message = Column(Integer)
    is_active = Column(Boolean)
    is_acknowledge = Column(Boolean)
    date_active = Column(Date)# mb DateTime
    date_out = Column(Date)# mb DateTime
    date_acknowledge = Column(Date)# mb DateTime


class ListDriver(base):
    __tablename__ = "listdriver"
    id_driver_connection = Column(Integer, primary_key=True, unique=True, index=True)
    name_driver = Column(String, nullable=False, default="snap7")# need default?
    stationkns = relationship("StationKNS")

class ListLevel(base):
    __tablename__ = "listlevel"
    id_list_level = Column(Integer, primary_key=True, index=True)
    number_level = Column(Integer, nullable=False)
    is_level_dry_run = Column(Boolean, nullable=False, default=False)
    name_dry_level = Column(String, nullable=False, default="No name level")
    is_sensor_overflow = Column(Boolean, nullable=False, default=False)
    name_sensor_overflow = Column(String, nullable=False, default="No name sensor over.")
    is_sensor_submersion = Column(Boolean, nullable=False, default=False)
    name_sensor_submersion = Column(String, nullable=False, default="No name sensor submer.")
    is_analog_level = Column(Boolean, nullable=False, default=False)
    stationkns = relationship("StationKNS")


class StationKNS(base):
    __tablename__ = "stationkns"
    id_kns_station = Column(Integer, primary_key=True, unique=True, index=True)
    id_station = Column(Integer, ForeignKey("station.id_station"))
    id_driver_connection = Column(Integer, ForeignKey("listdriver.id_driver_connection"))
    number_pump = Column(Integer, nullable=False)
    number_input = Column(Integer, nullable=False)
    id_list_level = Column(Integer, ForeignKey("listlevel.id_list_level"))
    dataconnectionkns = relationship("DataConnectionKNS")


class DataConnectionKNS(base):
    __tablename__ = "dataconnectionkns"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    id_kns_station = Column(Integer, ForeignKey("stationkns.id_kns_station"))
    is_alarm = Column(Boolean, nullable=False, default=False)
    name_table_signal_xd = Column(String, nullable=False, default="No table name")
    name_table_signal_xa = Column(String, nullable=False, default="No table name")
    name_table_pump = Column(String, nullable=False, default="No table name")
    name_table_energo = Column(String, nullable=False, default="No table name")
    name_table_level = Column(String, nullable=False, default="No table name")
    is_auto = Column(Boolean, nullable=False, default=False)
    is_manual = Column(Boolean, nullable=False, default=False)
    is_only_read = Column(Boolean, nullable=False, default=False)
    set_auto = Column(Boolean, nullable=False, default=False)# что значит это поле
    set_manual = Column(Boolean, nullable=False, default=False)# также как и set_auuto?
    is_distance_control = Column(Boolean, nullable=False, default=False)
    is_nsd = Column(Boolean, nullable=False, default=False)
    is_temperature = Column(Boolean, nullable=False, default=False)
    temperature = Column(Float, nullable=True)
    analog_level = Column(Float, nullable=True)
    name_table_history_level = Column(String, nullable=False)


class TableSignalXD(base):
    __tablename__ = "tablesignalxd"
    id_signal = Column(Integer, primary_key=True, unique=True, index=True)
    name_signal = Column(String, nullable=False, default="No name signal")
    name_x = Column(String, nullable=False, default="No name")
    state = Column(Boolean, nullable=False, default=False)


class TableSignalXA(base):
    __tablename__ = "tablesignalxa"
    id_signal = Column(Integer, primary_key=True, unique=True, index=True)
    name_signal = Column(String, nullable=False, default="No name signal")
    name_x = Column(String, nullable=False, default="No name")
    state = Column(Integer, nullable=False, default=0)

class TablePump(base):
    __tablename__ = "tablepump"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    no_pump = Column(Integer, nullable=False)#  случайно не boolean?
    reset_alarm = Column(Boolean, nullable=False, default=False)
    manual_start = Column(Boolean, nullable=False, default=False)
    manual_stop = Column(Boolean, nullable=False, default=False)
    auto_mode = Column(Integer, nullable=False, default=0)
    is_starter = Column(Boolean, nullable=False, default=False)
    name_starter = Column(String, nullable=False, default="No name starter")
    is_wash = Column(Boolean, nullable=False, default=False)
    is_enable_bypass = Column(Boolean, nullable=False, default=False)
    is_enable_rotation = Column(Boolean, nullable=False, default=False)
    no_priority = Column(Integer, nullable=False, default=0)
    enable_run = Column(Boolean, nullable=False, default=False)
    current = Column(Float, nullable=False, default=0.0)
    name_table_history_current = Column(String, nullable=False)
    nominal_current = Column(Float, nullable=False, default=0.0)
    mototime = Column(Float, nullable=False, default=0.0)
    reset_mototime = Column(Boolean, nullable=False, default=False)
    state_pump = Column(Integer, nullable=False, default=0)
    name_table_history_state = Column(String, nullable=False)
    block_upp = Column(Boolean, nullable=False, default=False)
    block_bypass = Column(Boolean, nullable=False, default=False)


class TableLevel(base):
    __tablename__ = "tablelevel"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    id_name_level = Column(Integer, nullable=False, default=0)
    state = Column(Boolean, nullable=False, default=False)


class NameLevelKNS(base):
    __tablename__ = "namelevelkns"
    id_name_level = Column(Integer, primary_key=True, unique=True, index=True)
    name_level = Column(String, nullable=False, default="No name level")
    no_nc = Column(Boolean, nullable=False, default=False)
    hierarchy = Column(Integer, nullable=False, default=0)