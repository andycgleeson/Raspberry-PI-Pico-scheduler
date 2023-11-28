from machine import Pin, PWM
from time import sleep


class Scheduler:
    def __init__(self, num_slots, sequence_duration):
        self.slots = num_slots
        self.slot_duration = sequence_duration / num_slots
        self.channels = []
        self.tasks = []
        self.resetChannels()

    def addChannel(self, channel):
        self.channels.append(channel)

    def addTask(self, task):
        self.tasks.append(task)

    def run(self):
        current_slot = 1
        while current_slot <= self.slots:
            for task in self.tasks:
                if current_slot >= task.start_slot and current_slot <= task.end_slot:
                    channel = self.getChannel(task.name)
                    self.render_value(current_slot, channel, task)
            sleep(self.slot_duration)
            current_slot += 1
        self.resetChannels()

    def getChannel(self, name):
        for channel in self.channels:
            if name == channel.name:
                return channel

    def render_value(self, current_slot, channel, task):
        current_val = channel.getValue()
        new_val = 0
        if task.action == "set":
            new_val = self.normalise_values(task.target_val, channel.max, channel.min)
        elif task.action == "high":
            new_val = channel.max
        elif task.action == "low":
            new_val = channel.min
        elif task.action == "ramp":
            if current_slot == task.start_slot:
                num_slots = task.end_slot - task.start_slot
                task.step_val = round((task.target_val - channel.value) / num_slots)
            new_val = self.normalise_values(current_val + task.step_val, channel.max, channel.min)
        if new_val != current_val:
            channel.setValue(new_val)

    def normalise_values(self, val, max, min):
        if val < min:
            val = min
        if val > max:
            val = max
        return round(val)

    def resetChannels(self):
        for channel in self.channels:
            channel.setValue(0)


class SchedulerChannel:
    def __init__(self, name, pin, max, min):
        self.name = name
        self.pin = pin
        self.value = 0
        self.max = max
        self.min = min
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(1000)

    def setValue(self, value):
        self.value = value
        self.pwm.duty_u16(self.value)

    def getValue(self):
        return self.value


class SchedulerTask:
    def __init__(self, start_slot, end_slot, target_val, name, action):
        self.start_slot = start_slot
        self.end_slot = end_slot
        self.target_val = target_val
        self.name = name
        self.action = action
        self.step_val = 0
