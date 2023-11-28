from machine import Pin
from scheduler import Scheduler, SchedulerChannel, SchedulerTask

start_button = Pin(2, Pin.IN, Pin.PULL_UP)

# params = number of slots, duration of sequence in seconds
scheduler = Scheduler(650, 90)


# params =  name, pin number, max value, min value
scheduler.addChannel(SchedulerChannel('led-green-right', 17, 65025, 0))
scheduler.addChannel(SchedulerChannel('led-green-left', 18, 65025, 0))
scheduler.addChannel(SchedulerChannel('led-flicker-red', 19, 65025, 0))
scheduler.addChannel(SchedulerChannel('led-flicker-orange', 20, 65025, 0))
scheduler.addChannel(SchedulerChannel('led-uv', 21, 65025, 0))


# params = start time slot, end time slot, target value, channel name, action
scheduler.addTask(SchedulerTask(1, 30, 65025, 'led-flicker-red', "ramp"))
scheduler.addTask(SchedulerTask(1, 30, 65025, 'led-flicker-orange', "ramp"))
scheduler.addTask(SchedulerTask(480, 600, 0, 'led-flicker-red', "ramp"))
scheduler.addTask(SchedulerTask(480, 600, 0, 'led-flicker-orange', "ramp"))

scheduler.addTask(SchedulerTask(40, 250, 65025, 'led-green-right', "ramp"))
scheduler.addTask(SchedulerTask(40, 250, 65025, 'led-green-left', "ramp"))
scheduler.addTask(SchedulerTask(301, 500, 0, 'led-green-right', "ramp"))
scheduler.addTask(SchedulerTask(301, 500, 0, 'led-green-left', "ramp"))

scheduler.addTask(SchedulerTask(450, 500, 65025, 'led-uv', "ramp"))
scheduler.addTask(SchedulerTask(580, 650, 0, 'led-uv', "ramp"))


while 1:
    if start_button.value() == 0:
        scheduler.run()
