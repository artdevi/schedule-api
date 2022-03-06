from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String, unique=False)
    first_name = Column(String, unique=False)
    middle_name = Column(String, unique=False)
    email = Column(String, unique=True)
    phone_number = Column(String, unique=True)

    def __init__(self, last_name: str, first_name: str, middle_name: str, email: str, phone_number: str):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        info: str = f'Клиент [ФИО: {self.last_name} {self.first_name} {self.middle_name}, ' \
                    f'Email: {self.email} ' \
                    f'Номер телефона: {self.phone_number} ]'

        return info


class Bands(Base):
    __tablename__ = 'bands'

    name = Column(String, primary_key=True)


class ClientBands(Base):
    __tablename__ = 'client_bands'

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    band = Column(String, ForeignKey('bands.name'))


engine = create_engine(
    'postgresql://postgres:password@localhost/testdb',
    connect_args={'check_same_thread': False},
)
