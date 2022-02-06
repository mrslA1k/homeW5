from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
url = 'sqlite:///local.db'
engine = create_engine(url, echo=False)
Base=declarative_base()