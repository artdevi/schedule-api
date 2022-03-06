from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgresql+psycopg2://postgres:password@localhost/testdb'

engine = create_engine(DATABASE_URI)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
