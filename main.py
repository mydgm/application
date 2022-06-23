
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from sqlalchemy.orm import relationship,sessionmaker, Session
from datetime import datetime,date
import os

BASE_DIR = os.path.dirname(os.path.realpath("project2.py"))
Base = declarative_base()

session = sessionmaker()
connection_string = "sqlite:///"+os.path.join(BASE_DIR, 'site.db')
engine = create_engine(connection_string,echo = True)
local_session= session(bind=engine)
Base.metadata.create_all(engine)

class User(Base):
  __tablename__ = "Users"
  user_id = Column(Integer(), primary_key = True,autoincrement = True) #or can autoincrement
  username = Column(String(20), nullable = False, unique = True)
  
  def __rep__(self):
    return f"<User username = {self.username}"
  def get_tablename_(self):
    return self.__tablename__
  def get_user_id(self):
    return self.user_id
  def get_username(self):
    return self.username
  def __rep__(self):
    return f"<User username = {self.username}>"
  
  



class Account(Base):
  __tablename__ = "Accounts"
  account_id = Column(Integer(), primary_key = True, autoincrement = True) 
  user_id =  Column(Integer(), ForeignKey('Users.user_id'), nullable = False)
  us = relationship(User)
  balance = 0
  
  def get_tablename_(self):
    return self.__tablename__
  def get_account_id(self):
    return self.account_id
  def get_userid(self):
    return self.user_id
  def get_balance(self):
    return self.balance

class Transaction(Base):
  
  __tablename__ = "Transactions"
  transaction_id = Column(Integer(), primary_key = True)
  account_id = Column(Integer, ForeignKey('Accounts.account_id'), nullable = False)
  ammount = Column(Integer(), nullable = False)
  created_at = Column(DateTime(),nullable = False, default = datetime.utcnow)
  status= "PENDING"

  def get_tablename_(self):
    return self.__tablename__
  def get_account_id(self):
    return self.account_id
  def get_transaction_id(self):
    return self.transaction_id
  def get_amount(self):
    return self.ammount
  def get_status(self):
    return self.status
  def get_created_at(self):
    return self.created_at
  
  def update_status(self, new_status):
    if (((new_status == 'DECLINED') or (new_status == 'ACCEPTED')) and (self.status == 'PENDING')):
      updating =  local_session.query(Transaction).filter(Transaction.transaction_id == self.transaction_id).first()
      updating.status = new_status
      local_session.commit()
      if ((new_status == 'DECLINED') and (self.status != 'DECLINED')):
          self.status = 'DECLINED'
      if (new_status == 'ACCEPTED'and (self.status != 'ACCEPTED')):
          self.status = 'ACCEPTED'
          account = local_session.query(Account).filter(Account.account_id == updating.account_id).first()
          bal = account.balance
          new_bal = bal + self.ammount
          account.balance = new_bal
          local_session.commit()
        
        




