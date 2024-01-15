from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
  """ created State class"""
  __init__ = 'states'
  id = Column(String(128), primary_key=True)

  def display_state(self):
    print("ID: ", self.id)


  

