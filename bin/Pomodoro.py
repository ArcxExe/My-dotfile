from datetime import datetime
import time
def current_time(stop_time=0):

    current_datetime = datetime.now()
    current_hour = current_datetime.hour
    current_minute = current_datetime.minute
    if stop_time == 0:
        print(f"Текущее время: {current_hour}:{current_minute:02}")
    else:
        stop_minute = stop_time % 60
        stop_hour = stop_time // 60
        if current_minute + stop_minute >= 60:
            end_time_minute = (current_minute + stop_minute) % 60
            return f"Мы Закончим: {current_hour+stop_hour+1}:{end_time_minute:02}"
        return f"Мы закончим: {current_hour+stop_hour}:{current_minute+stop_minute:02}"


def work():
    print("Начнем работу!")
    global stop_minute
    current_time()
    stop_minute = int(input("Скажи через сколько минут мне выключиться ? "))
    print(current_time(stop_minute))
    # a = stop_minute
    print("Начнем сессию Pomodoro!")
    while stop_minute != 0:
        time.sleep(60) 
        stop_minute = stop_minute-1
        print(f"Осталось: {stop_minute} минут ")
  
def sleep():
    print("Отдых ухх хорошо потрудились!")
    stop_sleep = int(input("Сколько будем отдыхать? "))
    while stop_sleep != 0:
        time.sleep(60) 
        stop_sleep = stop_sleep - 1
        print(f"Осталось: {stop_sleep} минут ")

session = int(input("Сколько сессий будет Pomodoro? "))
for i in range(session):
    print(f"Да начнется сессия номер {i+1}")
    work()
    sleep()
else:
    work()
print("Работа оконечена.")
