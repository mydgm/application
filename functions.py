from main import User,Account, Transaction,local_session
from datetime import datetime,date
import os

def new_data(data):  #used to add transactions users or accounts
  if((data.__tablename__ = 'Transaction')):
    if(data.status == 'DECLINED' or (data.status == 'ACCEPTED') or (data.status == 'PENDING') ):
      local_session.add(data)
      local_session.commit()
    else:
      print("Invalid status")
      
  else:
    local_session.add(data)
    local_session.commit()
  
def get_user_balance(username):
  person = local_session.query(User).filter(User.username == str(username)).first()
  account = local_session.query(Account).filter(Account.user_id == person.user_id).first()
  return account.balance
  
def helper(day,month,year):
  while(True):
    try:
      new = date(year, month, day)
      break
    except:
      day = day -1
  return new
  
def within_month():
  today = date.today()
  if today.month == 1:
    year = today.year - 1
    month = 12
  else:
    year = today.year
    month = today.month - 1
    
  earliest = helper(today.day,month,year)
  print(today)
  between = Transaction.created_at.between(earliest,today)
  result  =  local_session.query(Transaction).filter(between).all()
  for s in result:
   print(f"transaction_id{s[0]} account_id{s[1]} ammount{s[2]} created_at {s[3]} status{s[4]}")
