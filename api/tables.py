import sqlalchemy as sa
from sqlalchemy import MetaData, Table, Column, Integer, Computed
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Cameras(Base):
    __tablename__ = "cameras"

    id = sa.Column(sa.Integer, primary_key=True)
    camera_name = sa.Column(sa.String)
    stream_url = sa.Column(sa.String)
    is_active = sa.Column(sa.Boolean)
    live_views_relationship = relationship("LiveViews")
    time_lapse_relationship = relationship("TimeLapse")


class LiveViews(Base):
    __tablename__ = "live_views"

    id = sa.Column(sa.Integer, primary_key=True)
    camera_id = sa.Column(sa.Integer)
    path = sa.Column(sa.String)
    file_size = sa.Column(sa.Integer)
    fps = sa.Column(sa.DECIMAL)
    fk_cameras = sa.Column(sa.Integer, ForeignKey('cameras.id'))

class TimeLapse(Base):
    __tablename__ = "time_lapse"

    id = sa.Column(sa.Integer, primary_key=True)
    camera_id = sa.Column(sa.Integer)
    path = sa.Column(sa.String)
    file_size = sa.Column(sa.Integer)
    fps = sa.Column(sa.DECIMAL)
    comment = sa.Column(sa.String, nullable=True)
    fk_cameras = sa.Column(sa.Integer, ForeignKey("cameras.id"))
