import  time
import urllib2
from wia import Wia
from sense_hat import SenseHat

wia = Wia()
wia.access_token = "d_sk_yxhosMPKxwC9HIg2pZLxi4w3"

WRITE_API_KEY='ON0J9PUVWMEQZ9RH'
baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()
sense.set_rotation(270)
sense.clear()
red = (255,0,0)
green = (0,255,0)

# create database on DB server (Macbook Pro)
mysql -uroot -h192.168.0.45 -e "CREATE DATABASE doorOpenDB"
mysql -uroot -h192.168.0.45 -e "CREATE TABLE doorOpenDB.OpenEvents (doorOpen TIMESTAMP)"

def writeData(x) # function to send data to thingspeak
  conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s' % (x))
  print(conn.read())
  conn.close()

while True:
  doorOpen = False # doorOpen event reset
  motion = sense.get_accelerometer_raw()

  x = round(motion['x'], 4)
  y = motion['y']
  z = motion['z']

  #x = round(x, 4)
  y = round(y, 4)
  z = round(z, 4)

  print("x={0}, y={1}, z={2}".format(x, y, z))

  while x > 0.8: # door is opened
    if doorOpen == False: # if door had been closed until while loop was triggered
      doorOpen = True # set status of door to open

      writeData(x) # send data to thingspeak

      wia.Event.publish(name="door open test", data = motion) # publish event to wia
      sense.show_message("Back to bed kiddo!", text_colour = red) # display message

      # save door open event timestamp to DB server
      mysql -h 192.168.0.45 -uroot -e "insert into doorOpenDB.OpenEvents(doorOpen) VALUES(CURRENT_TIMESTAMP)"

    x = sense.get_accelerometer_raw()['x'] # check for whether door has been closed

  time.sleep(.5)
