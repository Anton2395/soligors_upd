from ast import Str
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
    TableAlarm = relationship("TableAlarm")


class TableAlarm(base):
    __tablename__ = "tablealarm"
    id_message = Column(Integer, primary_key=True, unique=True, nullable=False)
    id_station = Column(Integer, ForeignKey("station.id_station"))
    id_type_message = Column(Integer)
    id_text_message = Column(Integer)
    is_active = Column(Boolean)
    is_acknowledge = Column(Boolean)
    date_active = Column(Date)# mb DateTime
    date_out = Column(Date)# mb DateTime
    date_acknowledge = Column(Date)# mb DateTime




