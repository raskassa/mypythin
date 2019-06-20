
from datetime import datetime, timedelta

d = datetime.strptime('Jun 1 2005  11:33PM', '%b %d %Y %I:%M%p')
e = datetime.strptime('Jun 21 2005  06:33AM', '%b %d %Y %I:%M%p')
f = datetime.strptime('10 1 2015  08:33AM',    '%m %d %Y %H:%M%p')
print(d)
print(e)
print(f)
print(e - d)
print(d + timedelta(days=21))
print(d.strftime("%A"))
x = int(f.strftime("%Y")) - int(d.strftime("%Y"))
print(x)


