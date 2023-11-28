# Raspberry PI Pico scheduler

## Description

A simple event scheduler designed to control animated dioramas.
Currently only supports PWM channels, next version will support digital and I2c channels

## Dependencies

Paspberry PI Pico or Pico W loaded with micropython.

## Installing

Modify the main.py file to reflect your hardware setup and sequence.
Copy main.py and schedule.py to the PI Pico

## Executing program

main.py will need to altered to reflect your setup.

### Scheduler

The Scheduler class constructor accepts two parameters.

- **num_slots** The number of individual steps in a sequence at which an event can be initiated or end.
- **sequence_duration** Duration in seconds for entire sequence, this is a minimum as processing time is not accounted for.

### SchedulerChannel

SchedulerChannel objects describe the characteristics of the output channels, they are appended to the scheduler using the addChannel method

#### Parameters

- **name** A text string that uniquely describes the channel
- **pin** The gpio pin that will be used to output this channels values
- **max** The highest value that this channel supports
- **min** The lowest value supported by this channel

### SchedulerTask

SchedulerTask objects describe event values, start and stop times.

#### Parameters

- **start_slot** Time slot where action starts
- **end_slot** Time slot where action ends
- **target_value** Value to use
- **name** Name of channel action applies to
- **action** Action to perform

#### Action values

- **set** Set channel value to target_value
- **high** Set channel value to channel max
- **low** Set channel value to channel min
- **ramp** ramp from current value to target_value over duration of task

You can modify main.py to reflect how you want to start the sequence running.
Out of the box shorting GPIO pin 2 to ground will run the sequence.

## Authors

Contributors names and contact info

Andy Gleeson [andy\@carnivalofcrows.net](mailto:andy@carnivalofcrows.net)

## Version History

- 0.1
  - Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
