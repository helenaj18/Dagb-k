import datetime


departure_time = datetime.datetime(2020,12,4,16,20,0).isoformat()

print(departure_time)

date, time = departure_time.split('T')

print(date)

departure_time2 = datetime.datetime(2020,12,4,0,0,0).isoformat()

print(departure_time2)




print('idag')
today = datetime.date.today()
print(today)

#d = datetime.datetime('2020-12-04T00:00:00').isoformat()

#d= datetime.strptime('2020-12-04T00:00:00', format)

print(dir(datetime))
#print(d)