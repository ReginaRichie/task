from sqlalchemy.orm import sessionmaker
from app.database.database_setup import engine

Session = sessionmaker(bind=engine)
