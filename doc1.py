from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from sqlalchemy.orm import relationship
from datetime import datetime
import os

#BASE_DIR = os.path.dirname(os.path.realpath("Untitled2"))#file)))
Base = declarative_base()
#engine = create_engine()

connection_string = ""


class User(Base):
  __tablename__ = "Users"
  user_id = Column(Integer(), primary_key = True)
  username = Column(String(20), nullable = False, unique = True)
  
  def __rep__(self):
    return f"<User username = {self.username}"
  def get_tablename_(self):
    return self.__tablename__
  def get_user_id(self):
    return self.user_id
  def get_username(self):
    return self.username
  
  

user = User(user_id = 1, username = "nick")
print(user.get_user_id())
print(user.username)

class Account(Base):
  __tablename__ = "Accounts"
  account_id = Column(Integer(), primary_key = True)
  user_id = Column(Integer, ForeignKey('Users.user_id'))
  balance = Column(Integer(), nullable = False)
  #account = relationship("Users", foreign_keys= "Users.user_id")
  
  def get_tablename_(self):
    return self.__tablename__
  def get_account_id(self):
    return self.account_id
  def get_userid(self):
    return self.user_id

class Transaction(Base):
  __tablename__ = "Transactions"
  transaction_id = Column(Integer(), primary_key = True)
  account_id = Column(Integer, ForeignKey('Account.account_id'), nullable = False)
  created_at = Column(DateTime(),nullable = False, default = datetime.utcnow)
  status= Column(String(8),nullable = False)
