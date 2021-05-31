from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)
import datetime
from webhelpers2.text import urlify
from webhelpers2.date import distance_of_time_in_words
from .meta import Base
import re


class LocationEnum:
    location = 'UK England'


class PositionEnum:
    position1 = 'HR'
    position2 = 'digital marketing'


class TimeWorkEnum:
    time_work1 = 'Full time'
    time_work2 = 'Part time'


class WorkNeedEnum:
    work_need1 = 'Permanent'
    work_need2 = 'Project work'


class BenefitsEnum:
    benefits = 'Benefits'


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    responsibilities = Column(Text, unique=False)
    skills = Column(Text, unique=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    location = Column(Text, default=LocationEnum.location, unique=False)
    position = Column(Text, default=PositionEnum.position1, unique=False)
    time_work = Column(Text, default=TimeWorkEnum.time_work1, unique=False)
    work_need = Column(Text, default=WorkNeedEnum.work_need1, unique=False)
    benefits = Column(Text, default=BenefitsEnum.benefits, unique=False)

    @property
    def slug(self):
        return urlify(self.title)

    @property
    def created_in_words(self):
        return distance_of_time_in_words(self.created, datetime.datetime.utcnow())
    

Index('vacancy_index', Vacancy.title, unique=True, mysql_length=255)
