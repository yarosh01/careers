from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,

)

from .meta import Base


# Дописать когда пообедаю!
class AdminUser(Base):
    __tablename__ = 'admin_user'
    id = Column(Integer, primary_key=True)
    login = Column(Text, nullable=False)
    mail = Column(Text)
    password = Column(Text, nullable=False)


Index('admin_index', AdminUser.login, unique=True, mysql_length=255)
