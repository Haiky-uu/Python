#130. Get date from config file and display date and date-365 days (same thing you can do using 1 year or 12 months)
import conf2 as cf
import datetime

a = cf.start_date
print("Date: ",a)
print("Last year date:",a - datetime.timedelta(365))

