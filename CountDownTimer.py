import time


def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time -= 1
   print('Lift off!')


choice = int(input("Do you want to enter time in\n1. Seconds \n2. Minutes \n3. Hours \nEnter Your Choice: "))
if choice==1:
    user_time = int(input("Enter a time in seconds: "))
elif choice==2:
    mins_time = int(input("Enter a time in minutes: "))
    user_time = mins_time*60
else:
    hours_time = int(input("Enter a time in hours: "))
    user_time = hours_time*3600
countdown(user_time)
