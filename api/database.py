from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import settings


def get_url():
    user = settings.POSTGRES_USER
    password = settings.POSTGRES_PASSWORD
    db = settings.POSTGRES_DB
    server = settings.POSTGRES_SERVER
    return f"postgresql://{user}:{password}@{server}/{db}"


database_url = get_url()

engine = create_engine(database_url)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)

def get_session():
    session = Session()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close() 