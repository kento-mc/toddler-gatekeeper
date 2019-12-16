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
  eventCount = 0 # doorOpen event reset
  motion = sense.get_accelerometer_raw()

  x = motion['x']
  y = motion['y']
  z = motion['z']

  x = round(x, 4)
  y = round(y, 4)
  z = round(z, 4)

  print("x={0}, y={1}, z={2}".format(x, y, z))

  while x > 0.8:
    if eventCount == 0:
      wia.Event.publish(name="door open test", data = motion)
      eventCount = 1
      sense.show_message("Back to bed kiddo!", text_colour = red)
      time.sleep(5)

      motion = sense.get_accelerometer_raw()
      x = motion['x']

  time.sleep(.5)
