# s1 = {"Name":"Jaydip"}
# s2 = {"education":"maths"}
# s3 = {"result":"pass"}

# s ={**s1,**s2,**s3}
# print(s)

import datetime as dt

d=dt.datetime.now()

date= d.strftime("%f")
print("Microsecond:",date)

date =d.time()
print(date)
