from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import FLOAT, INTEGER, VARCHAR, DATETIME, BOOLEAN, TEXT, TIMESTAMP
import datetime

from utils.others import uniqid


Base = declarative_base()



class WaypointDB(Base):
    __tablename__ = "isim_waypoints"
    id   = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(length=10), unique=True)
    lat  = Column(FLOAT(precision=10))
    lon  = Column(FLOAT(precision=10))


class ScenarioDB(Base):
    __tablename__ = "isim_scenarios"
    id          = Column(INTEGER, primary_key=True)
    name        = Column(VARCHAR(length=255), unique=True)
    notes       = Column(VARCHAR(length=255))
    last_update = Column(DATETIME(), default=datetime.datetime.now, onupdate=datetime.datetime.now)


class FlightPlanDB(Base):
    __tablename__ = "isim_flightplans"
    id             = Column(INTEGER, primary_key=True)
    scenario_id    = Column(INTEGER)
    flight_id      = Column(VARCHAR(length=20), default=uniqid)
    callsign       = Column(VARCHAR(length=10), default='')
    routes         = Column(TEXT(), nullable=False)
    enroute_only   = Column(BOOLEAN, default=False)
    origin         = Column(VARCHAR(length=10), default='')
    destination    = Column(VARCHAR(length=10), default='')
    departure_time = Column(INTEGER)
    cruising_level = Column(INTEGER)
    cruising_speed = Column(INTEGER)
    last_update    = Column(DATETIME(), default=datetime.datetime.now, onupdate=datetime.datetime.now)