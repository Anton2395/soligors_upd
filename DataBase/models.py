from ast import Str
from cgitb import reset
from doctest import FAIL_FAST
import string
from xml.etree.ElementInclude import default_loader
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean, DateTime
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from DataBase.config_db import DATABASE_URL


engine = create_engine(DATABASE_URL)


base = declarative_base()

class TypeStation(base):
    __tablename__ = "typestation"
    id_type_station = Column(Integer, primary_key=True, unique=True)
    name_type_station = Column(String, index=True, nullable=False, default="No set name type")
    name_table_station = Column(String, index=True)
    station = relationship("Station", cascade="all, delete", back_populates="typestation")

class Station(base):
    __tablename__ = "station"
    id_station = Column(Integer, primary_key=True, unique=True)
    name_station = Column(String, nullable=False, index=True, default='No name')
    city_station = Column(String, nullable=True, index=True, default="No set city")
    ip_station = Column(String, nullable=True, index=True, default="No set ip")
    longitude = Column(Float, nullable=True, index=True)
    latitube = Column(Float, nullable=True, index=True)
    id_type_station = Column(Integer, ForeignKey("typestation.id_type_station"), index=True)
    typestation = relationship("TypeStation", back_populates="station")
    tablealarm = relationship("TableAlarm", cascade="all, delete", back_populates="station")
    stationkns = relationship("StationKNS", cascade="all, delete", back_populates="station")


class TableAlarm(base):
    __tablename__ = "tablealarm"
    id_message = Column(Integer, primary_key=True, unique=True)
    id_station = Column(Integer, ForeignKey("station.id_station"), index=True)
    id_type_message = Column(Integer, index=True)
    id_text_message = Column(Integer, index=True)
    is_active = Column(Boolean, index=True)
    is_acknowledge = Column(Boolean, index=True)
    date_active = Column(DateTime, index=True)
    date_out = Column(DateTime, index=True)
    date_acknowledge = Column(DateTime, index=True)
    station = relationship("Station", back_populates="tablealarm")


class ListDriver(base):
    __tablename__ = "listdriver"
    id_driver_connection = Column(Integer, primary_key=True, unique=True)
    name_driver = Column(String, nullable=False, index=True, default="snap7")# need default?
    stationkns = relationship("StationKNS", cascade="all, delete", back_populates="listdriver")

class ListLevel(base):
    __tablename__ = "listlevel"
    id_list_level = Column(Integer, primary_key=True, unique=True)
    number_level = Column(Integer, nullable=False, index=True)
    is_level_dry_run = Column(Boolean, nullable=False, index=True, default=False)
    name_dry_level = Column(String, nullable=False, index=True, default="No name level")
    is_sensor_overflow = Column(Boolean, nullable=False, index=True, default=False)
    name_sensor_overflow = Column(String, nullable=False, index=True, default="No name sensor over.")
    is_sensor_submersion = Column(Boolean, nullable=False, index=True, default=False)
    name_sensor_submersion = Column(String, nullable=False, index=True, default="No name sensor submer.")
    is_analog_level = Column(Boolean, nullable=False, index=True, default=False)
    stationkns = relationship("StationKNS", cascade="all, delete", back_populates="listlevel")


class StationKNS(base):
    __tablename__ = "stationkns"
    id_kns_station = Column(Integer, primary_key=True, unique=True)
    id_station = Column(Integer, ForeignKey("station.id_station"), index=True)
    id_driver_connection = Column(Integer, ForeignKey("listdriver.id_driver_connection"), index=True)
    number_pump = Column(Integer, nullable=False, index=True)
    number_input = Column(Integer, nullable=False, index=True)
    id_list_level = Column(Integer, ForeignKey("listlevel.id_list_level"), index=True)
    dataconnectionkns = relationship("DataConnectionKNS", cascade="all, delete", back_populates="stationkns")
    station = relationship("Station", back_populates="stationkns")
    listdriver = relationship("ListDriver", back_populates="stationkns")
    listlevel = relationship("ListLevel", back_populates="stationkns")


