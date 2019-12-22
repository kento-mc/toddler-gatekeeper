import time
import datetime
import os
import sys
from multiprocessing import Process
from contextlib import contextmanager
import urllib2
from wia import Wia
from sense_hat import SenseHat

# set up Wia
wia = Wia()
wia.access_token = "d_sk_yxhosMPKxwC9HIg2pZLxi4w3"

# set up Thingspeak
WRITE_API_KEY='ON0J9PUVWMEQZ9RH'
baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

# instnsiate SenseHat object and apply settings
sense = SenseHat()
sense.set_rotation(270)
sense.clear()
red = (255,0,0)
green = (0,255,0)

# create database on DB server (Macbook Pro), if it does not already exist
os.system("mysql -uroot -h192.168.0.45 --password='steviey19' -e \"CREATE DATABASE IF NOT EXISTS doorOpenDB\"")
os.system("mysql -uroot -h192.168.0.45 --password='steviey19' -e \"CREATE TABLE IF NOT EXISTS doorOpenDB.OpenEvents (doorOpen TIMESTAMP)\"")

# count arguments
args = len(sys.argv)-1

if args != 0: # if there is a time threshold argument provided
  wake_up = sys.argv[1] # save command line argument to wake_up variable
  threshold = datetime.datetime.strptime(wake_up, "%H:%M:%S") # convert to datetime format

# store current time in variable
current_time = time.strftime("%H:%M:%S", time.localtime()) # save current time to current_time string variable
now = datetime.datetime.strptime(current_time, "%H:%M:%S") # convert to datetime format

def writeData(x): # function to send data to thingspeak
  conn = urllib2.urlopen(baseURL + '&field1=%s' % (x))
  print(conn.read())
  conn.close()

def LEDs(): # function for LED display
  if args == 0 or now.time() < threshold.time(): # if there is no argument provided or if the time argument is earlier than the current time.
    sense.show_message("Back to bed kiddo!", scroll_speed = 0.035, text_colour = red) # display message
  else:
    sense.show_message("Good morning!", scroll_speed = 0.035, text_colour = green) # display message

def audio(): # function for audio playback via bluetooth
  if args == 0 or now.time() < threshold.time(): # if there is no argument provided or if the time argument is earlier than the current time.
    os.system('mpg123 -q /home/pi/dev/wit/compsys19/assignments/02/audio-files/back-to-bed.mp3') # play mp3
  else:
    os.system('mpg123 -q /home/pi/dev/wit/compsys19/assignments/02/audio-files/good-morning.mp3') # play mp3

while True: # main programme loop. will run as long as script is running
  doorOpen = False # doorOpen event reset
  motion = sense.get_accelerometer_raw()

  x = round(motion['x'], 4) # parse the JSON data for x value and round it
  y = round(motion['y'], 4) # parse the JSON data for y value and round it
  z = round(motion['z'], 4) # parse the JSON data for z value and round it

  # print accelerometer readings and time to console for testing purposes
  print("x={0}, y={1}, z={2}".format(x, y, z))

  while x > 0.975: # door is opened
    if doorOpen == False: # if door had been closed until while loop was triggered
      doorOpen = True # set status of door to open

      print("\nDoor Open at {}!\n".format(now.time()))

      # save door open event timestamp to DB server
      os.system("mysql -h 192.168.0.45 -uroot --password='steviey19' -e \"insert into doorOpenDB.OpenEvents(doorOpen) VALUES(CURRENT_TIMESTAMP)\"")

      writeData(x) # send data to thingspeak

      wia.Event.publish(name="door open", data = str(now.time())) # publish event to wia

      if __name__ == '__main__':
        Process(target=LEDs).start() # run LED process
        Process(target=audio).start() # run audio process

    x = sense.get_accelerometer_raw()['x'] # check for whether door has been closed

  time.sleep(.5) # set delay between reads of the accelerometer data
