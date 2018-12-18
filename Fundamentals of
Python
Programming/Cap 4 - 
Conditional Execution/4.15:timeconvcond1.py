#4.15:timeconvcond1.py
seconds_per_minute = 60
seconds_per_hour = 60*seconds_per_minute

seconds = int(input('Please enter the number of seconds: '))

hours = seconds // seconds_per_hour
seconds = seconds % seconds_per_hour

minutes = seconds // seconds_per_minute
seconds = seconds % seconds_per_minute

print(hours, end='')
if(hours == 1):
    print(' hour ', end='')
else:
    print(' hours ', end='')

print(minutes, end='')
if(minutes == 1):
    print(' minute ', end='')
else:
    print(' minutes ', end='')

print(seconds, end='')
if(seconds == 1):
    print(' second ', end='')
else:
    print(' seconds ', end='')