class DataConnectionKNS(base):
    __tablename__ = "dataconnectionkns"
    id = Column(Integer, primary_key=True, unique=True)
    id_kns_station = Column(Integer, ForeignKey("stationkns.id_kns_station"), index=True)
    is_alarm = Column(Boolean, nullable=False, index=True, default=False)
    name_table_signal_xd = Column(String, nullable=False, index=True, default="No table name")
    name_table_signal_xa = Column(String, nullable=False, index=True, default="No table name")
    name_table_pump = Column(String, nullable=False, index=True, default="No table name")
    name_table_energo = Column(String, nullable=False, index=True, default="No table name")
    name_table_level = Column(String, nullable=False, index=True, default="No table name")
    is_auto = Column(Boolean, nullable=False, index=True, default=False)
    is_manual = Column(Boolean, nullable=False, index=True, default=False)
    is_only_read = Column(Boolean, nullable=False, index=True, default=False)
    is_distance_control = Column(Boolean, nullable=False, index=True, default=False)
    is_nsd = Column(Boolean, nullable=False, index=True, default=False)
    is_temperature = Column(Boolean, nullable=False, index=True, default=False)
    temperature = Column(Float, nullable=True, index=True)
    analog_level = Column(Float, nullable=True, index=True)
    name_table_history_level = Column(String, nullable=False, index=True)
    stationkns = relationship("StationKNS", back_populates="dataconnectionkns")


class TableSignalXD(base):
    __tablename__ = "tablesignalxd"
    id_signal = Column(Integer, primary_key=True, unique=True)
    name_signal = Column(String, nullable=False, index=True, default="No name signal")
    name_x = Column(String, nullable=False, index=True, default="No name")
    state = Column(Boolean, nullable=False, index=True, default=False)


class TableSignalXA(base):
    __tablename__ = "tablesignalxa"
    id_signal = Column(Integer, primary_key=True, unique=True)
    name_signal = Column(String, nullable=False, index=True, default="No name signal")
    name_x = Column(String, nullable=False, index=True, default="No name")
    state = Column(Integer, nullable=False, index=True, default=0)

class TablePump(base):
    __tablename__ = "tablepump"
    id = Column(Integer, primary_key=True, unique=True)
    no_pump = Column(Integer, nullable=False, index=True)
    auto_mode = Column(Integer, nullable=False, index=True, default=0)
    is_starter = Column(Boolean, nullable=False, index=True, default=False)
    name_starter = Column(String, nullable=False, index=True, default="No name starter")
    is_wash = Column(Boolean, nullable=False, index=True, default=False)
    is_enable_bypass = Column(Boolean, nullable=False, index=True, default=False)
    is_enable_rotation = Column(Boolean, nullable=False, index=True, default=False)
    no_priority = Column(Integer, nullable=False, index=True, default=0)
    enable_run = Column(Boolean, nullable=False, index=True, default=False)
    current = Column(Float, nullable=False, index=True, default=0.0)
    name_table_history_current = Column(String, index=True, nullable=False)
    nominal_current = Column(Float, nullable=False, index=True, default=0.0)
    mototime = Column(Float, nullable=False, index=True, default=0.0)
    state_pump = Column(Integer, nullable=False, index=True, default=0)
    name_table_history_state = Column(String, nullable=False, index=True)
    block_upp = Column(Boolean, nullable=False, default=False, index=True)
    block_bypass = Column(Boolean, nullable=False, default=False, index=True)


class TableLevel(base):
    __tablename__ = "tablelevel"
    id = Column(Integer, primary_key=True, unique=True)
    id_name_level = Column(Integer, nullable=False, index=True, default=0)
    state = Column(Boolean, nullable=False, index=True, default=False)


class NameLevelKNS(base):
    __tablename__ = "namelevelkns"
    id_name_level = Column(Integer, primary_key=True, unique=True)
    name_level = Column(String, nullable=False, index=True, default="No name level")
    no_nc = Column(Boolean, nullable=False, index=True, default=False)
    hierarchy = Column(Integer, nullable=False, index=True, default=0)

SessionLocal = sessionmaker(autocommit=False, bind=engine)