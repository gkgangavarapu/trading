import pandas as pd
import numpy as np
import creds
from dhanhq import dhanhq
from nsepython import *
###################################
print("Hello world")
dhan = dhanhq(creds.client_id(),creds.access_token())

holdings = dhan.get_holdings()

print(holdings)

ltp_nifty = nse_quote_ltp("NIFTY")
print(ltp_nifty)
