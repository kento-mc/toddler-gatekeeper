import  time
from wia import Wia
from sense_hat import SenseHat

wia = Wia()
wia.access_token = "d_sk_yxhosMPKxwC9HIg2pZLxi4w3"

sense = SenseHat()
sense.clear()
red = (255,0,0)
green = (0,255,0)

while True:
  doorOpen = False # doorOpen event reset
  motion = sense.get_accelerometer_raw()

  x = motion['x']
  y = motion['y']
  z = motion['z']

  x = round(x, 4)
  y = round(y, 4)
  z = round(z, 4)

  print("x={0}, y={1}, z={2}".format(x, y, z))

  while x > 0.8: # door is opened
    if doorOpen == False: # if door had been closed until while loop was triggered
      doorOpen = True # set status of door to open
      wia.Event.publish(name="door open test", data = motion) # publish event
      sense.show_message("Back to bed kiddo!", text_colour = red) # display message

    x = sense.get_accelerometer_raw()['x'] # check for whether door has been closed

  time.sleep(.5)
