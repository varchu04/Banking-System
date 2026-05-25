import os 
import re

def is_valid_indian_phone_number(phone_number):
    # Define the regex pattern for a valid Indian phone number
    pattern = re.compile(r'^(?:\+?91)?[6789]\d{9}$')
    
    # Check if the phone number matches the pattern
    if pattern.match(phone_number):
        return True
    else:
        return False
    
class bank:
  def accountinfo(accounts,account_name,phno):
    if account_name not in accounts and phno not in accounts:
        accounts[account_name] = bank()
        print("name of the depositor added successfully")
        accounts[phno] = bank()
        print("phone number added successfully")
    else:
       print("account does not exists.create a new account for valid inputs")
