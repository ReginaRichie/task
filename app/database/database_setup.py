
# создание и подключение к базе данных

# from app.database.database_setup import engine
from sqlalchemy.engine import create_engine
import settings
# from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(settings.DATABASE_URL)
Base = declarative_base()



