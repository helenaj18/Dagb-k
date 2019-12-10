import datetime


departure_time = datetime.datetime(2020,12,4,16,20,0).isoformat()

print(departure_time)

date, time = departure_time.split('T')

print(date)

departure_time2 = datetime.datetime(2020,12,4,0,0,0)

print(departure_time2)

<<<<<<< HEAD
print('date')
print(departure_time2.date())
=======
time_now = datetime.datetime.now()

year_now = time_now.year
month_now = time_now.month
day_now = time_now.day
hour_now = time_now.hour
mintue_now = time_now.minute


>>>>>>> 6a96f8b06e90bd9fb0f8366bad886a3f89492e22
print('idag')
today = datetime.date.today()
print(today)

#d = datetime.datetime('2020-12-04T00:00:00').isoformat()

#d= datetime.strptime('2020-12-04T00:00:00', format)

print(dir(datetime))
#print(d)


cool = type('cool')

a_list = [1,2,3]
b_list = [4,5,6]
print(a_list+b_list)


yes = datetime.datetime(2019,11,20,15,30,0,0)
print(type(yes))
print(yes.hour)

if type(yes) == datetime.datetime:
    print('JAAAS')

yesyes = yes.date().isoformat()
print(type(yesyes))