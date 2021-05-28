from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,

)

from .meta import Base


# Дописать когда пообедаю!
class Resume(Base):
    __tablename__ = 'resume'
    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    mail = Column(Text)
    phone = Column(Text)
    url = Column(Text)


Index('resume_index', Resume.last_name, unique=True, mysql_length=255)
