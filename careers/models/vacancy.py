from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)
import sqlalchemy.types as types
from .meta import Base
import enum

from sqlalchemy.types import Enum


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


# class ChoiceType(types.TypeDecorator):
#     impl = types.String
#
#     def __init__(self, choices, **kw):
#         self.choices = dict(choices)
#         super(ChoiceType, self).__init__(**kw)
#
#     def process_bind_param(self, value, dialect):
#         return [k for k, v in self.choices.items() if v == value][0]
#
#     def process_result_value(self, value, dialect):
#         return self.choices[value]


class Vacancy(Base):
    __tablename__ = 'vacancy'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=False)
    responsibilities = Column(Text, unique=False)
    skills = Column(Text, unique=False)
    location = Column(Text, default=LocationEnum.location, unique=False)
    position = Column(Text, default=PositionEnum.position1, unique=False)
    time_work = Column(Text, default=TimeWorkEnum.time_work1, unique=False)
    work_need = Column(Text, default=WorkNeedEnum.work_need1, unique=False)
    benefits = Column(Text, default=BenefitsEnum.benefits, unique=False)


    def get_absolute_url(self):
        pass

    # location = Column(ChoiceType({"UK": "UK"}), nullable=False)
    # position = Column(ChoiceType({"HR": "HR", "digital": "digital marketing"}), nullable=False)
    # time_work = Column(ChoiceType({'Full': 'Full time', 'Relocate': 'Relocate'}), nullable=False)
    # work_need = Column(ChoiceType({'Permanent': 'Permanent', 'Project': 'Project work'}), nullable=False)
    # benefits = Column(ChoiceType({'Benefits': 'Benefits'}))


Index('vacancy_index', Vacancy.title, unique=True, mysql_length=255)
