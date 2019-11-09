# Project Name
#### Student Name: Kent Chadwick   Student ID: 20086513

I would like to build a door-opening detector for a children's room using the Raspberry Pi and Sense Hat that performs serveral functions when the door opens. This is motivated by my own experience of my two small children who often manage to get up from their beds and leave the room without making enough noise to activate the baby monitor. 

I want to try the to implement the following: 

1. Send a message to the parents' (or other caretakers') phones to alert them that the door has opened.
2. Log the door-opening event to an IOT platform so that the children opening the door in the night can be tracked over multiple days.
3. Store these events in local database.
4. Display a color (red or green) on the Sense Hat LEDs based on the time the door is opened to indicate to the child that it's either too early and they're not supposed to leave the room, or that it's not morning and they are free to come out. (I understand that abiding by this isn't really a realistic expectation of a 4 year old...)
5. Play a recorded message over a bluetooth speaker that corresponds to the color indicator in #4. If it's too early (red), play a message like "It's still night time, everyone stay in bed." If it's after 7am (green) play a message like "Good morning!"

## Tools, Technologies and Equipment

Hardware

I am planning to use the Raspberry Pi and Sense Hat, either mounted to the door itself or mounted to the wall with some sort of attachment to the door. I would make use of the Sense Hat's accelerometer to detect the door movement and its LED array to flash red or green depending on the time.

Programming languages

I am planning to expand on what we've done so far with Python this semester, because I'd like to develop my knowledge of it further. I might fall back on Java if I get stuck.

I will also use mysql to create the database to store the door-open events.

Networking protocalls

I plan to use MQTT to send messages to subscribers (parents).

IOT Platform

I will use WIA to track the door-open events over time.

## Project Repository
https://github.com/kento-mc/wit-2019-compsys-02

