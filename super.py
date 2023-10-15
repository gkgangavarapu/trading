import creds
from dhanhq import dhanhq


dhan =dhanhq(creds.client_id(),creds.access_token()) 

funds = dhan.get_fund_limits()

print(funds)
